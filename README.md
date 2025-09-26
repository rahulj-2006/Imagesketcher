# Image Sketcher 🎨

A simple yet powerful desktop application built with Python and CustomTkinter that converts your favorite images into beautiful line-art sketches.

![Image Sketcher App Interface](https://i.imgur.com/your-screenshot-url.png)
_Note: You can take a screenshot of your app and upload it to a site like [Imgur](https://imgur.com/upload) to get a URL to replace the one above._

---

## ## Features

* **Modern UI:** A clean and intuitive user interface built with CustomTkinter.
* **Image Selection:** Easily select any JPG or PNG image from your computer.
* **Live Drawing:** Generates a pencil-like sketch in a new window using Python's `turtle` graphics for a live drawing effect.
* **Reusable Canvas:** The drawing canvas is automatically cleared for each new sketch.

---

## ## Technology Stack

* **Language:** Python
* **GUI Framework:** CustomTkinter
* **Sketch Logic:** sketchpy
* **Image Handling:** Pillow, OpenCV-Python

---

## ## Setup and Installation

Follow these steps to get the application running on your local machine.

#### **Prerequisites**

* Python 3.8 or newer
* Git

#### **Installation Steps**

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/rahulj-2006/Imagesketcher.git](https://github.com/rahulj-2006/Imagesketcher.git)
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd Imagesketcher
    ```

3.  **Create and activate a virtual environment:**
    * **On Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    * **On macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

4.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## ## How to Use

Once the setup is complete, run the application with the following command:

```bash
python app.py
