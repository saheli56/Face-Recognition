# Face Recognition

This project is a simple face recognition application using OpenCV in Python. It captures video from a camera or an IP stream, detects faces in real-time, and displays the video with rectangles drawn around detected faces.

## Features
- Real-time face detection using Haar cascades
- Supports both local webcam and IP camera streams
- Easy to use and modify

## Requirements
- Python 3.x
- OpenCV (`opencv-python`)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/saheli56/Face-Recognition.git
   ```
2. Navigate to the project directory:
   ```bash
   cd "Face Recognition"
   ```
3. Install the required packages:
   ```bash
   pip install opencv-python
   ```

## Usage
1. Run the main script:
   ```bash
   python main.py
   ```
2. The application will try to open the IP camera stream first. If it fails, it will use the local webcam.
3. Press `q` to quit the video window.

## Customization
- To use a different IP camera, change the `url` variable in `main.py`.
- You can adjust the face detection parameters in the script for better accuracy.

## License
This project is licensed under the MIT License.
