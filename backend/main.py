"""
FILE: main.py
MÔ TẢ: Backend API Server - FastAPI Application

CHỨC NĂNG:
    - API Server chính cho ứng dụng trực quan hóa đồ thị
    - Cung cấp 13 RESTful endpoints
    - Tích hợp OpenStreetMap để tải dữ liệu bản đồ
    - Xử lý các thuật toán đồ thị (BFS, DFS, Dijkstra, MST, Flow, Euler)
    - Lưu/tải đồ thị từ file
    - Phục vụ frontend static files

CÁC ENDPOINTS:

    1. Tải Bản Đồ:
        GET /api/map-data
        → Tải dữ liệu đồ thị từ OpenStreetMap
    
    2. Thuật Toán Cơ Bản (4 endpoints):
        POST /api/bfs                    # Breadth-First Search
        POST /api/dfs                    # Depth-First Search
        POST /api/shortest-path          # Dijkstra
        POST /api/check-bipartite        # Kiểm tra đồ thị 2 phần
    
    3. Thuật Toán Nâng Cao (5 endpoints):
        POST /api/prim                   # Prim's MST
        POST /api/kruskal                # Kruskal's MST
        POST /api/ford-fulkerson         # Max Flow
        POST /api/fleury                 # Đường đi Euler (Fleury)
        POST /api/hierholzer             # Chu trình Euler (Hierholzer)
    
    4. Chỉnh Sửa Đồ Thị (3 endpoints):
        POST /api/add-edge               # Thêm cạnh thủ công
        POST /api/delete-node            # Xóa đỉnh
        POST /api/delete-edge            # Xóa cạnh
    
    5. Lưu Trữ (4 endpoints):
        POST /api/save-graph             # Lưu đồ thị vào file
        GET  /api/load-graph/{name}      # Tải đồ thị đã lưu
        GET  /api/saved-graphs           # Liệt kê đồ thị đã lưu
        POST /api/convert-representation # Chuyển đổi biểu diễn
"""
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from typing import List, Optional
import os
import uvicorn

from models import (
    AlgorithmRequest, ConversionRequest, SaveGraphRequest,
    AlgorithmResponse, ConversionResponse, SaveGraphResponse, LoadGraphResponse,
    MSTRequest, MSTResponse, MaxFlowRequest, MaxFlowResponse,
    EulerianRequest, EulerianResponse, AddEdgeRequest, 
    DeleteNodeRequest, DeleteEdgeRequest, GraphData, Edge
)
from map_data import osm_fetcher
from algorithms import GraphAlgorithms
from graph_storage import graph_storage

app = FastAPI(
    title="Graph Visualization API",
    description="API for graph algorithms with OSM data from Bình Thạnh wards",
    version="2.0.0"
)

# Cấu hình CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Trong production, chỉ định origins cụ thể
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Phục vụ frontend static files
frontend_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")
if os.path.exists(frontend_path):
    app.mount("/static", StaticFiles(directory=frontend_path, html=True), name="static")

@app.get("/")
async def root():
    """Phục vụ trang HTML chính"""
    # TODO: Triển khai serve index.html
    pass

@app.get("/style.css")
async def get_css():
    """Phục vụ file CSS"""
    # TODO: Triển khai serve CSS
    pass

@app.get("/app.js")
async def get_js():
    """Phục vụ file JavaScript"""
    # TODO: Triển khai serve JS
    pass

@app.get("/api/health")
async def health_check():
    """Endpoint kiểm tra sức khỏe"""
    # TODO: Triển khai health check
    pass

@app.get("/api/map-data")
async def get_map_data(major_roads_only: bool = True):
    """Lấy dữ liệu OpenStreetMap cho các phường  cụ thể ở Bình Thạnh"""
    # TODO: Triển khai lấy dữ liệu OSM
    pass

# ==================== Endpoints Thuật Toán Cơ Bản ====================

@app.post("/api/bfs")
async def run_bfs(request: AlgorithmRequest) -> AlgorithmResponse:
    """Chạy thuật toán Breadth-First Search"""
    # TODO: Triển khai BFS endpoint
    pass

@app.post("/api/dfs")
async def run_dfs(request: AlgorithmRequest) -> AlgorithmResponse:
    """Chạy thuật toán Depth-First Search"""
    # TODO: Triển khai DFS endpoint
    pass

@app.post("/api/shortest-path")
async def find_shortest_path(request: AlgorithmRequest) -> AlgorithmResponse:
    """Tìm đường đi ngắn nhất sử dụng thuật toán Dijkstra"""
    # TODO: Triển khai shortest path endpoint
    pass

@app.post("/api/check-bipartite")
async def check_bipartite(request: AlgorithmRequest) -> AlgorithmResponse:
    """Kiểm tra xem đồ thị có phải bipartite"""
    # TODO: Triển khai bipartite check endpoint
    pass

# ==================== Endpoints Thuật Toán Nâng Cao ====================

@app.post("/api/prim")
async def run_prim(request: MSTRequest) -> MSTResponse:
    """
    Chạy thuật toán Prim cho Cây Khung Nhỏ Nhất
    
    Tham số:
        request: MST request với đồ thị và đỉnh bắt đầu tùy chọn
        
    Trả về:
        MST response với các cạnh và tổng trọng số
    """
    # TODO: Triển khai Prim endpoint
    pass

@app.post("/api/kruskal")
async def run_kruskal(request: MSTRequest) -> MSTResponse:
    """
    Chạy thuật toán Kruskal cho Cây Khung Nhỏ Nhất
    
    Tham số:
        request: MST request với đồ thị
        
    Trả về:
        MST response với các cạnh và tổng trọng số
    """
    # TODO: Triển khai Kruskal endpoint
    pass

@app.post("/api/ford-fulkerson")
async def run_ford_fulkerson(request: MaxFlowRequest) -> MaxFlowResponse:
    """
    Chạy thuật toán Ford-Fulkerson cho luồng cực đại
    
    Tham số:
        request: Max flow request với đồ thị, nguồn, và đích
        
    Trả về:
        Max flow response với giá trị luồng và các cạnh
    """
    # TODO: Triển khai Ford-Fulkerson endpoint
    pass

@app.post("/api/fleury")
async def run_fleury(request: EulerianRequest) -> EulerianResponse:
    """
    Chạy thuật toán Fleury cho đường đi Euler
    
    Tham số:
        request: Euler request với đồ thị và đỉnh bắt đầu tùy chọn
        
    Trả về:
        Euler response với thông tin đường đi
    """
    # TODO: Triển khai Fleury endpoint
    pass

@app.post("/api/hierholzer")
async def run_hierholzer(request: EulerianRequest) -> EulerianResponse:
    """
    Chạy thuật toán Hierholzer cho chu trình Euler
    
    Tham số:
        request: Euler request với đồ thị và đỉnh bắt đầu tùy chọn
        
    Trả về:
        Euler response với thông tin chu trình
    """
    # TODO: Triển khai Hierholzer endpoint
    pass

# ==================== Endpoints Thao Tác Đồ Thị ====================

@app.post("/api/add-edge")
async def add_edge(request: AddEdgeRequest):
    """
    Thêm cạnh vào đồ thị thủ công
    
    Tham số:
        request: Request với đồ thị, nguồn, đích, trọng số, và capacity
        
    Trả về:
        Dữ liệu đồ thị đã cập nhật
    """
    # TODO: Triển khai add edge
    pass

@app.post("/api/delete-node")
async def delete_node(request: DeleteNodeRequest):
    """
    Xóa một đỉnh và tất cả cạnh kết nối
    
    Tham số:
        request: Request với đồ thị và node_id
        
    Trả về:
        Dữ liệu đồ thị đã cập nhật
    """
    # TODO: Triển khai delete node
    pass

@app.post("/api/delete-edge")
async def delete_edge(request: DeleteEdgeRequest):
    """
    Xóa một cạnh khỏi đồ thị
    
    Tham số:
        request: Request với đồ thị, nguồn, và đích
        
    Trả về:
        Dữ liệu đồ thị đã cập nhật
    """
    # TODO: Triển khai delete edge
    pass

# ==================== Endpoints Chuyển Đổi & Lưu Trữ ====================

@app.post("/api/convert-representation")
async def convert_representation(request: ConversionRequest) -> ConversionResponse:
    """Chuyển đổi định dạng biểu diễn đồ thị"""
    # TODO: Triển khai conversion
    pass

@app.post("/api/save-graph")
async def save_graph(request: SaveGraphRequest) -> SaveGraphResponse:
    """Lưu đồ thị vào file"""
    # TODO: Triển khai save graph
    pass

@app.get("/api/load-graph/{filename}")
async def load_graph(filename: str) -> LoadGraphResponse:
    """Tải đồ thị từ file"""
    # TODO: Triển khai load graph
    pass

@app.get("/api/saved-graphs")
async def list_saved_graphs():
    """Liệt kê tất cả đồ thị đã lưu """
    # TODO: Triển khai list saved graphs
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
