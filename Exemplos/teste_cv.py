import cv2
cap = cv2.VideoCapture('rtsp://admin:12345@10.81.18.50/live4.sdp')
while cap.isOpened():
    ret,frame = cap.read()
    if not ret:
        continue
    cv2.imshow('janela',frame)
    cv2.waitKey(1)