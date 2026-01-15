// Configuration
const API_BASE_URL = 'http://localhost:8000/api';
const ANIMATION_SPEED_DEFAULT = 500;

// Application State
const state = {
    map: null,
    graphData: null,
    selectedStartNode: null,
    selectedEndNode: null,
    nodeMarkers: {},
    edgePolylines: [],
    animationSpeed: ANIMATION_SPEED_DEFAULT,
    isAnimating: false,
    animationPaused: false,
    currentAnimation: null
};

// Initialize application
document.addEventListener('DOMContentLoaded', () => {
    initializeMap();
    attachEventListeners();
    hideLoading();
    // Auto-start with empty canvas
    startEmptyCanvas();
});

// Initialize Leaflet Map
function initializeMap() {
    // Center at user-specified coordinates
    const center = [10.803451, 106.719046];

    state.map = L.map('map').setView(center, 15);

    // Add OpenStreetMap tile layer
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors',
        maxZoom: 19
    }).addTo(state.map);

    // Add click handler to map for creating custom nodes
    state.map.on('click', function (e) {
        // Only allow if graph data exists
        if (!state.graphData) {
            showError('Please load map data first');
            return;
        }

        const lat = e.latlng.lat;
        const lon = e.latlng.lng;

        // Create custom node ID
        const customId = `custom_${Date.now()}`;
        const nodeNumber = state.graphData.nodes.length + 1;

        // Create new node
        const newNode = {
            id: customId,
            lat: lat,
            lon: lon,
            label: `Custom ${nodeNumber}`
        };

        // Add to graph data
        state.graphData.nodes.push(newNode);

        // Create marker with distinct style
        const marker = L.circleMarker([lat, lon], {
            radius: 8,
            fillColor: '#fbbf24', // Yellow for custom nodes
            color: '#fff',
            weight: 3,
            opacity: 1,
            fillOpacity: 0.9
        }).addTo(state.map);

        marker.bindPopup(`<b>Custom Node ${nodeNumber}</b><br>Lat: ${lat.toFixed(6)}<br>Lon: ${lon.toFixed(6)}<br><em>Click created</em>`);

        // Add click handler - prevent event bubbling
        marker.on('click', function (event) {
            L.DomEvent.stopPropagation(event);
            selectNode(customId);
        });

        state.nodeMarkers[customId] = marker;

        // Update dropdowns
        populateNodeSelectors(state.graphData.nodes);
        updateStats(state.graphData.nodes.length, state.graphData.edges.length);

        // Auto-select as start/end node
        selectNode(customId);

        showSuccess(`Custom node created: ${newNode.label}`);
        console.log('Custom node created:', customId, 'at', lat.toFixed(6), lon.toFixed(6));
    });

    console.log('Map initialized with click-to-create functionality');
}

// Event Listeners
function attachEventListeners() {
    // Canvas controls
    document.getElementById('load-map-btn').addEventListener('click', loadMapData);
    document.getElementById('empty-canvas-btn').addEventListener('click', startEmptyCanvas);
    document.getElementById('clear-map-btn').addEventListener('click', clearMap);

    // Algorithm buttons
    document.getElementById('bfs-btn').addEventListener('click', () => runAlgorithm('bfs'));
    document.getElementById('dfs-btn').addEventListener('click', () => runAlgorithm('dfs'));
    document.getElementById('shortest-path-btn').addEventListener('click', () => runAlgorithm('shortest-path'));
    document.getElementById('bipartite-btn').addEventListener('click', runBipartiteCheck);

    // Conversion
    document.getElementById('convert-btn').addEventListener('click', convertRepresentation);
    document.getElementById('representation-format').addEventListener('change', (e) => {
        document.getElementById('convert-btn').disabled = !e.target.value;
    });

    // Save/Load
    document.getElementById('save-btn').addEventListener('click', saveGraph);
    document.getElementById('load-btn').addEventListener('click', showLoadModal);

    // Animation
    document.getElementById('animation-speed').addEventListener('input', (e) => {
        state.animationSpeed = parseInt(e.target.value);
        document.getElementById('speed-value').textContent = `${e.target.value}ms`;
    });
    document.getElementById('pause-btn').addEventListener('click', toggleAnimationPause);

    // Node selection
    document.getElementById('start-node').addEventListener('change', (e) => {
        state.selectedStartNode = e.target.value;
        updateButtonStates();
    });
    document.getElementById('end-node').addEventListener('change', (e) => {
        state.selectedEndNode = e.target.value;
        updateButtonStates();
    });

    // Clear results
    document.getElementById('clear-results-btn').addEventListener('click', clearResults);

    // Add reset selections button handler
    const clearMapBtn = document.getElementById('clear-map-btn');
    clearMapBtn.addEventListener('click', () => {
        // Clear highlights but keep the graph data
        if (state.selectedStartNode) {
            highlightNode(state.selectedStartNode, '#06b6d4');
        }
        if (state.selectedEndNode) {
            highlightNode(state.selectedEndNode, '#06b6d4');
        }
        state.selectedStartNode = null;
        state.selectedEndNode = null;
        document.getElementById('start-node').value = '';
        document.getElementById('end-node').value = '';
        clearHighlights();
        updateButtonStates();
        showSuccess('Node selections cleared');
    });

    // Modal
    document.getElementById('modal-close').addEventListener('click', closeModal);
    document.getElementById('modal').addEventListener('click', (e) => {
        if (e.target.id === 'modal') closeModal();
    });
}

// API calls
async function loadMapData() {
    try {
        setStatus('Loading...', 'loading');
        showLoading('Fetching map data from OpenStreetMap...');

        const response = await fetch(`${API_BASE_URL}/map-data?major_roads_only=true`);
        const data = await response.json();

        if (data.success && data.graph) {
            state.graphData = data.graph;
            renderGraph(data.graph);
            populateNodeSelectors(data.graph.nodes);
            updateStats(data.metadata.node_count, data.metadata.edge_count);
            setStatus('Ready', 'ready');
            showSuccess(`Loaded ${data.metadata.node_count} nodes and ${data.metadata.edge_count} edges`);
        } else {
            throw new Error('Failed to load map data');
        }

        hideLoading();
    } catch (error) {
        console.error('Error loading map data:', error);
        showError('Failed to load map data. Please try again.');
        setStatus('Error', 'error');
        hideLoading();
    }
}

function startEmptyCanvas() {
    // Create empty graph for custom nodes only
    state.graphData = {
        nodes: [],
        edges: [],
        directed: false,
        metadata: {
            source: 'Empty Canvas',
            area: 'Custom Graph - District 1, Ho Chi Minh City',
            timestamp: Date.now()
        }
    };

    clearMap();
    updateStats(0, 0);
    setStatus('Ready', 'ready');
    showSuccess('Empty canvas ready! Click on the map to create custom nodes.');
    console.log('Started with empty canvas');
}

async function runAlgorithm(algorithm) {
    if (!state.graphData) {
        showError('Please load map data first');
        return;
    }

    const startNode = state.selectedStartNode;
    const endNode = state.selectedEndNode;

    if (!startNode) {
        showError('Please select a start node');
        return;
    }

    if (algorithm === 'shortest-path' && !endNode) {
        showError('Please select both start and end nodes for shortest path');
        return;
    }

    try {
        setStatus('Running...', 'running');
        clearHighlights();

        const endpoint = algorithm === 'shortest-path' ? 'shortest-path' : algorithm;
        const algorithmName = algorithm.replace('-', '_'); // Convert to snake_case for API

        const response = await fetch(`${API_BASE_URL}/${endpoint}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                graph: state.graphData,
                algorithm: algorithmName,
                start_node: startNode,
                end_node: endNode
            })
        });

        const data = await response.json();

        if (data.success) {
            await animateAlgorithm(data);
            displayAlgorithmResult(data);
            setStatus('Complete', 'complete');
        } else {
            throw new Error(data.error || 'Algorithm execution failed');
        }
    } catch (error) {
        console.error('Error running algorithm:', error);
        showError(`Failed to run ${algorithm}: ${error.message}`);
        setStatus('Error', 'error');
    }
}

async function runBipartiteCheck() {
    if (!state.graphData) {
        showError('Please load map data first');
        return;
    }

    try {
        setStatus('Checking...', 'running');
        clearHighlights();

        const response = await fetch(`${API_BASE_URL}/check-bipartite`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                graph: state.graphData,
                algorithm: 'bipartite'
            })
        });

        const data = await response.json();

        if (data.success) {
            await animateAlgorithm(data);

            const resultBox = document.getElementById('bipartite-result');
            resultBox.style.display = 'block';

            if (data.result.is_bipartite) {
                resultBox.innerHTML = `
                    <strong style="color: var(--accent-green)">✓ Graph is BIPARTITE</strong><br>
                    Set A: ${data.result.set_a.length} nodes<br>
                    Set B: ${data.result.set_b.length} nodes
                `;
                resultBox.style.borderColor = 'var(--accent-green)';
            } else {
                resultBox.innerHTML = `
                    <strong style="color: var(--accent-red)">✗ Graph is NOT BIPARTITE</strong><br>
                    The graph contains odd cycles.
                `;
                resultBox.style.borderColor = 'var(--accent-red)';
            }

            setStatus('Complete', 'complete');
        }
    } catch (error) {
        console.error('Error checking bipartite:', error);
        showError('Failed to check bipartite property');
        setStatus('Error', 'error');
    }
}

async function convertRepresentation() {
    if (!state.graphData) {
        showError('Please load map data first');
        return;
    }

    const format = document.getElementById('representation-format').value;
    if (!format) return;

    try {
        const response = await fetch(`${API_BASE_URL}/convert-representation`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                graph: state.graphData,
                from_format: 'graph',
                to_format: format
            })
        });

        const data = await response.json();

        if (data.success) {
            displayConversionResult(data.to_format, data.data);
        } else {
            throw new Error(data.error);
        }
    } catch (error) {
        console.error('Error converting representation:', error);
        showError('Failed to convert graph representation');
    }
}

async function saveGraph() {
    if (!state.graphData) {
        showError('Please load map data first');
        return;
    }

    const name = document.getElementById('graph-name').value.trim() || 'Untitled';

    try {
        const response = await fetch(`${API_BASE_URL}/save-graph`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                name: name,
                graph: state.graphData
            })
        });

        const data = await response.json();

        if (data.success) {
            showSuccess(`Graph saved as: ${data.filename}`);
            document.getElementById('graph-name').value = '';
        } else {
            throw new Error(data.error);
        }
    } catch (error) {
        console.error('Error saving graph:', error);
        showError('Failed to save graph');
    }
}

async function showLoadModal() {
    try {
        const response = await fetch(`${API_BASE_URL}/saved-graphs`);
        const data = await response.json();

        if (data.success) {
            const modalBody = document.getElementById('modal-body');

            if (data.graphs.length === 0) {
                modalBody.innerHTML = '<p style="text-align: center; color: var(--text-muted);">No saved graphs found.</p>';
            } else {
                modalBody.innerHTML = data.graphs.map(graph => `
                    <div class="saved-graph-item" onclick="loadSavedGraph('${graph.filename}')">
                        <div class="saved-graph-info">
                            <h5>${graph.name}</h5>
                            <p>${graph.node_count} nodes, ${graph.edge_count} edges • ${new Date(graph.saved_at).toLocaleString()}</p>
                        </div>
                    </div>
                `).join('');
            }

            document.getElementById('modal-title').textContent = 'Load Saved Graph';
            document.getElementById('modal').style.display = 'flex';
        }
    } catch (error) {
        console.error('Error loading saved graphs:', error);
        showError('Failed to load saved graphs');
    }
}

async function loadSavedGraph(filename) {
    try {
        const response = await fetch(`${API_BASE_URL}/load-graph/${filename}`);
        const data = await response.json();

        if (data.success && data.graph) {
            state.graphData = data.graph;
            renderGraph(data.graph);
            populateNodeSelectors(data.graph.nodes);
            updateStats(data.graph.nodes.length, data.graph.edges.length);
            setStatus('Ready', 'ready');
            showSuccess(`Loaded graph: ${filename}`);
            closeModal();
        } else {
            throw new Error(data.error);
        }
    } catch (error) {
        console.error('Error loading graph:', error);
        showError('Failed to load graph');
    }
}

// Rendering
function renderGraph(graphData) {
    clearMap();

    // Render edges first (so they appear below nodes)
    graphData.edges.forEach(edge => {
        const sourceNode = graphData.nodes.find(n => n.id === edge.source);
        const targetNode = graphData.nodes.find(n => n.id === edge.target);

        if (sourceNode && targetNode) {
            const polyline = L.polyline(
                [[sourceNode.lat, sourceNode.lon], [targetNode.lat, targetNode.lon]],
                {
                    color: '#4b5563',
                    weight: 2,
                    opacity: 0.6
                }
            ).addTo(state.map);

            state.edgePolylines.push({
                polyline: polyline,
                source: edge.source,
                target: edge.target
            });
        }
    });

    // Render nodes
    graphData.nodes.forEach(node => {
        const marker = L.circleMarker([node.lat, node.lon], {
            radius: 6,
            fillColor: '#06b6d4',
            color: '#fff',
            weight: 2,
            opacity: 1,
            fillOpacity: 0.8
        }).addTo(state.map);

        marker.bindPopup(`<b>Node ${node.id}</b><br>Lat: ${node.lat.toFixed(6)}<br>Lon: ${node.lon.toFixed(6)}`);

        marker.on('click', () => selectNode(node.id));

        state.nodeMarkers[node.id] = marker;
    });

    // Fit bounds to show all nodes
    if (graphData.nodes.length > 0) {
        const bounds = L.latLngBounds(graphData.nodes.map(n => [n.lat, n.lon]));
        state.map.fitBounds(bounds, { padding: [50, 50] });
    }
}

function selectNode(nodeId) {
    console.log('Node clicked:', nodeId);
    console.log('Current state - Start:', state.selectedStartNode, 'End:', state.selectedEndNode);

    // If clicking the same node that's already selected, deselect it
    if (state.selectedStartNode === nodeId) {
        console.log('Deselecting start node');
        state.selectedStartNode = null;
        document.getElementById('start-node').value = '';
        highlightNode(nodeId, '#06b6d4'); // Reset to default color
        updateButtonStates();
        return;
    }

    if (state.selectedEndNode === nodeId) {
        console.log('Deselecting end node');
        state.selectedEndNode = null;
        document.getElementById('end-node').value = '';
        highlightNode(nodeId, '#06b6d4'); // Reset to default color
        updateButtonStates();
        return;
    }

    // Select start node if not yet selected
    if (!state.selectedStartNode) {
        console.log('Selecting as start node');
        state.selectedStartNode = nodeId;
        document.getElementById('start-node').value = nodeId;
        highlightNode(nodeId, '#f97316'); // Orange for start
        showSuccess(`Start node selected: ${nodeId}`);
    }
    // Select end node if start is already selected
    else if (!state.selectedEndNode && nodeId !== state.selectedStartNode) {
        console.log('Selecting as end node');
        state.selectedEndNode = nodeId;
        document.getElementById('end-node').value = nodeId;
        highlightNode(nodeId, '#10b981'); // Green for end
        showSuccess(`End node selected: ${nodeId}`);
    }
    // If both are selected, reset and start over
    else {
        console.log('Both nodes already selected, resetting...');
        // Clear all previous selections
        if (state.selectedStartNode) {
            highlightNode(state.selectedStartNode, '#06b6d4');
        }
        if (state.selectedEndNode) {
            highlightNode(state.selectedEndNode, '#06b6d4');
        }

        // Set new start node
        state.selectedStartNode = nodeId;
        state.selectedEndNode = null;
        document.getElementById('start-node').value = nodeId;
        document.getElementById('end-node').value = '';
        highlightNode(nodeId, '#f97316');
        showSuccess(`Start node reset to: ${nodeId}`);
    }

    updateButtonStates();
    console.log('Updated state - Start:', state.selectedStartNode, 'End:', state.selectedEndNode);
}

function highlightNode(nodeId, color) {
    const marker = state.nodeMarkers[nodeId];
    if (marker) {
        marker.setStyle({
            fillColor: color,
            radius: 8,
            weight: 3
        });
    }
}

function clearHighlights() {
    // Reset all nodes
    Object.values(state.nodeMarkers).forEach(marker => {
        marker.setStyle({
            fillColor: '#06b6d4',
            radius: 6,
            weight: 2
        });
    });

    // Reset all edges
    state.edgePolylines.forEach(({ polyline }) => {
        polyline.setStyle({
            color: '#4b5563',
            weight: 2,
            opacity: 0.6
        });
    });
}

async function animateAlgorithm(algorithmData) {
    if (!algorithmData.steps || algorithmData.steps.length === 0) return;

    clearResults();
    const resultsContent = document.getElementById('results-content');
    resultsContent.innerHTML = '<div class="step-container"></div>';
    const stepContainer = resultsContent.querySelector('.step-container');

    state.isAnimating = true;
    document.getElementById('pause-btn').disabled = false;

    for (let i = 0; i < algorithmData.steps.length; i++) {
        if (state.animationPaused) {
            await new Promise(resolve => {
                const checkPause = setInterval(() => {
                    if (!state.animationPaused) {
                        clearInterval(checkPause);
                        resolve();
                    }
                }, 100);
            });
        }

        const step = algorithmData.steps[i];

        // Display step
        const stepDiv = document.createElement('div');
        stepDiv.className = 'step-item';
        stepDiv.textContent = `Step ${step.step}: ${step.description}`;
        stepContainer.appendChild(stepDiv);
        stepContainer.scrollTop = stepContainer.scrollHeight;

        // Visualize step on map
        if (step.node) {
            highlightNode(step.node, '#8b5cf6');
        }

        if (step.edge) {
            highlightEdge(step.edge.source, step.edge.target, '#8b5cf6');
        }

        await sleep(state.animationSpeed);
    }

    // Highlight final result
    if (algorithmData.result?.path) {
        highlightPath(algorithmData.result.path);
    }

    state.isAnimating = false;
    document.getElementById('pause-btn').disabled = true;
}

function highlightEdge(source, target, color) {
    const edge = state.edgePolylines.find(e =>
        (e.source === source && e.target === target) ||
        (e.source === target && e.target === source)
    );

    if (edge) {
        edge.polyline.setStyle({
            color: color,
            weight: 4,
            opacity: 1
        });
    }
}

function highlightPath(path) {
    for (let i = 0; i < path.length; i++) {
        highlightNode(path[i], '#10b981');

        if (i < path.length - 1) {
            highlightEdge(path[i], path[i + 1], '#10b981');
        }
    }

    // Show path result
    const resultBox = document.getElementById('path-result');
    resultBox.style.display = 'block';
    resultBox.innerHTML = `
        <strong style="color: var(--accent-green)">Path Found!</strong><br>
        Length: ${path.length} nodes<br>
        Path: ${path.join(' → ')}
    `;
    resultBox.style.borderColor = 'var(--accent-green)';
}

function displayAlgorithmResult(data) {
    const resultsContent = document.getElementById('results-content');

    let resultHTML = `<h4>${data.algorithm.toUpperCase()} Results</h4>`;

    if (data.result.traversal_order) {
        resultHTML += `<p><strong>Traversal Order:</strong> ${data.result.traversal_order.join(' → ')}</p>`;
        resultHTML += `<p><strong>Nodes Visited:</strong> ${data.result.visited_count}</p>`;
    }

    if (data.result.path) {
        resultHTML += `<p><strong>Shortest Path:</strong> ${data.result.path.join(' → ')}</p>`;
        resultHTML += `<p><strong>Total Distance:</strong> ${data.result.distance?.toFixed(2)} meters</p>`;
    }

    resultsContent.innerHTML += `<div class="result-box">${resultHTML}</div>`;
}

function displayConversionResult(format, data) {
    const resultsContent = document.getElementById('results-content');
    resultsContent.innerHTML = '';

    let displayHTML = `<h4>${format.replace('_', ' ').toUpperCase()}</h4>`;

    if (format === 'adjacency_matrix') {
        displayHTML += '<pre style="font-size: 0.75rem; overflow-x: auto;">';
        displayHTML += data.matrix.map(row => row.map(v => v.toFixed(0).padStart(3)).join(' ')).join('\n');
        displayHTML += '</pre>';
    } else if (format === 'adjacency_list') {
        displayHTML += '<pre style="font-size: 0.75rem; overflow-y: auto; max-height: 200px;">';
        Object.entries(data.adjacency_list).forEach(([node, neighbors]) => {
            displayHTML += `${node}: ${neighbors.map(n => n.node).join(', ')}\n`;
        });
        displayHTML += '</pre>';
    } else if (format === 'edge_list') {
        displayHTML += `<p><strong>Total Edges:</strong> ${data.edges.length}</p>`;
        displayHTML += '<pre style="font-size: 0.75rem; overflow-y: auto; max-height: 200px;">';
        data.edges.slice(0, 50).forEach(edge => {
            displayHTML += `${edge.source} -- ${edge.target} (${edge.weight.toFixed(2)})\n`;
        });
        if (data.edges.length > 50) {
            displayHTML += `\n... and ${data.edges.length - 50} more edges`;
        }
        displayHTML += '</pre>';
    }

    resultsContent.innerHTML = displayHTML;
}

// UI Helpers
function populateNodeSelectors(nodes) {
    const startSelect = document.getElementById('start-node');
    const endSelect = document.getElementById('end-node');

    startSelect.innerHTML = '<option value="">Select start node...</option>';
    endSelect.innerHTML = '<option value="">Select end node...</option>';

    nodes.forEach(node => {
        const option1 = document.createElement('option');
        option1.value = node.id;
        option1.textContent = `Node ${node.id}`;
        startSelect.appendChild(option1);

        const option2 = document.createElement('option');
        option2.value = node.id;
        option2.textContent = `Node ${node.id}`;
        endSelect.appendChild(option2);
    });
}

function updateButtonStates() {
    const hasGraph = state.graphData !== null;
    const hasStart = state.selectedStartNode !== null;
    const hasEnd = state.selectedEndNode !== null;

    document.getElementById('bfs-btn').disabled = !hasGraph || !hasStart;
    document.getElementById('dfs-btn').disabled = !hasGraph || !hasStart;
    document.getElementById('shortest-path-btn').disabled = !hasGraph || !hasStart || !hasEnd;
    document.getElementById('bipartite-btn').disabled = !hasGraph;
    document.getElementById('save-btn').disabled = !hasGraph;
}

function updateStats(nodeCount, edgeCount) {
    document.getElementById('node-count').textContent = nodeCount;
    document.getElementById('edge-count').textContent = edgeCount;
}

function setStatus(status, type) {
    const statusEl = document.getElementById('status');
    statusEl.textContent = status;
    statusEl.className = 'stat-value status-indicator';

    const colors = {
        ready: 'var(--accent-green)',
        loading: 'var(--accent-yellow)',
        running: 'var(--accent-cyan)',
        complete: 'var(--accent-green)',
        error: 'var(--accent-red)'
    };

    statusEl.style.borderColor = colors[type] || colors.ready;
    statusEl.style.color = colors[type] || colors.ready;
}

function clearMap() {
    // Remove all markers
    Object.values(state.nodeMarkers).forEach(marker => marker.remove());
    state.nodeMarkers = {};

    // Remove all polylines
    state.edgePolylines.forEach(({ polyline }) => polyline.remove());
    state.edgePolylines = [];

    // Reset selections
    state.selectedStartNode = null;
    state.selectedEndNode = null;
    document.getElementById('start-node').value = '';
    document.getElementById('end-node').value = '';

    updateButtonStates();
}

function clearResults() {
    const resultsContent = document.getElementById('results-content');
    resultsContent.innerHTML = `
        <div class="empty-state">
            <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <circle cx="12" cy="12" r="10"></circle>
                <path d="M12 6v6l4 2"></path>
            </svg>
            <p>No results yet. Run an algorithm to see visualizations and details here.</p>
        </div>
    `;

    document.getElementById('path-result').style.display = 'none';
    document.getElementById('bipartite-result').style.display = 'none';
}

function toggleAnimationPause() {
    state.animationPaused = !state.animationPaused;
    const btn = document.getElementById('pause-btn');

    if (state.animationPaused) {
        btn.innerHTML = `
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polygon points="5 3 19 12 5 21 5 3"></polygon>
            </svg>
            Resume Animation
        `;
    } else {
        btn.innerHTML = `
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="6" y="4" width="4" height="16"></rect>
                <rect x="14" y="4" width="4" height="16"></rect>
            </svg>
            Pause Animation
        `;
    }
}

function closeModal() {
    document.getElementById('modal').style.display = 'none';
}

function showLoading(message = 'Loading...') {
    const loadingScreen = document.getElementById('loading-screen');
    loadingScreen.querySelector('p').textContent = message;
    loadingScreen.classList.remove('hidden');
}

function hideLoading() {
    document.getElementById('loading-screen').classList.add('hidden');
}

function showSuccess(message) {
    console.log('✓', message);

    // Create a temporary toast notification
    const toast = document.createElement('div');
    toast.style.cssText = `
        position: fixed;
        bottom: 30px;
        right: 30px;
        background: linear-gradient(135deg, var(--accent-green), #059669);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 0.75rem;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
        z-index: 10001;
        font-size: 0.875rem;
        font-weight: 500;
        animation: slideInUp 0.3s ease;
    `;
    toast.textContent = message;
    document.body.appendChild(toast);

    // Add animation
    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideInUp {
            from { transform: translateY(100px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
    `;
    document.head.appendChild(style);

    // Remove after 3 seconds
    setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transform = 'translateY(50px)';
        toast.style.transition = 'all 0.3s ease';
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

function showError(message) {
    console.error('✗', message);
    alert(message);  // Simple alert for now
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
