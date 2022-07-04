import os
import sys
import shutil
import cv2
import random



path = "/home/fernandobellelis/Downloads/archive/dogscats/train" #diretorio onde se encontra as duas pastas de cachorros e gatos

classes = os.listdir(path)

lim_elements_training = 40 #limite de elementos do training
lim_elements_testing = 20 #limite de elementos do testing
lim_elements_validating = 30 #l imite de elementos do validating


def create_folder(path,classes, lim_elements):
    #alterando o nome de cada path baseado no lim_elements
    if lim_elements==40:
        dest_folder = "/home/fernandobellelis/Downloads/archive/training"
    elif lim_elements==20:
        dest_folder = "/home/fernandobellelis/Downloads/archive/testing"
    elif lim_elements==30:
        dest_folder = "/home/fernandobellelis/Downloads/archive/validating"


    for _class in classes:
        path_class = os.path.join(path,_class)
        path_dest = os.path.join(dest_folder, _class)
        if not os.path.exists(path_dest):
            os.makedirs(path_dest)
        images=os.listdir(path_class)
        slice = random.sample(images,lim_elements)
        for img in slice:
            path_img = os.path.join(path_class,img)
            path_img_dest =os.path.join(path_dest,img)


            images = cv2.imread(path_img,1)
            images = cv2.resize(images, (200, 200))
            cv2.imwrite(path_img_dest,images)


create_folder(path,classes,lim_elements_training)
create_folder(path,classes,lim_elements_validating)
create_folder(path,classes,lim_elements_testing)

