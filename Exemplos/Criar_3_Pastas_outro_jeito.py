import os
import shutil
import random

"""
Dataset
    train
        dog
        cat
    val
        dog
        cat
    test
        dog
        cat
"""

path_source = "/home/fernandobellelis/Downloads/archive/dogscatspersons"
path_dest = "/home/fernandobellelis/Downloads/archive/mySplit"

classes = os.listdir(path_source)

train_split = 0.8
val_split = (1 - train_split)/2


for subfolder in ["train", "val", "test"]:

    for _class in classes:
        p = os.path.join(path_dest, subfolder, _class)

        if not os.path.exists(p):
            os.makedirs(p)

for _class in classes:

    path_class = os.path.join(path_source, _class)
    images = os.listdir(path_class)
    random.shuffle(images)

    len_images = len(images)
    train_limit = int(train_split * len_images)
    val_limit = int(val_split * len_images)

    train_set = images[:train_limit]
    val_set = images[train_limit:train_limit+val_limit]
    test_set = images[train_limit+val_limit:]

    dataset = {
        "train": train_set,
        "val": val_set,
        "test": test_set
    }

    for key in dataset.keys():

        _set = dataset[key]

        for image in _set:

            path_image_source = os.path.join(path_source, _class, image)
            path_image_dest = os.path.join(path_dest, key, _class, image)

            print(path_image_source,",",path_image_dest)
            shutil.copyfile(path_image_source, path_image_dest)

