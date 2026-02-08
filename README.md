# GAMING GESTURES 🎮✋

## Project Overview
This project enables users to play endless runner games such as **Temple Run**, **Subway Surfers**, or PC-based games **using only hand movements**, without touching the keyboard, mouse, or screen.

The system uses **real-time computer vision** to detect and track hand motion through a webcam and maps those movements to in-game controls.  
All hand tracking is done **invisibly** — no hand outlines, skeletons, or visual markers are displayed.

---

## Problem Statement
Traditional mobile and PC games require physical interaction with screens or input devices, which limits hands-free interaction and accessibility.

This project aims to:
- Enable **touch-free game control**
- Reduce hardware dependency
- Demonstrate real-time computer vision control systems

---

## Solution Approach
The system captures live video from a webcam, detects hand position using computer vision, tracks motion across frames, and translates directional movements into keyboard inputs that control the game.

The core logic is **rule-based**, prioritizing:
- Accuracy
- Low latency
- Demo reliability

---

## Key Features
- Real-time hand gesture detection
- No visual overlays or hand markings
- Gesture-to-keyboard control mapping
- Works with PC games and Android emulators
- Lightweight and low-latency execution
- No machine learning required for core functionality

---

## Gesture Mapping
| Hand Movement | Action | Key Trigger |
|--------------|--------|-------------|
| Move hand left | Move Left | Left Arrow |
| Move hand right | Move Right | Right Arrow |
| Move hand upward | Jump | Up Arrow |
| Move hand downward | Slide | Down Arrow |

---

## Tech Stack
- **Programming Language:** Python 3.9+
- **Computer Vision:** OpenCV, MediaPipe Hands
- **Numerical Processing:** NumPy
- **Input Simulation:** PyAutoGUI / pynput
- **Platform:** PC Games / Android Emulator

---

## Project Structure

gaming_gestures/
│
├── src/
│ ├── camera.py # Webcam capture
│ ├── hand_tracker.py # Hand detection (no drawing)
│ ├── gesture_logic.py # Motion tracking & gesture detection
│ ├── controller.py # Keyboard input control
│ └── main.py # Application entry point
│
├── requirements.txt
└── README.md


---

## System Workflow
1. Capture live video using webcam
2. Detect hand landmarks internally (not displayed)
3. Track hand center movement across frames
4. Identify gesture based on motion direction and speed
5. Trigger corresponding keyboard input
6. Game responds in real time

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/hand-gesture-game-control.git
cd hand-gesture-game-control
