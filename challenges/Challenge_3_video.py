import numpy as np
import cv2

cap = cv2.VideoCapture('rtsp://labs:yBtYHJ35Hk@mediastreaming.grupoavantia.com.br/Operacional/avantia_entrada_labs.stream')
while (True):
    ret, frame = cap.read()

    cv2.imshow('janela', frame)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()


#programa que abre uma camera no corredor do escritorio, para sair da camera apertar q.

#cap=cv2.VideoCapture('/home/fernandobellelis/Downloads/ab.mp4')

#Comando que abre um video no computador

#cap=cv2.VideoCapture('rtsp://labs:yBtYHJ35Hk@mediastreaming.grupoavantia.com.br/Operacional/avantia_entrada_labs.stream')


#