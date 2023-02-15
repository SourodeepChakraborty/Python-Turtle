import cv2
import numpy as np

image = cv2.imread('puji.png')

image_resized = cv2.resize(image,None,fx= 1,fy= 1)

image_clear = cv2.medianBlur(image_resized, 3)
image_clear = cv2.medianBlur(image_clear, 3)
image_clear = cv2.medianBlur(image_clear, 3)

image_clear = cv2.edgePreservingFilter(image_clear, sigma_s = 5)

image_filtered = cv2.bilateralFilter(image_clear,3,10,5)

for i in range(2):
    image_filtered = cv2.bilateralFilter(image_clear,3,20,10)

for i in range(2):
    image_filtered = cv2.bilateralFilter(image_clear, 5, 30, 10)


gaussian_mask = cv2.GaussianBlur(image_filtered,(7,7),2)
image_sharp = cv2.addWeighted