# Sample working of the project

import cv2
import numpy as np
import face_recognition

imgShekhar = face_recognition.load_image_file("D:\Python Projects\Face Recognition and Attendance\Images\Shekhar.jpg")
imgShekhar = cv2.cvtColor(imgShekhar,cv2.COLOR_BGR2RGB)

imgTest = face_recognition.load_image_file("D:\Python Projects\Face Recognition and Attendance\Images\TestShekhar.jpg")
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgShekhar)[0]
encodeShekhar = face_recognition.face_encodings(imgShekhar)[0]
cv2.rectangle(imgShekhar,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(6, 112, 8, 1),2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(6, 112, 8, 1),2)

results = face_recognition.compare_faces([encodeShekhar],encodeTest)
print(results)

faceDis = face_recognition.face_distance([encodeShekhar],encodeTest)
print(faceDis) 

cv2.putText(imgTest,f'{results}{round(faceDis[0],2)}',(40,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

cv2.imshow("Shekhar Yadav",imgShekhar)
cv2.imshow("Shekhar Yadav Test",imgTest)
cv2.waitKey(0)


