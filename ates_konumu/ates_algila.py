import numpy as np
import cv2
import time
import math
from calc_distance import atesin_konumu

fire_cascade = cv2.CascadeClassifier('fire_detection.xml')
file = open("fire_pos.log", "w+")

en_boy = [640, 480]
'''
en_boy[0] = int(input("en orani: "))
en_boy[1] = int(input("boy orani: "))
'''
drone_konum = [124, 65]

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, en_boy[0])
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, en_boy[1])


konumlar = []

while 1:
    a = 1
    ret, img = cap.read()

    fire = fire_cascade.detectMultiScale(img, 1.2, 5)
    for (x,y,w,h) in fire:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

        ates_pos = [x + w / 2, y + h / 2]
        ates_konum = atesin_konumu([124, 65], en_boy, ates_pos, 12, 1.3)
        uzaklik = math.sqrt((drone_konum[0] - ates_konum["x"])**2 + (drone_konum[1] - ates_konum["y"])**2)
        
        for konum in konumlar:
            if int(konum[0]) == int(ates_konum["x"]) and int(konum[1]) == int(ates_konum["y"]):
                a = 0
                break
        if a == 1:
            print("atesin drone'ya uzakligi: " + str(uzaklik) + "mt.")
            konumlar.append([ates_konum["x"], ates_konum["y"]])
        
    cv2.imshow('img',img)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

for konum in konumlar:
    file.write(str(konum[0]) + "|" + str(konum[1]) + "\n")

file.close()
cap.release()
cv2.destroyAllWindows()

# TODO: algilanan atesin konuma bakılarak bidaha algilanmamasi lazım