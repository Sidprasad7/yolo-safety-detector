# 🦺 YOLOv8 Safety Gear Detector

> Custom-trained object detection system for real-time safety gear compliance checking.
> Detects helmets, harnesses, and carabiners using **4 YOLOv8 model variants** trained on a hand-annotated custom dataset.

---

## 🎯 What It Does

Automatically identifies whether workers are wearing the correct safety equipment in real-time from live camera feeds or video input — and outputs a **pass/fail safety check** for each detection.

**Detected Classes:**
- 🪖 Helmet
- 🦺 Harness
- 🔗 Carabiner

---

## 🧠 Model Variants

All 4 YOLOv8 variants were trained and benchmarked on the same custom dataset:

| Model | Size | Speed | Accuracy |
|---|---|---|---|
| YOLOv8n | Nano | ⚡ Fastest | Good |
| YOLOv8m | Medium | Fast | Better |
| YOLOv8l | Large | Moderate | High |
| YOLOv8x | Extra Large | Slower | Highest |

> Use `n` for edge/real-time deployment, `x` for maximum accuracy.

---

## 📁 Project Structure

```
yolo-safety-detector/
├── detect.py              # Run detection on image/video/webcam
├── train.py               # Train model on custom dataset
├── data.yaml              # Dataset configuration
├── classes.txt            # Custom class definitions
├── requirements.txt       # Python dependencies
├── dataset/
│   ├── images/            # Sample training images
│   └── labels/            # LabelImg annotation files (.txt)
└── runs/
    ├── train/             # Training results, metrics, graphs
    └── detect/            # Sample detection outputs
```

---

## ⚙️ Setup & Run

**1. Clone the repo**
```bash
git clone https://github.com/Sidprasad7/yolo-safety-detector.git
cd yolo-safety-detector
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run detection on an image**
```bash
python detect.py --source your_image.jpg --weights runs/train/weights/best.pt
```

**4. Run detection on webcam**
```bash
python detect.py --source 0 --weights runs/train/weights/best.pt
```

**5. Train on custom dataset**
```bash
python train.py --data data.yaml --model yolov8n.pt --epochs 100
```

---

## 🏷️ Dataset & Annotation

- Custom dataset built from scratch
- Annotated manually using **LabelImg**
- Labels in YOLO format (`.txt` per image)
- 3 custom classes: helmet, harness, carabiner

---

## 🔄 How It Works

```
Live Camera / Video Input
        ↓
YOLOv8 Model (n / m / l / x)
        ↓
Bounding Box Detection
        ↓
Class Identification
(helmet / harness / carabiner)
        ↓
Pass ✅  or  Fail ❌
Safety Check Output
```

---

## 📦 Requirements

```
ultralytics
opencv-python
torch
torchvision
labelImg
```

---

## 📹 Demo

> Demo video available on request — contact [Sidprasad07@gmail.com](mailto:Sidprasad07@gmail.com)

---

## Author

**Siddharth Prasad** — Frontend & AI Engineer
[GitHub](https://github.com/Sidprasad7) · [LinkedIn](https://linkedin.com/in/siddharth-prasad) · [Email](mailto:Sidprasad07@gmail.com)
