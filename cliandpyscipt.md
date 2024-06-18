the Python code and CLI command for training a YOLO model:

**Python Code:**
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLOv8n model
model = YOLO("yolov8n.pt")

# Train the model on the Open Images V7 dataset
results = model.train(data="open-images-v7.yaml", epochs=100, imgsz=640)
```

**CLI Command:**
```bash
# Train a COCO-pretrained YOLOv8n model on the Open Images V7 dataset
yolo detect train data=open-images-v7.yaml model=yolov8n.pt epochs=100 imgsz=640
```