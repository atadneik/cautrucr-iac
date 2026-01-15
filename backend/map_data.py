"""
FILE: map_data.py
MÔ TẢ: Tích Hợp OpenStreetMap - Tải dữ liệu bản đồ thành đồ thị

CHỨC NĂNG:
    - Tải dữ liệu đường phố từ OpenStreetMap API (Overpass)
    - Chuyển đổi dữ liệu OSM thành đồ thị
    - Lọc theo khu vực Bình Thạnh, TP.HCM
    - Fallback sang sample data nếu OSM API fail

CÁCH HOẠT ĐỘNG:
    1. Gửi Overpass query đến OSM API
    2. Lọc các đường: Điện Biên Phủ, Võ Oanh, Xô Viết Nghệ Tĩnh, etc.
    3. Parse kết quả:
        - Ways (đường) → tìm giao điểm
        - Nodes (điểm) → đỉnh đồ thị
    4. Tạo GraphData với nodes và edges
    5. Nếu fail → dùng sample graph (16 nodes)

SAMPLE GRAPH:
    - 16 nodes tại các giao điểm đường chính
    - 24 edges nối các giao điểm
    - Khu vực: 8 đường lớn ở Bình Thạnh
"""
import requests
import json
from typing import Dict, List, Tuple
from models import GraphData, Node, Edge
import time

# Khu vực trung tâm tọa độ đã chỉ định
BINH_THANH_WARDS = [51, 54, 56, 58, 61, 66, 67, 69, 71]

# Bounding box tại Lat: 10.803451, Lon: 106.719046 (±500m)
BINH_THANH_BBOX = {
    "south": 10.7985,
    "west": 106.7140,
    "north": 10.8085,
    "east": 106.7240
}

class OSMDataFetcher:
    """Lấy và parse dữ liệu OpenStreetMap cho khu vực Quận 1"""
    
    def __init__(self):
        """Khởi tạo OSM fetcher"""
        # TODO: Triển khai khởi tạo
        pass
        
    def fetch_binh_thanh_roads(self, major_roads_only: bool = True) -> GraphData:
        """
        Lấy mạng đường thực tế từ khu vực Thành Mỹ Tây sử dụng OSM
        Fallback sang sample data nếu API fail
        
        Tham số:
            major_roads_only: Nếu True, chỉ lấy các đường chính
            
        Trả về:
            GraphData với các nút giao lộ thực tế và đoạn đường
        """
        # TODO: Triển khai lấy dữ liệu OSM
        pass
    
    def _parse_osm_to_graph(self, osm_data: Dict) -> GraphData:
        """
        Chuyển đổi dữ liệu OSM sang định dạng GraphData
        
        Ways của OSM biểu diễn đường, và nodes biểu diễn điểm trên đường.
        Tạo các nút đồ thị tại giao lộ và điểm cuối đường.
        """
        # TODO: Triển khai parse OSM
        pass
    
    def _calculate_distance(self, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """
        Tính khoảng cách giữa hai tọa độ theo mét (công thức Haversine)
        """
        # TODO: Triển khai tính khoảng cách Haversine
        pass
    
    def _create_sample_graph(self) -> GraphData:
        """
        Đồ thị mẫu với các nút tại giao lộ của các đường đã chỉ định
        Đường: Ung Văn Khiêm, Võ Oanh, Xô Viết Nghệ Tĩnh, 
               Nguyễn Gia Trí, Tân Cảng, Nguyễn Văn Thương, Điện Biên Phủ, D5
        """
        # TODO: Triển khai tạo đồ thị mẫu
        pass

# Singleton instance
osm_fetcher = OSMDataFetcher()
