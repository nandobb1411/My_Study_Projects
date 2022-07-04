import cv2
import os
import time
import threading

os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"
rtsp1 = 'rtsp://userid:password@192.168.1.108:8080/h264_ulaw.sdp'
rtsp = 'rtsp://userid:password@192.168.1.136:10554/udp/av0_0'


def getPicture(url):


    cam = cv2.VideoCapture(url)
    a = cam.get(cv2.CAP_PROP_BUFFERSIZE)
    cam.set(cv2.CAP_PROP_BUFFERSIZE, 3)
    start_frame_number = 20
    cam.set(cv2.CAP_PROP_POS_FRAMES, start_frame_number)

    print("buffer" + str(a))

    while True:
        ret, frame = cam.read()
        small_frame = cv2.resize(frame, (0, 0), fx=.50, fy=.50)
        small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("camera", small_frame)

        key = cv2.waitKey(20)
        if key == 27:  # exit on ESC
            break

# When everything done, release the video capture object
    cam.release()

# Closes all the frames
    cv2.destroyAllWindows()

if __name__ == '__main__':
    t1 = threading.Thread(target=getPicture, args=(rtsp,))
    t2 = threading.Thread(target=getPicture, args=(rtsp1,))

    t1.start()
    t2.start()