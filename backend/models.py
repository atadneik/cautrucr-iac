"""
FILE: models.py
MÔ TẢ: Pydantic Data Models - Cấu trúc dữ liệu cho toàn bộ hệ thống

CHỨC NĂNG:
    - Định nghĩa tất cả data models cho API
    - Validation tự động với Pydantic
    - Type hints đầy đủ cho IDE support
    - Serialization/Deserialization JSON

CÁC MODELS CHÍNH:

    1. Cấu trúc đồ thị:
        - Node: Đỉnh đồ thị (id, lat, lon, label)
        - Edge: Cạnh đồ thị (source, target, weight, capacity, directed)
        - GraphData: Đồ thị hoàn chỉnh (nodes, edges, directed, graph_type)
        - GraphType: Enum (UNDIRECTED, DIRECTED, FLOW)
    
    2. Thực thi thuật toán:
        - AlgorithmRequest: Request chung cho các thuật toán
        - AlgorithmStep: Một bước trong quá trình thực thi
        - AlgorithmResponse: Kết quả thuật toán với steps
    
    3. Thuật toán nâng cao:
        - MSTRequest/MSTResponse: Prim & Kruskal
        - MaxFlowRequest/MaxFlowResponse: Ford-Fulkerson
        - EulerianRequest/EulerianResponse: Fleury & Hierholzer
    
    4. Thao tác đồ thị:
        - AddEdgeRequest: Thêm cạnh thủ công
        - DeleteNodeRequest: Xóa đỉnh
        - DeleteEdgeRequest: Xóa cạnh
    
    5. Lưu trữ:
        - SaveGraphRequest: Lưu đồ thị
        - SaveGraphResponse: Kết quả lưu
        - LoadGraphResponse: Kết quả tải
    
    6. Chuyển đổi:
        - ConversionRequest: Chuyển đổi biểu diễn
        - ConversionResponse: Kết quả chuyển đổi
"""
from pydantic import BaseModel
from typing import List, Dict, Any, Optional, Literal
from enum import Enum

class GraphType(str, Enum):
    """Các loại đồ thị được hỗ trợ"""
    UNDIRECTED = "undirected"
    DIRECTED = "directed"
    FLOW = "flow"

class Node(BaseModel):
    """Biểu diễn đỉnh trong đồ thị"""
    id: str
    lat: float
    lon: float
    label: Optional[str] = None

class Edge(BaseModel):
    """Biểu diễn cạnh trong đồ thị"""
    source: str
    target: str
    weight: float = 1.0
    directed: bool = False
    capacity: Optional[float] = None  # Cho mạng luồng

class FlowEdge(BaseModel):
    """Cạnh có thông tin luồng cho mạng luồng"""
    source: str
    target: str
    flow: float
    capacity: float

class GraphData(BaseModel):
    """Cấu trúc đồ thị hoàn chỉnh"""
    nodes: List[Node]
    edges: List[Edge]
    directed: bool = False
    graph_type: GraphType = GraphType.UNDIRECTED
    metadata: Optional[Dict[str, Any]] = None

class AlgorithmRequest(BaseModel):
    """Request để thực thi thuật toán"""
    graph: GraphData
    algorithm: Literal["bfs", "dfs", "shortest_path", "bipartite"]
    start_node: Optional[str] = None
    end_node: Optional[str] = None

class MSTRequest(BaseModel):
    """Request cho thuật toán MST (Prim, Kruskal)"""
    graph: GraphData
    algorithm: Literal["prim", "kruskal"]
    start_node: Optional[str] = None  # Cho thuật toán Prim

class MSTResponse(BaseModel):
    """Response từ thuật toán MST"""
    success: bool
    algorithm: str
    steps: List["AlgorithmStep"]
    mst_edges: List[Dict[str, Any]]
    total_weight: float
    error: Optional[str] = None

class MaxFlowRequest(BaseModel):
    """Request cho thuật toán luồng cực đại (Ford-Fulkerson)"""
    graph: GraphData
    source_node: str
    sink_node: str

class MaxFlowResponse(BaseModel):
    """Response từ thuật toán luồng cực đại"""
    success: bool
    algorithm: str
    steps: List["AlgorithmStep"]
    max_flow: float
    flow_edges: List[FlowEdge]
    error: Optional[str] = None

class EulerianRequest(BaseModel):
    """Request cho thuật toán đường đi/chu trình Euler (Fleury, Hierholzer)"""
    graph: GraphData
    algorithm: Literal["fleury", "hierholzer"]
    start_node: Optional[str] = None

class EulerianResponse(BaseModel):
    """Response từ thuật toán Euler"""
    success: bool
    algorithm: str
    steps: List["AlgorithmStep"]
    has_eulerian_path: bool
    has_eulerian_circuit: bool
    path: Optional[List[str]] = None
    path_type: Optional[str] = None  # "circuit", "path", hoặc "none"
    error: Optional[str] = None

class ConversionRequest(BaseModel):
    """Request để chuyển đổi biểu diễn đồ thị"""
    graph: GraphData
    from_format: Literal["adjacency_matrix", "adjacency_list", "edge_list"]
    to_format: Literal["adjacency_matrix", "adjacency_list", "edge_list"]

class AlgorithmStep(BaseModel):
    """Một bước trong quá trình thực thi thuật toán"""
    step: int
    action: str
    node: Optional[str] = None
    edge: Optional[Dict[str, str]] = None
    visited: List[str] = []
    queue: List[str] = []
    stack: List[str] = []
    distance: Optional[Dict[str, float]] = None
    parent: Optional[Dict[str, Optional[str]]] = None
    mst_edges: Optional[List[Dict[str, Any]]] = None  # Cho thuật toán MST
    current_flow: Optional[Dict[str, float]] = None  # Cho thuật toán luồng
    sets: Optional[Dict[str, Any]] = None  # Cho union-find trong Kruskal
    description: str

class AlgorithmResponse(BaseModel):
    """Response từ quá trình thực thi thuật toán"""
    success: bool
    algorithm: str
    steps: List[AlgorithmStep]
    result: Any
    error: Optional[str] = None

class ConversionResponse(BaseModel):
    """Response từ chuyển đổi biểu diễn"""
    success: bool
    from_format: str
    to_format: str
    data: Any
    error: Optional[str] = None

class SaveGraphRequest(BaseModel):
    """Request để lưu đồ thị"""
    name: str
    graph: GraphData

class SaveGraphResponse(BaseModel):
    """Response từ thao tác lưu"""
    success: bool
    filename: str
    error: Optional[str] = None

class LoadGraphResponse(BaseModel):
    """Response từ thao tác tải"""
    success: bool
    graph: Optional[GraphData] = None
    error: Optional[str] = None

class AddEdgeRequest(BaseModel):
    """Request để thêm cạnh thủ công"""
    graph: GraphData
    source: str
    target: str
    weight: float = 1.0
    capacity: Optional[float] = None
    directed: Optional[bool] = None  # Nếu None, dùng mặc định của đồ thị

class DeleteNodeRequest(BaseModel):
    """Request để xóa đỉnh"""
    graph: GraphData
    node_id: str

class DeleteEdgeRequest(BaseModel):
    """Request để xóa cạnh"""
    graph: GraphData
    source: str
    target: str
