"""
================================================================================
HƯỚNG DẪN SỬ DỤNG LỚP GraphAlgorithms
================================================================================

LỚP NÀY LÀ GÌ?
    - Lớp cơ sở tích hợp TẤT CẢ các thuật toán đồ thị
    - Sử dụng ĐA KẾ THỪA (Multiple Inheritance) với Mixin Pattern
    - Mỗi Mixin chứa một nhóm thuật toán liên quan

KIẾN TRÚC MIXIN:
    ┌─────────────────────────────────────┐
    │      GraphAlgorithms (Base)         │
    │  - Quản lý đồ thị NetworkX          │
    │  - Cung cấp interface chung         │
    └─────────────────┬───────────────────┘
                      │
        ┌─────────────┴─────────────┐
        │   Kế thừa từ 7 Mixins     │
        └───────────────────────────┘
                      │
    ┌─────────────────┴─────────────────────┐
    │                                       │
    ├─ TraversalMixin      (BFS, DFS)      │
    ├─ ShortestPathMixin   (Dijkstra)      │  
    ├─ BipartiteMixin      (2-Coloring)    │
    ├─ MSTMixin            (Prim, Kruskal) │
    ├─ FlowMixin           (Ford-Fulkerson)│
    ├─ EulerMixin          (Euler Path)    │
    └─ ConversionMixin     (Format Convert)│

CÁCH SỬ DỤNG:
    1. Tạo đối tượng GraphData (từ frontend hoặc test)
    2. Khởi tạo GraphAlgorithms(graph_data)
    3. Gọi thuật toán: algo.bfs("A"), algo.dijkstra("A", "D")...
    
VÍ DỤ:
    from models import GraphData, Node, Edge
    from algorithms import GraphAlgorithms
    
    # Tạo đồ thị
    graph = GraphData(
        nodes=[Node(id="A"), Node(id="B"), Node(id="C")],
        edges=[Edge(source="A", target="B", weight=1.0)],
        directed=False
    )
    
    # Chạy thuật toán
    algo = GraphAlgorithms(graph)
    result = algo.bfs("A")           # BFS từ A
    result = algo.shortest_path("A", "C")  # Dijkstra
    result = algo.prim_mst()         # MST bằng Prim

LƯU Ý QUAN TRỌNG:
    - GraphData = định dạng của bạn (từ frontend)
    - NetworkX Graph = định dạng thư viện (để chạy thuật toán)
    - _build_networkx_graph() chuyển đổi GraphData → NetworkX
================================================================================
"""
import networkx as nx
from models import GraphData

from .traversal import TraversalMixin
from .shortest_path import ShortestPathMixin
from .bipartite import BipartiteMixin
from .mst import MSTMixin
from .flow import FlowMixin
from .euler import EulerMixin
from .conversion import ConversionMixin


class GraphAlgorithms(
    TraversalMixin,          # Cung cấp: bfs(), dfs()
    ShortestPathMixin,       # Cung cấp: shortest_path()
    BipartiteMixin,          # Cung cấp: check_bipartite()
    MSTMixin,                # Cung cấp: prim_mst(), kruskal_mst()
    FlowMixin,               # Cung cấp: ford_fulkerson()
    EulerMixin,              # Cung cấp: fleury_algorithm(), hierholzer_algorithm()
    ConversionMixin          # Cung cấp: convert_representation()
):
    """
    Triển khai các thuật toán đồ thị với theo dõi từng bước
    
    Sử dụng đa kế thừa để tổ chức thuật toán theo danh mục.
    Mỗi mixin cung cấp các triển khai thuật toán cụ thể.
    """
    
    def __init__(self, graph_data: GraphData):
        """Khởi tạo với dữ liệu đồ thị
        
        Tham số:
            graph_data: Đối tượng GraphData chứa nodes và edges
        
        Thuộc tính được tạo:
            self.graph_data: Lưu trữ dữ liệu gốc
            self.G: Đồ thị NetworkX để chạy thuật toán
        """
        # TODO: Triển khai khởi tạo
        pass
    
    def _build_networkx_graph(self) -> nx.Graph:
        """Chuyển đổi GraphData sang đồ thị NetworkX
        
        CÁCH HOẠT ĐỘNG:
            1. Kiểm tra đồ thị có hướng hay vô hướng
            2. Tạo nx.DiGraph() hoặc nx.Graph()
            3. Thêm tất cả đỉnh với thuộc tính (lat, lon, label)
            4. Thêm tất cả cạnh với trọng số
        
        Trả về:
            nx.Graph hoặc nx.DiGraph
        """
        # TODO: Triển khai chuyển đổi đồ thị
        pass
