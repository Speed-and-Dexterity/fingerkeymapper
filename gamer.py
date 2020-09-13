import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
img = cv2.imread("altkeyboardb.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(img,30,200)
img = edged
boxes = pytesseract.image_to_boxes(img)
hImg,wimg = img.shape
for b in boxes.splitlines():
    b = b.split(" ")
    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img,(x,hImg-y), (w,hImg-h),(0,0,255),8)
cv2.imshow("s",img)
cv2.waitKey()
#img = cv2.bitwise_not(img) ## reverse black and white ##
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# edged = cv2.Canny(img,30,200)
# #contours, hierarchy = cv2.findContours(edged,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
# #cv2.imshow("help", edged)
# #cv2.waitKey()
# #cv2.drawContours(img,contours,-1,(0,255,0),3)
# cv2.imwrite("altkeyboardb.jpg", img)
# cv2.waitKey()
# cv2.destroyAllWindows()