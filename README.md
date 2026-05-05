# 🛡️ AI Face Vault: Real-Time Biometric Access System

An intelligent facial recognition dashboard that bridges the gap between hardware-level computer vision and modern web interfaces. Developed as a transition project from Mechanical Engineering into the AI/ML space.

## 🚀 Overview
This system uses a Deep Learning backbone to identify authorized personnel via a live webcam feed. It features a responsive, high-tech web dashboard with real-time status updates and voice-synthesis feedback.

### Key Features
*   **Facial Recognition:** Powered by the `Facenet` model via the DeepFace library.
*   **Live Web Dashboard:** Real-time data streaming using Flask-SocketIO.
*   **Voice Feedback:** Automated audio greetings upon successful verification using the Web Speech API.
*   **Industrial UI:** A custom-styled "Glassmorphism" interface designed for low-light security environments.
*   **Security Logging:** Automatic timestamping of access events into a CSV database.

## 🛠️ Technical Stack
*   **Language:** Python 3.11
*   **AI Framework:** DeepFace (TensorFlow/Keras)
*   **Backend:** Flask, Flask-SocketIO
*   **Frontend:** HTML5, CSS3 (Modern Glassmorphism), JavaScript
*   **Computer Vision:** OpenCV

## 📁 Project Roadmap
```text
Face_Auth_Project/
├── db/               # Authorized user database (JPG images)
├── templates/        # UI layer (index.html)
├── app.py            # The AI Engine & Web Server
└── access_logs.csv   # Historical access record
