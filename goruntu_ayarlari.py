import cv2

img=cv2.imread('bozukparalar.jpg')
grilestirme=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blurlama=cv2.medianBlur(grilestirme,5)
       