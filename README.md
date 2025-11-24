# Histology-Dev--
Histology scan spatial partitioning &amp; Pseudocolor density analysis 

# 📌 Overview
+ This project provides a distributed system for processing **high-resolution histology scans**.  
+ The pipeline leverages **Spatial partitioning** to divide tissue images into independent tiles, which are then distributed across a local cluster of worker nodes.  

The system is designed for scalability, modularity, and efficient visualization of large histological datasets.
# ⚙️ Features
- **Spatial Partitioning**: Divide massive histology scans into manageable tiles.
- **Distributed Processing**: Tiles are sent to worker nodes via TCP/IP sockets.
- **Pseudocolor Density Analysis**: Apply optical density mapping with OpenCV colormaps.
- **Spectral Visualization**: Use Jet colormap to simulate attenuation coefficients.
- **Image Manipulation**: Pillow integration for preprocessing and tile management.
- **Cluster-ready**: Local worker nodes can be scaled horizontally.

# 🛠️ Tech Stack
- **Language**: Python 3
- **Libraries**:
  - [OpenCV](https://opencv.org/) → Density thresholding & colormapping
  - [Pillow](https://python-pillow.org/) → Image manipulation
  - [socket](https://docs.python.org/3/library/socket.html) → TCP/IP networking

----

# 🚀 Getting Started

# 1. Clone the Repository
```bash
git clone 
cd histology-scan
pip install opencv-python pillow
python src/master.py --input data/sample_scan.tif




