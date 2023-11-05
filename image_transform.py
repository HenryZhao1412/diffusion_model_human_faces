# Import needed libraries for the code.
import os
from PIL import Image
from shutil import copy2

# This function is writen for collecting all jpg images from
# different folders of source_path and copy them into
# direction_path.
def collect_images(source_path, direction_path):

    if not os.path.exists(direction_path):
        os.makedirs(direction_path)

    for subdir, dirs, files in os.walk(source_path):
        for file in files:
            if file.lower().endswith(".jpg"):
                file_path = os.path.join(subdir, file)
                copy2(file_path, direction_path)

# This function is to convert the images in jpg format into
# png format
def convert_to_png(source_dir):

    for file in os.listdir(source_dir):
        if file.lower().endswith(".jpg"):
            file_path = os.path.join(source_dir, file)
            image = Image.open(file_path)
            png_path = os.path.splitext(file_path)[0] + ".png"
            image.save(png_path, "PNG")
            os.remove(file_path)

# The location of the source folder and the direction folder.
source_path = "/Users/zhaohengji/Desktop/Thesis/archive/lfw-deepfunneled"
direct_path = "/Users/zhaohengji/Desktop/GSS"

# Execute the functions.
collect_images(source_path, direct_path)
convert_to_png(direct_path)

