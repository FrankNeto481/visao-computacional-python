from tkinter import *
from tkinter import ttk
import cv2 
import numpy as np
import mediapipe as mp

#mediapipe
mp_hands=mp.solutions.hands
mp_drawing=mp.solutions.drawing_utils

#OPEN IP CAMERA
def camera():
    url = 'http://192.168.0.128:8080/video'
    cap = cv2.VideoCapture(url)
    with mp_hands.Hands(max_num_hands=2,min_detection_confidence=0.7, min_tracking_confidence=0.5) as hands:
        while cap.isOpened():
            ret, frame = cap.read()

        #applying hand tracking
            image=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

            image.flags.writeable = False

            results = hands.process(image)

            image.flags.writeable = True
        #annotations on the img
            image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)    
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, hand_landmarks, connections=mp_hands.HAND_CONNECTIONS)
            if frame is not None:
                cv2.imshow('HandTracking',frame)
            q = cv2.waitKey(1)
            if q == ord("q"):
                break
        cv2.destroyAllWindows()



#JANELA
janela = Tk()
janela.title("Camera")

texto_orientacao = Label(janela, text= "Welcome to IP access Camera")
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

#Botao
botao = Button(janela, text="Open Camera",width=10, height=2, command=camera,  bg='white')
botao.grid(column=0,row=1, sticky=W)


#senha gerada
texto_senha = Label(janela, text="Created by: Frank Neto")
texto_senha.grid(column=0,row=4, padx=10, pady=10)

#NON RESIZABLE
janela.resizable(0,0)



janela.mainloop()