import cv2
from ultralytics import YOLO

# Load YOLOv8l model
model = YOLO("yolov8l.pt")

# Open Pi camera
cap = cv2.VideoCapture(0)

# Optional: Set resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print("Camera could not be opened.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run inference
    results = model(frame)
    annotated_frame = results[0].plot()

    # Display
    cv2.imshow("YOLOv8 Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()