Face Blur using OpenCV

This project uses OpenCV to detect human faces from a webcam feed and automatically blur them in real time. If no face is detected, it displays a message "No Face Found!" on the screen.

 Features

Captures live video from your webcam

Detects faces using Haar Cascade Classifier

Applies Gaussian Blur on detected face regions

Displays "No Face Found!" when no face is detected

Press q to exit the application

 Requirements

Make sure you have the following installed:

Python 3.x

OpenCV library

Install OpenCV with:

pip install opencv-python


(Optional, for extra features)

pip install opencv-contrib-python

 How to Run

Clone this repository or copy the code into a file, e.g. face_blur.py

Open a terminal and run:

python face_blur.py


A window will open showing the webcam feed.

Detected faces will be blurred automatically.

Press q to quit.
