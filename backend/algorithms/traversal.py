"""
FILE: traversal.py
MÔ TẢ: Thuật toán duyệt đồ thị BFS và DFS

CHỨC NĂNG:
    - Breadth-First Search (BFS): Duyệt đồ thị theo chiều rộng
    - Depth-First Search (DFS): Duyệt đồ thị theo chiều sâu
    
CÁCH HOẠT ĐỘNG:
    BFS:
        1. Bắt đầu từ đỉnh nguồn, thêm vào hàng đợi
        2. Lấy đỉnh đầu hàng đợi, đánh dấu đã thăm
        3. Thêm tất cả đỉnh kề chưa thăm vào hàng đợi
        4. Lặp lại cho đến khi hàng đợi rỗng
        => Đảm bảo thăm các đỉnh theo thứ tự khoảng cách tăng dần
    
    DFS:
        1. Bắt đầu từ đỉnh nguồn, thêm vào ngăn xếp
        2. Lấy đỉnh đầu ngăn xếp, đánh dấu đã thăm
        3. Thêm tất cả đỉnh kề chưa thăm vào ngăn xếp
        4. Lặp lại cho đến khi ngăn xếp rỗng
        => Đi sâu vào một nhánh trước khi quay lui

ĐẦU VÀO:
    - start_node (str): ID của đỉnh bắt đầu duyệt
    - self.G (NetworkX Graph): Đồ thị cần duyệt

ĐẦU RA:
    - AlgorithmResponse chứa:
        + success: True/False
        + steps: Danh sách các bước thực thi (để visualization)
        + result: Thứ tự duyệt và số đỉnh đã thăm
"""
from collections import deque
from models import AlgorithmResponse, AlgorithmStep


class TraversalMixin:
    """Mixin cung cấp các thuật toán duyệt đồ thị"""
    
    def bfs(self, start_node: str) -> AlgorithmResponse:
        """
        Tìm kiếm theo chiều rộng với theo dõi từng bước thực thi
        
        Tham số:
            start_node: ID đỉnh bắt đầu
            
        Trả về:
            AlgorithmResponse với các bước thực thi
        """
        # TODO: Triển khai thuật toán BFS
        pass
    
    def dfs(self, start_node: str) -> AlgorithmResponse:
        """
        Tìm kiếm theo chiều sâu với theo dõi từng bước thực thi
        
        Tham số:
            start_node: ID đỉnh bắt đầu
            
        Trả về:
            AlgorithmResponse với các bước thực thi
        """
        # TODO: Triển khai thuật toán DFS
        pass
