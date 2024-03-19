import os

os.system("pip install opencv-python")
os.system("pip install opencv-contrib-python")
os.system("pip install opencv-python-headless")
os.system("pip install opencv-contrib-python-headless")
os.system("pip install numpy")
os.system("pip install np")

import cv2
# import np
import numpy as np


# Get the current working directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the image file in the same directory
image1_path = os.path.join(current_directory, 'image1.jpg')
image2_path = os.path.join(current_directory, 'image2.jpg')

# Load the two images
# image1 = cv2.imread('image1.jpg')
# image2 = cv2.imread('image2.jpg')

image1 = cv2.imread(image1_path)
image2 = cv2.imread(image2_path)

# Set the degree of mixing for each channel (values between 0 and 1)
# alpha_red = 0.5  # Mixing ratio for Red channel
# alpha_green = 0.3  # Mixing ratio for Green channel
# alpha_blue = 0.7  # Mixing ratio for Blue channel

alpha_red = int(input("Enter the value for alpha_red (1-100): ")) / 100
alpha_green = int(input("Enter the value for alpha_green (1-100): ")) / 100
alpha_blue = int(input("Enter the value for alpha_blue (1-100): ")) / 100

# Combine the images
combined_image = cv2.addWeighted(image1, alpha_red, image2, 1 - alpha_red, 0)
combined_image = cv2.addWeighted(combined_image, alpha_green, image2, 1 - alpha_green, 0)
combined_image = cv2.addWeighted(combined_image, alpha_blue, image2, 1 - alpha_blue, 0)

# Save the combined image in the current folder as 'output.jpg'
cv2.imwrite('output.jpg', combined_image)

# softy_plug
