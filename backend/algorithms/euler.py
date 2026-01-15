"""
FILE: euler.py
MÔ TẢ: Thuật toán Đường Đi và Chu Trình Euler

CHỨC NĂNG:
    - Fleury: Tìm đường đi/chu trình Euler (tránh cầu)
    - Hierholzer: Tìm chu trình Euler (dùng ngăn xếp)

ĐIỀU KIỆN EULER:
    Đồ thị vô hướng:
        - Chu trình: TẤT CẢ đỉnh có bậc chẵn
        - Đường đi: ĐÚNG 2 đỉnh có bậc lẻ
    Đồ thị có hướng:
        - Chu trình: Mọi đỉnh có in-degree = out-degree

CÁCH HOẠT ĐỘNG:
    Fleury:
        1. Kiểm tra điều kiện Euler
        2. Chọn cạnh KHÔNG phải cầu (nếu có thể)
        3. Đi qua cạnh và xóa cạnh đó
        4. Lặp lại cho đến hết cạnh
        => O(E²) - Phải kiểm tra cầu
    
    Hierholzer:
        1. Duyệt theo cạnh bất kỳ, đẩy vào ngăn xếp
        2. Gặp đỉnh bế tắc → pop và thêm vào kết quả
        3. Lặp lại cho đến hết
        => O(E) - Nhanh hơn Fleury
"""
import networkx as nx
from typing import Dict, Any, Optional
from models import AlgorithmStep


class EulerMixin:
    """Mixin cung cấp các thuật toán đường đi/chu trình Euler"""
    
    def fleury_algorithm(self, start_node: Optional[str] = None) -> Dict[str, Any]:
        """
        Thuật toán Fleury để tìm đường đi/chu trình Euler
        
        Tham số:
            start_node: Đỉnh bắt đầu (tùy chọn)
            
        Trả về:
            Dictionary với đường đi Euler và các bước
        """
        # TODO: Triển khai thuật toán Fleury
        pass
    
    def hierholzer_algorithm(self, start_node: Optional[str] = None) -> Dict[str, Any]:
        """
        Thuật toán Hierholzer để tìm chu trình Euler
        
        Tham số:
            start_node: Đỉnh bắt đầu (tùy chọn)
            
        Trả về:
            Dictionary với chu trình Euler và các bước
        """
        # TODO: Triển khai thuật toán Hierholzer
        pass
