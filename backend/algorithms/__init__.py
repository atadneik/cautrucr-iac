"""
===============================================================================
FILE: __init__.py
MÔ TẢ: Package Initialization - Export public API của algorithms
===============================================================================

CHỨC NĂNG:
    - Định nghĩa public API của package algorithms
    - Export GraphAlgorithms class (class chính)
    - Export UnionFind class (dùng cho Kruskal)
    - Giấu implementation details (các mixin)

CẤU TRÚC PACKAGE:
    algorithms/
    ├── __init__.py          ← File này
    ├── base.py              → GraphAlgorithms (kết hợp tất cả mixins)
    ├── traversal.py         → TraversalMixin (BFS, DFS)
    ├── shortest_path.py     → ShortestPathMixin (Dijkstra)
    ├── bipartite.py         → BipartiteMixin
    ├── mst.py               → MSTMixin, UnionFind
    ├── flow.py              → FlowMixin
    ├── euler.py             → EulerMixin
    └── conversion.py        → ConversionMixin

CÁCH SỬ DỤNG:
    from algorithms import GraphAlgorithms, UnionFind
    
    # Tạo instance
    algo = GraphAlgorithms(graph_data)
    
    # Gọi bất kỳ thuật toán nào
    result = algo.bfs(start_node)
    result = algo.prim_mst()
    result = algo.ford_fulkerson(source, sink)

EXPORT:
    - GraphAlgorithms: Class chính với tất cả thuật toán
    - UnionFind: Cấu trúc dữ liệu cho Kruskal

KHÔNG EXPORT (internal):
    - Các Mixin classes (TraversalMixin, MSTMixin, etc.)
    - Implementation details

THÀNH VIÊN PHỤ TRÁCH: Tất cả members (shared package)
===============================================================================
"""

from .base import GraphAlgorithms
from .mst import UnionFind

__all__ = ['GraphAlgorithms', 'UnionFind']
