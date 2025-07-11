# YOLOv8 with Raspberry Pi Camera (Raspberry Pi 5)

This project runs YOLOv8 (large model) with real-time object detection using the Raspberry Pi Camera.

## 🚀 Setup

### 1. Install Dependencies

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv libopencv-dev python3-opencv -y
```

### 2. Create Virtual Environment

```bash
python3 -m venv yolov8env
source yolov8env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Download YOLOv8l Model

```bash
wget https://github.com/ultralytics/assets/releases/download/v8.0.0/yolov8l.pt
```

### 4. Run the Program

```bash
python3 main.py
```

Press `q` to exit.

## 🐢 Note
YOLOv8l is heavy. For better performance, use:
```python
model = YOLO("yolov8n.pt")
```
Download:
```bash
wget https://github.com/ultralytics/assets/releases/download/v8.0.0/yolov8n.pt
```