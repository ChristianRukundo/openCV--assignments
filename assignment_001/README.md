# 🛠️ License Plate Annotation Assignment 🛠️

This repository contains an image processing script that uses OpenCV to annotate license plates in images. The program reads an image, draws a rectangle around the license plate area, adds a sample license plate number text, and saves the annotated image. This project is great for learning about OpenCV's basic functionalities such as image loading, drawing shapes, text annotation, and image saving.

---

## 🔧 Features

- **Image Processing**:
  - Reads the input image.
  - Draws a green rectangle around a region (simulating a license plate).
  - Adds text annotation (license plate number).
  - Saves the final annotated image.

- **OpenCV Functions**:
  - `cv2.imread()`: Reads images.
  - `cv2.rectangle()`: Draws a rectangle around the license plate.
  - `cv2.putText()`: Adds text to the image.
  - `cv2.imshow()`: Displays the image with annotation.

---

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed:

- **Python 3.6 or later**
- **OpenCV** library (if not installed, follow the instructions below).

---

### 📝 Installation Steps

1. **Install OpenCV via pip**:
   To get started with OpenCV, run the following command:

   ```bash
   pip install opencv-python
