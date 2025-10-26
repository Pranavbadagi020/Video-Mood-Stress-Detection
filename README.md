# Video-Mood-Stress-Detection
# 🧠 Video Mood & Stress Detection

This project uses **DeepFace** and **OpenCV** to detect human emotions in real time using your webcam.  
It analyzes facial expressions frame-by-frame and displays the detected mood (like *happy*, *sad*, *angry*, *neutral*, etc.) directly on the video stream.

---

## 🎥 Demo

> Real-time facial emotion detection using your computer's camera.

<p align="center">
  <img src="https://github.com/Pranavbadagi020/Video-Mood-Stress-Detection/assets/demo_image_here" alt="Video Mood Detection Demo" width="600">
</p>

*(Replace the image link above with your own screenshot or demo GIF later.)*

---

## ⚙️ Features

✅ Real-time face emotion detection using webcam  
✅ Detects emotions — Happy, Sad, Angry, Fear, Surprise, Disgust, Neutral  
✅ Displays emotion live on video stream  
✅ Lightweight and easy to run locally  
✅ Built with DeepFace, OpenCV, and TensorFlow  

---

## 🧩 Tech Stack

| Component | Description |
|------------|--------------|
| **Python** | Programming language |
| **DeepFace** | Facial emotion recognition framework |
| **OpenCV** | Real-time video processing |
| **TensorFlow** | Backend for DeepFace |
| **NumPy** | Image data handling |

---

## 🛠️ Installation

Make sure you have **Python 3.10+** installed.

Then follow these steps in your terminal:

```bash
# 1️⃣ Clone this repository
git clone https://github.com/Pranavbadagi020/Video-Mood-Stress-Detection.git
cd Video-Mood-Stress-Detection

# 2️⃣ (Optional but recommended) Create a virtual environment
python3 -m venv venv
source venv/bin/activate   # for macOS/Linux
venv\Scripts\activate      # for Windows

# 3️⃣ Install dependencies
pip install opencv-python deepface tensorflow-macos tensorflow-metal tf-keras


//run this code
python3 main.py
