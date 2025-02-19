
from PIL import Image
import pytesseract
import numpy as np
import cv2

image = cv2.imread('blue_period.jpg')
#image = cv2.imread('bluelock.jpg')
img=image
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Convert the image to grayscale
height, width, channel = image.shape #If channel=3, colour image. If 1, gray image
print("height ",height, "width ",width, "channel ",channel )



ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
"""
Threshold the image. Thresholding is a technique used to convert a grayscale image into a binary image. 
The threshold function sets all pixel values above a certain threshold value to white and all pixel 
values below the threshold value to black.

127: The threshold value. Pixels with values below this threshold will be set to black, 
and pixels with values above this threshold will be set to white.
255: The maximum value to use for the output binary image.
cv2.THRESH_BINARY: The thresholding mode to use
"""
cv2.imshow('Original', img)
cv2.imshow('Thresholded', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
Erosion and dilation are morphological operations used to remove small noise 
and smooth the edges of an object in an image. Erosion removes pixels at the 
edges of an object, while dilation adds pixels to the edges of an object. 

"""
kernel = np.ones((5,5), np.uint8) # Define the kernel for erosion and dilation

erosion = cv2.erode(img, kernel, iterations=1) # Apply erosion
dilation = cv2.dilate(img, kernel, iterations=1) # Apply dilation

cv2.imshow('Original', img)
cv2.imshow('Erosion', erosion)
cv2.imshow('Dilation', dilation)

contours2, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
"""
The cv2.RETR_TREE parameter specifies the retrieval mode for contours, 
and cv2.CHAIN_APPROX_SIMPLE specifies the contour approximation method.

The contours variable will contain a list of contours, and the 
hierarchy variable will contain the hierarchy information for each contour.

"""
#print("contours",contours)
#print("hierarchy",hierarchy)

"""
text = pytesseract.image_to_string(pil_image, lang="jpn_vert")
      #https://github.com/tesseract-ocr/tessdata/blob/main/jpn_vert.traineddata
      #download data from above and run command below to use japanese 
      #sudo mv jpn_vert.traineddata /usr/local/share/tessdata/
"""

"""
#Draw the contour in green

print("length ",len(contours2))
for cnt in contours2:
    area = cv2.contourArea(cnt)
    if area >= 3000:  # Replace 1000 with the desired area value
        cv2.drawContours(image, [cnt], 0, (0, 255, 0), 2)  
    # print("area ",area)
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""


###
for cnt in contours2:
    area = cv2.contourArea(cnt)
    if area > 2000:  # Replace 1000 with the desired area threshold
        x, y, w, h = cv2.boundingRect(cnt)
        roi = thresh[y:y+h, x:x+w]  # Crop the region of interest
        text = pytesseract.image_to_string(roi, lang='eng',)  # Perform OCR on the cropped image
        #not using configuration below as it worsened the performance.
        #text = pytesseract.image_to_string(roi, lang='eng',config='--psm 6 -l eng')
        #config='--oem 3 --psm 6 -l eng' to use LSTM OCR engine and English language.
        # --psm 6  for single uniform text lines, while --psm 11 is used for dense text with uniform character sizes.
        if len(text.strip()) > 0:  # Check if the extracted text is not empty
            print("text: ",text)
            cv2.rectangle(thresh, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw a green rectangle around the contour

# Display the image with the contours containing text outlined
cv2.imshow('Original image', image)
cv2.imshow('Thresh image', thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()

#implement pre-processing