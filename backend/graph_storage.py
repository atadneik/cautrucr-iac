"""
FILE: graph_storage.py
MÔ TẢ: Quản Lý Lưu Trữ Đồ Thị - Save/Load graphs to/from files

CHỨC NĂNG:
    - Lưu đồ thị vào file JSON
    - Tải đồ thị từ file đã lưu
    - Liệt kê tất cả đồ thị đã lưu
    - Tự động tạo thư mục lưu trữ

CÁCH HOẠT ĐỘNG:
    Lưu đồ thị:
        1. Nhận GraphData từ API
        2. Serialize thành JSON (dùng model_dump())
        3. Lưu vào file: saved_graphs/<name>.json
        4. Trả về đường dẫn file

    Tải đồ thị:
        1. Nhận tên file từ API
        2. Đọc file JSON từ saved_graphs/
        3. Parse JSON → GraphData object
        4. Trả về đồ thị đã tải

    Liệt kê đồ thị:
        1. Scan thư mục saved_graphs/
        2. Lọc các file .json
        3. Trả về danh sách tên file

THƯ MỤC LƯU TRỮ:
    - Đường dẫn: backend/saved_graphs/
    - Format: <name>.json
    - Auto-create nếu chưa tồn tại
"""
import json
import os
from pathlib import Path
from datetime import datetime
from typing import List
from models import GraphData, SaveGraphResponse, LoadGraphResponse

# Thư mục lưu trữ đồ thị
SAVE_DIR = "saved_graphs"

class GraphStorage:
    """Xử lý lưu và tải đồ thị"""
    
    def __init__(self):
        """Tạo thư mục lưu trữ nếu chưa tồn tại"""
        # TODO: Triển khai khởi tạo
        pass
    
    def save_graph(self, name: str, graph_data: GraphData) -> SaveGraphResponse:
        """
        Lưu đồ thị vào file
        
        Tham số:
            name: Tên cho đồ thị được lưu
            graph_data: Dữ liệu đồ thị cần lưu
            
        Trả về:
            SaveGraphResponse với trạng thái thành công
        """
        # TODO: Triển khai lưu đồ thị
        pass
    
    def load_graph(self, filename: str) -> LoadGraphResponse:
        """
        Tải đồ thị từ file
        
        Tham số:
            filename: Tên file của đồ thị đã lưu
            
        Trả về:
            LoadGraphResponse với dữ liệu đồ thị
        """
        # TODO: Triển khai tải đồ thị
        pass
    
    def list_saved_graphs(self) -> List[dict]:
        """
        Liệt kê tất cả các đồ thị đã lưu
        
        Trả về:
            Danh sách metadata của các đồ thị đã lưu
        """
        # TODO: Triển khai liệt kê đồ thị
        pass

# Singleton instance
graph_storage = GraphStorage()
