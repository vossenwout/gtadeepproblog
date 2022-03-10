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


labels_train = []
labels_test = []


def generate_data(path):
    train_counter = 0
    test_counter = 0

    training_data = np.load(path, allow_pickle=True)
    datasize = len(training_data)
    shuffle(training_data)
    for data in training_data:
        image = Image.fromarray(data[0])
        label = data[1]
        if train_counter < datasize * train_size:
            labels_train.append(label)
            image.save(image_train_path + "{}.png".format(train_counter))
            train_counter = train_counter + 1
        else:
            labels_test.append(label)
            image.save(image_test_path + "{}.png".format(test_counter))
            test_counter = test_counter + 1




def save_labels():
    train_file = open(label_train_path, 'a')
    for label in labels_train:
        train_file.write(str(label) + '\n')
    train_file.close()

    test_file = open(label_test_path, 'a')
    for label in labels_test:
        test_file.write(str(label) + '\n')
    test_file.close()


generate_data("balanced_data/balanced_data.npy")
save_labels()


