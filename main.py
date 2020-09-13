# fingers = [["P","R","M","I","T"],["T","I","M","R","P"]]

# def findkeyboard():
#     pass
#     # make the keyboard into a mask and initalize a dict with the coordinates of every key and its value 
# def findfinger(keypress):
#     pass
import cv2 
import numpy as np


filter = False

img = cv2.imread("keyboard.jpg")
template = cv2.imread("qkey.png")
w, h = template.shape[:-1]
img.astype(np.float32)

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = cv2.GaussianBlur(gray, (5, 5), 0)
# #img.astype(np.float32)
# gray = cv2.adaptiveThreshold(gray, 255,  cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 7, 4)
#gray.astype(np.float32)
res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
print(top_left)
print(bottom_right)
cv2.rectangle(img,top_left, bottom_right, 255)
cv2.imshow("g",img)
cv2.waitKey()