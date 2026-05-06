from ultralytics import YOLO

model = YOLO("yolov8e.pt")

model.train(data = "data_custom.yaml", batch=8, imgsz=640, epochs=100, workers=1)