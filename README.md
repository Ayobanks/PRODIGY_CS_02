🖼️ Image Manipulation Script
This Python script inverts the colors of an image and replaces any fully transparent pixels with solid white. The modified image is then saved as a new file with _manipulated added to the filename.

✨ Features
Inverts RGB values of each pixel.

Converts fully transparent pixels (0, 0, 0, 0) to white (255, 255, 255, 255).

Saves the manipulated image with a new name (e.g., cat_manipulated.png).

📦 Requirements
Python 3.x

Pillow (Python Imaging Library fork)

Install the required package:
pip install pillow

🚀 Usage
Clone this repository or download the script.

Ensure the image you want to manipulate is in the same directory.

Run the script:
python manipulate_image.py
Enter the image filename when prompted (e.g., cat.png).

The script will generate a new file (e.g., cat_manipulated.png).

🧪 Example
Input Prompt:
Input the name of the image with the extension you want to manipulate (e.g cat.png): cat.png

Output:
cat_manipulated.png created successfully.

📌 Notes
Only .png and other RGBA-compatible formats are supported.
