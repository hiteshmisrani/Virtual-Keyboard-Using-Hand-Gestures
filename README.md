# Virtual Keyboard Using Hand Gestures

## Project Overview
This project implements a virtual keyboard that can be controlled using hand gestures, allowing users to type without physical contact with any device. The system uses computer vision techniques to detect and track hand movements, translating specific gestures into keyboard inputs.

## Video Demo
[Click here](https://github.com/yourusername/Virtual-Keyboard-Using-Hand-Gestures/blob/main/Demo.mp4) for demo video.

## Key Features
- **Real-time hand detection**: Uses OpenCV and MediaPipe to detect and track hand landmarks
- **Gesture recognition**: Identifies specific hand gestures for key selection and input
- **Virtual keyboard interface**: Displays an on-screen keyboard that responds to hand movements
- **Input simulation**: Converts recognized gestures into actual keyboard inputs using PyAutoGUI
- **Customizable layout**: Allows users to modify keyboard layout and gesture mappings

## Technology Stack
- Python 3.x
- OpenCV (for computer vision)
- MediaPipe (for hand tracking)
- PyAutoGUI (for input simulation)
- NumPy (for numerical operations)

## Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/Virtual-Keyboard-Using-Hand-Gestures.git

# Navigate to project directory
cd Virtual-Keyboard-Using-Hand-Gestures

# Install dependencies
pip install -r requirements.txt
