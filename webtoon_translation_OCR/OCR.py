import os
from PIL import Image
import pytesseract
import numpy as np
import cv2
from translate import Translator

def translate_korean_to_english(text):
    #ja for japanese
    translator = Translator(to_lang='en', from_lang='ko')

    # Translate the text to English
    translation = translator.translate(text)

    # Return the translated text
    return translation

def TL(image_path):
    image=cv2.imread(image_path)
    img=image

    tessdata_dir_config = '--tessdata-dir "/Users/joonghochoi/Desktop"'

    height, width, channel = image.shape #If channel=3, colour image. If 1, gray image
    print("image is ",image_path)
    print("height ",height, "width ",width, "channel ",channel )

    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Convert the image to grayscale
    ret, thresh = cv2.threshold(img_gray, 127, 255, 0)

    kernel = np.ones((5,5), np.uint8) # Define the kernel for erosion and dilation

    contours2, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    script=""
    d=dict()
    for cnt in contours2:
        area = cv2.contourArea(cnt)
        if area > 2000:  # Replace 1000 with the desired area threshold
            x, y, w, h = cv2.boundingRect(cnt)
            roi = image[y:y+h, x:x+w]
            # roi = thresh[y:y+h, x:x+w]  # Crop the region of interest
            text = pytesseract.image_to_string(roi, lang='kor', config=tessdata_dir_config)
            
            if len(text.strip()) > 0:  # Check if the extracted text is not empty
                #print("text: ",text)
                text=text.strip()
                if text not in d:       
                    d[text]=1
                    english_text = translate_korean_to_english(text)
                    script+=english_text
                    script+="\n"
    text_file = open("KTL.txt", "a")
    n = text_file.write(image_path+"\n"+script)
    text_file.close()

folder_path = "./KTL_work"
# Iterate over the files in the directory
items=os.listdir(folder_path)
items.sort()
print("sorted items ",items)
for filename in items:
    #print(filename)
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Construct the full path to the image file
        image_path = os.path.join(folder_path, filename)

        # Call the 'meow' function on the image file
        TL(image_path)
        #print("1")
