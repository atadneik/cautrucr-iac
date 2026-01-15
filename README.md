# Graph Visualization Application - Bình Thạnh District

A comprehensive web application for visualizing and analyzing graphs using real-time map data from Bình Thạnh district, TP.HCM. Features interactive graph manipulation, multiple algorithms (BFS, DFS, shortest path, bipartite checking), and graph representation conversions.

## ✨ Features

### Core Features
- 🗺️ **Real-time Map Integration**: OpenStreetMap data from Bình Thạnh district
- 🎨 **Interactive Visualization**: Click and explore graph nodes and edges on the map
- 📊 **Graph Algorithms**:
  - Breadth-First Search (BFS)
  - Depth-First Search (DFS)
  - Dijkstra's Shortest Path
  - Bipartite Graph Check
- 🔄 **Graph Representations**: Adjacency Matrix, Adjacency List, Edge List
- 💾 **Save/Load**: Persist graphs for later analysis
- ⚡ **Live Animation**: Step-by-step algorithm execution visualization

### UI Features
- 🌙 Modern dark theme with glassmorphism effects
- 🎯 Premium design with vibrant gradients
- 📱 Responsive layout
- ⚙️ Adjustable animation speed
- 🎬 Pause/resume animations

## 🏗️ Technology Stack

### Backend
- **FastAPI**: Modern Python web framework
- **NetworkX**: Graph algorithms library
- **Requests**: OpenStreetMap API integration
- **Pydantic**: Data validation

### Frontend
- **Vanilla JavaScript**: No framework dependencies
- **Leaflet.js**: Interactive map visualization
- **CSS3**: Modern styling with custom properties
- **HTML5**: Semantic markup

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project directory**
```bash
cd /home/dangkien/ctrr
```

2. **Install backend dependencies**
```bash
cd backend
pip install -r requirements.txt
```

### Running the Application

1. **Start the backend server**
```bash
cd backend
python main.py
```

The server will start on `http://localhost:8000`

2. **Access the application**

Open your web browser and navigate to:
```
http://localhost:8000
```

The frontend will be automatically served by FastAPI.

## 📖 Usage Guide

### 1. Load Map Data
- Click the **"Load Map"** button to fetch road network data from Bình Thạnh district
- The map will display intersections as nodes and roads as edges

### 2. Select Nodes
- Click on nodes directly on the map, or
- Use the dropdown selectors in the control panel
- First click selects the **start node** (orange)
- Second click selects the **end node** (green)

### 3. Run Algorithms

#### BFS/DFS Traversal
1. Select a start node
2. Click **"BFS Traversal"** or **"DFS Traversal"**
3. Watch the animated visualization
4. View results in the bottom panel

#### Shortest Path
1. Select both start and end nodes
2. Click **"Find Shortest Path"**
3. The shortest route will be highlighted in green
4. Distance is displayed in meters

#### Bipartite Check
1. Load a graph
2. Click **"Check Bipartite"**
3. The algorithm will attempt two-coloring
4. Results show if the graph is bipartite

### 4. Graph Representations
1. Select a format from the dropdown (Adjacency Matrix, List, or Edge List)
2. Click **"Convert & Display"**
3. View the representation in the results panel

### 5. Save/Load Graphs
- **Save**: Enter a name and click "Save" to persist the current graph
- **Load**: Click "Load" to view and restore previously saved graphs

### 6. Animation Controls
- Adjust animation speed with the slider (100ms - 2000ms)
- Click "Pause Animation" during execution to pause/resume

## 🎯 API Endpoints

All endpoints are accessible at `http://localhost:8000/api`

- `GET /api/map-data` - Fetch OpenStreetMap data
- `POST /api/bfs` - Run BFS algorithm
- `POST /api/dfs` - Run DFS algorithm
- `POST /api/shortest-path` - Find shortest path
- `POST /api/check-bipartite` - Check if graph is bipartite
- `POST /api/convert-representation` - Convert graph format
- `POST /api/save-graph` - Save a graph
- `GET /api/load-graph/{filename}` - Load a saved graph
- `GET /api/saved-graphs` - List all saved graphs

Full API documentation available at: `http://localhost:8000/docs`

## 📁 Project Structure

```
ctrr/
├── backend/
│   ├── main.py                 # FastAPI application
│   ├── models.py               # Pydantic data models
│   ├── map_data.py            # OpenStreetMap integration
│   ├── graph_algorithms.py    # Algorithm implementations
│   ├── graph_storage.py       # Save/load functionality
│   ├── requirements.txt       # Python dependencies
│   └── saved_graphs/          # Saved graph files
│
└── frontend/
    ├── index.html             # Main HTML page
    ├── style.css              # Premium UI styling
    └── app.js                 # Application logic
```

## 🔧 Configuration

### Map Area
To change the map area, edit `BINH_THANH_BBOX` in `backend/map_data.py`:
```python
BINH_THANH_BBOX = {
    "south": 10.7900,
    "west": 106.6850,
    "north": 10.8300,
    "east": 106.7250
}
```

### Graph Complexity
By default, only major roads are fetched. To include all roads:
```python
# In backend/map_data.py, change major_roads_only parameter
graph_data = osm_fetcher.fetch_binh_thanh_roads(major_roads_only=False)
```

## 🐛 Troubleshooting

### Map not loading
- Check internet connection (OpenStreetMap tiles require network access)
- Verify the backend server is running on port 8000
- Check browser console for CORS errors

### Algorithm errors
- Ensure map data is loaded before running algorithms
- Verify start/end nodes are selected
- Check the results panel for error messages

### Performance issues
- Reduce animation speed for large graphs
- Use `major_roads_only=True` to limit graph size
- Close other browser tabs to free memory

## 🤝 Contributing

This project was built as a graph visualization tool for educational purposes. Feel free to:
- Add new algorithms
- Improve visualization
- Enhance UI/UX
- Add more map data sources

## 📄 License

MIT License - Feel free to use and modify as needed.

## 🙏 Acknowledgments

- **OpenStreetMap** contributors for map data
- **Leaflet.js** for map visualization
- **FastAPI** for the excellent web framework
- **NetworkX** for graph algorithms

---

**Made with ❤️ for graph visualization and algorithm learning**
# cautrucr-iac
