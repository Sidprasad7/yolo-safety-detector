# 🦺 YOLOv8 Safety Gear Detector

> Custom-trained object detection system for real-time safety gear compliance checking.
> Detects helmets, harnesses, and carabiners using **4 YOLOv8 model variants** trained on a hand-annotated custom dataset.

---

## 🎯 What It Does

Automatically identifies whether workers are wearing the correct safety equipment from live camera feeds or video input — and outputs a **pass/fail safety check** for each detection.

**Detected Classes:**
- 🪖 Helmet
- 🦺 Harness
- 🔗 Carabiner

---

## 🧠 Model Variants Trained

All 4 YOLOv8 variants were trained and benchmarked on the same custom dataset:

| Model | Size | Speed | Best For |
|---|---|---|---|
| YOLOv8n | Nano | ⚡ Fastest | Edge / real-time |
| YOLOv8m | Medium | Fast | Balanced |
| YOLOv8l | Large | Moderate | High accuracy |
| YOLOv8x | Extra Large | Slower | Maximum accuracy |

---

## 📁 Project Structure

```
yolo-safety-detector/
├── detect.py                  # Run detection on image/video/webcam
├── train.py                   # Train model on custom dataset
├── data_custom.yaml           # Dataset configuration
├── classes.txt                # Custom class definitions
├── requirements.txt           # Python dependencies
└── runs/
    └── detect/
        └── train/             # Training results & metrics
            ├── F1_curve.png
            ├── PR_curve.png
            ├── P_curve.png
            ├── R_curve.png
            ├── confusion_matrix.png
            └── results.png
```

---

## 📊 Training Results

| Metric | Detail |
|---|---|
| Model | YOLOv8 (n / m / l / x) |
| Classes | 3 (helmet, harness, carabiner) |
| Annotation Tool | LabelImg |
| Label Format | YOLO .txt format |

> See `runs/detect/train/` for full training curves and confusion matrix.

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
python detect.py --source your_image.jpg --weights path/to/best.pt
```

**4. Run detection on webcam**
```bash
python detect.py --source 0 --weights path/to/best.pt
```

**5. Train on custom dataset**
```bash
python train.py --data data_custom.yaml --model yolov8n.pt --epochs 100
```

---

## 🏷️ Dataset & Annotation

- Custom dataset built from scratch
- Images manually annotated using **LabelImg**
- Labels saved in YOLO format (`.txt` per image)
- 3 custom classes defined in `classes.txt`

---

## 🔄 How It Works

```
Live Camera / Video / Image Input
            ↓
    YOLOv8 Model (n/m/l/x)
            ↓
    Bounding Box Detection
            ↓
    Class Identification
  (helmet / harness / carabiner)
            ↓
    ✅ Pass  or  ❌ Fail
      Safety Check Output
```

---

## 📹 Demo

> Demo video available on request — [Sidprasad07@gmail.com](mailto:Sidprasad07@gmail.com)

---

## Author

**Siddharth Prasad** — Frontend & AI Engineer
[GitHub](https://github.com/Sidprasad7) · [LinkedIn](https://linkedin.com/in/siddharth-prasad) · [Email](mailto:Sidprasad07@gmail.com)
