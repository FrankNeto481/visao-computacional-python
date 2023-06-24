from tkinter import *
from tkinter import ttk
import cv2 
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


#OPEN IP CAMERA
url = 'http://192.168.0.128:8080/video'
cap = cv2.VideoCapture(url)

solucao_reconhecimento_rosto = mp.solutions.face_detection
reconhecedor_rostos = solucao_reconhecimento_rosto.FaceDetection()
desenho = mp.solutions.drawing_utils

while True:
    #Ler as informações da webcam
    verificador, frame = cap.read()

    if not verificador:
        break

    #reconhecer os rostos que tem ali dentro
    list_rostos = reconhecedor_rostos.process(frame)

    if list_rostos.detections:
        for rosto in list_rostos.detections:
            #desenhar os rostos na imagem
            desenho.draw_detection(frame, rosto)
    cv2.imshow("Rostos na Webcam", frame)
    #quando apertar ESC, para o Loop
    if cv2.waitKey(5) == 27:
        break

cap.release()