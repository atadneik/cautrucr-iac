"""
FILE: mst.py
MÔ TẢ: Thuật toán Cây Khung Nhỏ Nhất (Minimum Spanning Tree)

CHỨC NĂNG:
    - Prim: Xây dựng MST bằng cách mở rộng từ một đỉnh
    - Kruskal: Xây dựng MST bằng cách sắp xếp cạnh theo trọng số
    - UnionFind: Cấu trúc dữ liệu hỗ trợ Kruskal

CÁCH HOẠT ĐỘNG:
    Prim:
        1. Bắt đầu từ một đỉnh bất kỳ, thêm vào cây
        2. Dùng priority queue lưu các cạnh kề
        3. Chọn cạnh nhỏ nhất nối đến đỉnh chưa trong cây
        4. Thêm đỉnh mới và cạnh vào cây
        5. Lặp lại cho đến khi có n-1 cạnh
        => Độ phức tạp: O(E log V)
    
    Kruskal:
        1. Sắp xếp tất cả cạnh theo trọng số tăng dần
        2. Duyệt từng cạnh, kiểm tra có tạo chu trình không (UnionFind)
        3. Nếu không tạo chu trình → thêm cạnh vào MST
        4. Dừng khi có n-1 cạnh
        => Độ phức tạp: O(E log E)
    
    UnionFind:
        - find(x): Tìm đại diện của tập chứa x (path compression)
        - union(x,y): Hợp 2 tập chứa x và y (union by rank)
        - Độ phức tạp: gần O(1) cho mỗi thao tác

ĐẦU VÀO:
    - graph_data: Đồ thị vô hướng, có trọng số
    - start_node (optional): Đỉnh bắt đầu cho Prim

ĐẦU RA:
    - Dictionary chứa:
        + mst_edges: Danh sách cạnh trong MST
        + total_weight: Tổng trọng số của MST
        + steps: Các bước thực thi

ĐIỀU KIỆN:
    - Đồ thị phải VÔ HƯỚNG
    - Đồ thị phải LIÊN THÔNG
"""
import heapq
from typing import Dict, Any, Optional
from models import AlgorithmStep


class UnionFind:
    """Cấu trúc dữ liệu Union-Find (Disjoint Set Union) cho thuật toán Kruskal"""
    
    def __init__(self, nodes):
        """Khởi tạo Union-Find với danh sách nodes"""
        # TODO: Triển khai khởi tạo
        pass
    
    def find(self, node):
        """Tìm gốc (root) của tập chứa node - với path compression
        
        Path Compression: Nén đường đi khi tìm root
        - Mọi lần gọi find(), cập nhật parent trực tiếp trỏ về root
        - Làm phẳng cây → Tăng tốc thao tác tiếp theo
        - Độ phức tạp: gần O(1) amortized
        """
        # TODO: Triển khai find với path compression
        pass
    
    def union(self, node1, node2):
        """Hợp hai tập chứa node1 và node2 - với union by rank
        
        Union by Rank: Nối cây thấp vào cây cao
        - rank = độ sâu tối đa của cây (xấp xỉ)
        - Luôn nối cây nhỏ hơn vào cây lớn hơn → tránh cây quá cao
        - Giữ cây cân bằng → thao tác nhanh hơn
        """
        # TODO: Triển khai union với rank
        pass
    
    def count_sets(self):
        """Đếm số lượng tập hợp rời rạc"""
        # TODO: Triển khai đếm tập hợp
        pass


class MSTMixin:
    """Mixin cung cấp các thuật toán Cây Khung Nhỏ Nhất"""
    
    def prim_mst(self, start_node: Optional[str] = None) -> Dict[str, Any]:
        """
        Thuật toán Prim cho Cây Khung Nhỏ Nhất với theo dõi từng bước
        
        Tham số:
            start_node: Đỉnh bắt đầu (tùy chọn, dùng đỉnh đầu tiên nếu None)
            
        Trả về:
            Dictionary với MST edges, tổng trọng số, và các bước
        """
        # TODO: Triển khai thuật toán Prim
        pass

    def kruskal_mst(self) -> Dict[str, Any]:
        """
        Thuật toán Kruskal cho Cây Khung Nhỏ Nhất với theo dõi từng bước
        Sử dụng cấu trúc dữ liệu Union-Find
        
        Trả về:
            Dictionary với MST edges, tổng trọng số, và các bước
        """
        # TODO: Triển khai thuật toán Kruskal
        pass
