"""
FILE: shortest_path.py  
MÔ TẢ: Thuật toán Tìm Đường Đi Ngắn Nhất (Dijkstra)

CHỨC NĂNG:
    - Dijkstra: Tìm đường đi ngắn nhất từ một đỉnh đến tất cả các đỉnh khác

CÁCH HOẠT ĐỘNG:
    1. Khởi tạo khoảng cách = ∞ cho tất cả đỉnh (trừ đỉnh nguồn = 0)
    2. Dùng priority queue để chọn đỉnh có khoảng cách nhỏ nhất
    3. Với mỗi đỉnh được chọn, cập nhật khoảng cách đến các đỉnh kề
    4. Lặp lại cho đến khi tìm thấy đích hoặc hết đỉnh
    5. Truy vết ngược để tìm đường đi
    => Độ phức tạp: O((V + E) log V)

ĐẦU VÀO:
    - start_node: Đỉnh bắt đầu
    - end_node: Đỉnh đích
    - self.G: Đồ thị có trọng số (phải >= 0)

ĐẦU RA:
    - AlgorithmResponse chứa:
        + path: Danh sách đỉnh trong đường đi
        + distance: Khoảng cách tổng
        + steps: Các bước thực thi

ĐIỀU KIỆN:
    - Trọng số các cạnh phải >= 0
    - Nếu có trọng số âm, dùng Bellman-Ford
"""
import heapq
from models import AlgorithmResponse, AlgorithmStep


class ShortestPathMixin:
    """Mixin cung cấp thuật toán tìm đường đi ngắn nhất"""
    
    def shortest_path(self, start_node: str, end_node: str) -> AlgorithmResponse:
        """
        Tìm đường đi ngắn nhất sử dụng thuật toán Dijkstra với theo dõi từng bước
        
        Tham số:
            start_node: ID đỉnh bắt đầu
            end_node: ID đỉnh đích
            
        Trả về:
            AlgorithmResponse với các bước thực thi
        """
        # TODO: Triển khai thuật toán Dijkstra
        pass
