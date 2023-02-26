import cv2
import pynput

camera_port=0

camera=cv2.VideoCapture(camera_port)

file="C:/Users/Deus.DEUS.002/Downloads/Mifare_LucasM"

retval,img=camera.read()

cv2.imshow('Foto.jpg',img)

cv2.imwrite(file,img)

cv2.destroyAllWindows()

camera.release()



