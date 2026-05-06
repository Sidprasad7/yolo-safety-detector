from ultralytics import YOLO
import cv2
import argparse

def run_detection(source, model_path, conf=0.5, show=True, save=False):
    """
    Run YOLOv8 safety gear detection.

    Args:
        source   : Path to image, video, or 0 for webcam
        model_path: Path to trained .pt weights file
        conf     : Confidence threshold (default 0.5)
        show     : Display results in a window
        save     : Save output to runs/detect/
    """
    model = YOLO(model_path)

    results = model.predict(
        source=source,
        conf=conf,
        show=show,
        save=save,
        line_width=2
    )

    for result in results:
        boxes = result.boxes
        for box in boxes:
            cls_id = int(box.cls[0])
            label  = model.names[cls_id]
            conf_score = float(box.conf[0])
            print(f"Detected: {label} | Confidence: {conf_score:.2f}")

    print("\n✅ Detection complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YOLOv8 Safety Gear Detector")
    parser.add_argument("--source",  type=str, default="0",
                        help="Image/video path or 0 for webcam")
    parser.add_argument("--weights", type=str,
                        default="runs/train/weights/best.pt",
                        help="Path to trained model weights")
    parser.add_argument("--conf",    type=float, default=0.5,
                        help="Confidence threshold (0.0 - 1.0)")
    parser.add_argument("--save",    action="store_true",
                        help="Save output images/video")
    args = parser.parse_args()

    run_detection(
        source=args.source,
        model_path=args.weights,
        conf=args.conf,
        show=True,
        save=args.save
    )
