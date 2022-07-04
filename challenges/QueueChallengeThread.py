import queue, threading, cv2

img = cv2.imread('/home/fernandobellelis/Imagens/Doguinho.jpg')

def GetImage(cv2,img):
    cv2.imshow("normal img",img)
    cv2.waitKey(0)


theimgs = [cv2.imread('/home/fernandobellelis/Imagens/Doguinho.jpg'),
           cv2.imread('/home/fernandobellelis/Downloads/archive/dogscatspersons/cats/cat.0.jpg'),
           cv2.imread('/home/fernandobellelis/Downloads/archive/dogscatspersons/cats/cat.1.jpg')]


for img in theimgs:
    t = threading.Thread(target=GetImage,args=(1,))
    t.start()


