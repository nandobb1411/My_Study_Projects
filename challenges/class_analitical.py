import cv2
import time
import numpy as np

#camera labs endereço
cap = cv2.VideoCapture('rtsp://admin:Avant1aa@10.81.18.32/onvif/profile2/media.smp')
class detectMotion:
    def __init__(self, name_stream, name_analytical=str(44), smallSize= 0,largSize=float('inf')):
        self.name_stream=name_stream
        self.name_analytical=name_analytical
        self.smallSize=smallSize
        self.largSize=largSize
        self.frame=None
        self.framePassado = None
        self.motion = ''
    def get_vis(self):
        return self.frame

    def send_event(self,motion):
        if motion == 'moveu':
            return 'Movimento'
        else:
            return ''
    def apply_video_analytics(self, frame):

        self.frame=frame.copy()
        if self.framePassado is None:
            self.framePassado=self.frame.copy()
            self.motion = ''
            return self.motion
        diff = cv2.absdiff(self.frame, self.framePassado)
        #frame1=self.frame.copy()
        #frame2= self.framePassado.copy()

        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        cv2.imshow("teste", dilated)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        self.framePassado = self.frame.copy()
        for c in contours:
        # when the bounding is small discard
            if not (cv2.contourArea(c) >= self.smallSize and cv2.contourArea(c) <= self.largSize):
                self.motion = ''
                return self.motion
            (x, y, w, h) = cv2.boundingRect(c)
            # draw a rectangle or contour around the calculated area
            cv2.rectangle(self.frame, (x, y), (x + w, y + h), (000, 255, 204), 1)
            #cv2.drawContours(self.frame, contours, -1, (76, 190, 23), 2)
        self.motion = 'Moveu'
        return self.motion

# while cap.isOpened():
#     diff = cv2.absdiff(frame1,frame2)
#     gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
#     blur = cv2.GaussianBlur(gray, (5,5), 0)
#     _,thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
#     dilated = cv2.dilate(thresh, None, iterations=3)
#     contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     cv2.drawContours(frame1, contours, -1, (76,190,23), 2)
#     cv2.imshow('feed',frame1)
#     frame1 = frame2
#     ret,frame2 = cap.read()
#     if cv2.waitKey(40)==27:
#         break
#
#
#



cv2.destroyAllWindows()
cap.release()


