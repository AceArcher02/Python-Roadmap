import cv2
img=cv2.impread("D\\:pick &videos\\pics\\3.jpeg")
cv2.imshow('Image',img)
print("The shape of the image is",img.shape)
print("The size of the image is",img.size)
cv2.waitKey(0)
#waitKey keeps the window open and provides small break between two parameters 
