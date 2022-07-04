import class_analitical
import cv2
analitics = class_analitical.detectMotion(
    name_stream='44',
    name_analytical=str(44),
    smallSize= -54,
    largSize=float('inf'),


)
cap = cv2.VideoCapture('rtsp://admin:Avant1aa@10.81.18.32/onvif/profile2/media.smp')
while cap.isOpened():
    ret,frame = cap.read()
    if not ret:
        continue
    frame_that_goes = frame.copy()
    motion = analitics.apply_video_analytics(frame_that_goes)
    evento=analitics.send_event(motion)
    print('meu evento',evento)
    frame_desenhado = analitics.get_vis()
    cv2.imshow('resultado',frame_desenhado)
    cv2.waitKey(1)