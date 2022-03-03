import os
import glob

import lockfile.pidlockfile
import numpy as np
from PIL import Image
from random import shuffle


local_path = os.path.dirname(os.path.abspath(__file__))
image_test_path = "{}/image_data/test/".format(local_path)
image_train_path = "{}/image_data/train/".format(local_path)
label_test_path = "{}/label_data/test.csv".format(local_path)
label_train_path = "{}/label_data/train.csv".format(local_path)

#sizes stand for the distribution of data over test and training set
train_size = 0.8


counter = 0
labels_train = []
labels_test = []


def generate_data(path):
    training_data = np.load(path, allow_pickle=True)
    datasize = len(training_data)
    shuffle(training_data)
    for data in training_data:
        image = Image.fromarray(data[0])
        label = data[1]
        if counter < datasize * train_size:
            labels_train.append(label)
            image.save(image_train_path + "{}.png".format(counter))
        else:
            labels_test.append(label)
            image.save(image_test_path + "{}.png".format(counter))

        counter = counter+1


def save_labels():
    train_file = open(label_train_path, 'a')
    for label in labels_train:
        train_file.write(label + '\n')
    train_file.close()

    test_file = open(label_test_path, 'a')
    for label in labels_test:
        test_file.write(label + '\n')
    test_file.close()


generate_data()
save_labels()


