import os
import glob

import cv2
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


def generate_data2(path):
    train_counter = 0
    test_counter = 0

    training_data = np.load(path, allow_pickle=True)
    datasize = len(training_data)
    shuffle(training_data)
    for data in training_data:
        # dit verandere zodat roi als input np array krijgt
        image = Image.fromarray(data[0])
        label = data[1]
        #creating training set
        if train_counter < datasize * train_size * 2:
            labels_train.append(label)
            roi(image).save(image_train_path + "{}.png".format(train_counter))
            cropped_image = split_speedometer(image)
            cropped_image.save(image_train_path + "{}.png".format(train_counter+1))
            train_counter = train_counter + 2
        #creating test set
        else:
            labels_test.append(label)
            roi(image).save(image_test_path + "{}.png".format(test_counter))
            cropped_image = split_speedometer(image)
            cropped_image.save(image_test_path + "{}.png".format(test_counter+1))
            test_counter = test_counter + 2

def roi(image):
    width, height = image.size
    left = 0
    right = width
    bottom = height
    top= height-140
    cropped_image = image.crop((left, top, right, bottom))

    return cropped_image

def split_speedometer(image):

    width, height = image.size

    # Setting the points for cropped image
    left = width - 130
    top = height - 80
    right = width
    bottom = height

    cropped_image = image.crop((left, top, right, bottom))

    return cropped_image





def save_labels():
    train_file = open(label_train_path, 'a')
    for label in labels_train:
        train_file.write(str(label) + '\n')
    train_file.close()

    test_file = open(label_test_path, 'a')
    for label in labels_test:
        test_file.write(str(label) + '\n')
    test_file.close()


generate_data2("balanced_data/balanced_data.npy")
save_labels()


