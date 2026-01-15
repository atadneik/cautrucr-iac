"""
FILE: bipartite.py
MÔ TẢ: Thuật toán Kiểm Tra Đồ Thị Hai Phần (Bipartite Graph)

CHỨC NĂNG:
    - Kiểm tra xem đồ thị có phải là đồ thị hai phần không
    - Sử dụng thuật toán tô màu hai màu (two-coloring)

CÁCH HOẠT ĐỘNG:
    1. Chọn một đỉnh bất kỳ, tô màu 0
    2. Dùng BFS để tô màu các đỉnh kề bằng màu đối lập (0↔1)
    3. Nếu gặp đỉnh kề cùng màu → KHÔNG phải đồ thị hai phần
    4. Nếu tô hết không xung đột → LÀ đồ thị hai phần
    5. Lặp lại cho tất cả thành phần liên thông
    => Độ phức tạp: O(V + E)

ĐẦU VÀO:
    - self.G: Đồ thị VÔ HƯỚNG cần kiểm tra

ĐẦU RA:
    - AlgorithmResponse chứa:
        + is_bipartite: True/False
        + set_a, set_b: Hai tập đỉnh (nếu là bipartite)
        + coloring: Màu của từng đỉnh
        + steps: Các bước tô màu

ĐIỀU KIỆN:
    - Đồ thị phải VÔ HƯỚNG
    - Có hướng thì không áp dụng được
"""
from collections import deque
from models import AlgorithmResponse, AlgorithmStep


class BipartiteMixin:
    """Mixin cung cấp kiểm tra đồ thị hai phần"""
    
    def check_bipartite(self) -> AlgorithmResponse:
        """
        Kiểm tra đồ thị có phải bipartite sử dụng thuật toán tô màu hai màu
        
        Trả về:
      AlgorithmResponse với các bước thực thi
        """
        # TODO: Triển khai thuật toán kiểm tra bipartite
        pass
