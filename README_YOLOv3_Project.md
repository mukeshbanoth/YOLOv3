
# Real-Time Object Detection with YOLOv3 in Google Colab

## 📌 Project Summary

This project demonstrates a real-time object detection system using **YOLOv3** in **Google Colab**. It processes static video input and overlays bounding boxes and class labels for detected objects.

## 🧰 Tech Stack
- Python
- OpenCV
- NumPy
- YOLOv3 (Darknet)
- FFmpeg
- Google Colab

## 🚀 Key Features
- 🧠 YOLOv3 deep learning-based detection on video input
- 🎯 Class-wise Non-Maximum Suppression (NMS) for filtering overlapping boxes
- 📦 Frame-by-frame video processing with annotated outputs
- 🎞️ Conversion of output to MP4 using FFmpeg for easy sharing/viewing

## 🛠️ Workflow Summary
1. Load YOLOv3 model (`yolov3.cfg`, `yolov3.weights`)
2. Process input video (`video3.mp4`) using OpenCV
3. Perform detection, apply NMS, and draw labels
4. Save processed video and convert to `.mp4` for Colab preview

## 📁 Files Required
- `yolov3.cfg`
- `yolov3.weights`
- `coco.names`
- `video3.mp4`

## 📂 Output Files
- `output.avi`: Raw processed video with annotations
- `output.mp4`: Converted MP4 video ready for playback

## 🖼️ Output Preview
The 10th frame is previewed in Colab using `cv2_imshow`, and full video is rendered in-browser using base64 HTML embedding.

---

## 🔗 Download Model Files

Due to GitHub size limits, you can download these files from the official sources:

- [yolov3.weights](https://pjreddie.com/media/files/yolov3.weights)
- [yolov3.cfg](https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg)

