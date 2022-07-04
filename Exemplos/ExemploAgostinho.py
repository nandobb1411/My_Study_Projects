import os
import sys
import shutil
import cv2
import random
path = "/home/agostinho/Datasets/archive/dogscats/train"
dest_folder = "/home/agostinho/Datasets/archive/random"
classes = os.listdir(path)

lim_elements = 50
for _class in classes:
    path_class = os.path.join(path, _class)
    path_dest = os.path.join(dest_folder, _class)
    if not os.path.exists(path_dest):
        os.makedirs(path_dest)
    images = os.listdir(path_class)
    slice = random.sample(images, lim_elements)
    for img in slice:
        path_img = os.path.join(path_class, img)
        path_img_dest = os.path.join(path_dest, img)
        path_img_dest = path_img_dest.replace(".jpg", ".png")
        image = cv2.imread(path_img, 1)
        image = cv2.resize(image, (224, 224), cv2.INTER_CUBIC)
        cv2.imwrite(path_img_dest, image)
        shutil.copyfile(path_img, path_img_dest)