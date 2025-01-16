# Core Operations

This repository contains code related to image processing, video handling, and computer vision operations. The files are organized as follows:

## Files Description

### `rescale.py`

This Python script provides a utility function for rescaling images and videos to a desired size. It includes functionality for adjusting the frame dimensions for better visualization or processing. Key features:

- **Image Rescaling**: Modify the resolution of static images.
- **Video Rescaling**: Adjust the resolution of video frames for compatibility with different systems.

### `videoio.py`

This script demonstrates basic operations for handling video files using OpenCV. Key functionalities include:

- **Video Capture**: Read video streams from files or camera devices.
- **Frame Processing**: Iterate through video frames for display or processing.
- **Window Management**: Proper handling of video display windows and cleanup after processing.

### `io.ipynb`

A Jupyter Notebook demonstrating the following:

- **Image Reading and Display**: Load and visualize images using OpenCV and Matplotlib.
- **Video Playback**: Play video files in a loop while demonstrating how to handle real-time video streams.
- **Code Examples**: Practical examples with annotations for educational or reference purposes.

---

## Prerequisites

The following libraries are required to run the scripts:

- `OpenCV`: For image and video processing (`cv2`).
- `Matplotlib`: For image visualization in the Jupyter notebook.

### Installation

To install the required libraries, run:

```bash
pip install opencv-python matplotlib
```

---

## Usage

1. **Run `rescale.py`**:
   Use this script to adjust the resolution of images and videos. Pass the input files and desired dimensions as arguments.
2. **Run `videoio.py`**:
   Demonstrates reading and displaying video frames from a file or a camera. Use it as a base for real-time video applications.
3. **Open `io.ipynb`**:
   Explore the Jupyter Notebook for interactive examples of image and video handling. Use JupyterLab or Jupyter Notebook to open and execute the file.

---
