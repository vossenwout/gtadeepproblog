import torch

from deepproblog.engines import ExactEngine
from deepproblog.examples.neurogta.data.dataset import train_dataset
from deepproblog.model import Model
from deepproblog.network import Network
import numpy as np
import keyboard
import torchvision.transforms as transforms

import cv2
import time
import os
from Xlib import display, X
from PIL import Image


from deepproblog.utils.standard_networks import smallnet, SmallNet
from deepproblog.query import Query
from problog.logic import Term, Constant

"""
THIS SCRIPT REQUIRES solver.solve() IN solver.py TO NOT CLEAR THE CACHE
REMEMBER TO UNDO THE COMMENT WHEN TRAINING A NEW MODEL
REMEMBER TO COMMENT WHEN RUNNING THIS SCRIPT


W
"""


key_dict = {0: "w", 2: "a", 3: "d", 4: "w, a", 5: "w, d", 8: ""}

lr = 1e-4

gta_network1 = SmallNet(num_classes=3, N=10752)
gta_network2 = SmallNet(num_classes=3, N=768)
batch_size = 5
gta_net1 = Network(gta_network1, "gta_net1", batching=True)
gta_net1.optimizer = torch.optim.Adam(gta_network1.parameters(), lr=lr)
gta_net2 = Network(gta_network2, "gta_net2", batching=True)
gta_net2.optimizer = torch.optim.Adam(gta_network2.parameters(), lr=lr)

model = Model("../model5.pl", [gta_net1, gta_net2])
model.add_tensor_source("train", train_dataset)
model.set_engine(ExactEngine(model), cache=True)

model.load_state("../saved_models/gtamodel.pth")



def tensor_to_query(tensor1, tensor2):
    #sub = {Term("a"): Term("tensor", Term("train", Constant(id)))}
    #sub = {Term("a"):  Term("tensor", Constant(0) ) }
    sub = {Term("a"): tensor1, Term("b"): tensor2 }
    query = Query(Term("drivinginput", Term("a"),Term("b"), Constant(1)), sub)
    return query.variable_output()

def query_model(query):
    return model.solve([query])


def get_keypress(tensor):
    answer = tensor[0]
    #temp = anaswer.result[0]
    max_ans = max(answer.result, key=lambda x: answer.result[x])
    #print("answer= {}".format(max_ans))
    #print("prob = {}".format(answer.result[max_ans]))
    answer = max_ans.args[2]
    return int(answer)


def simulate_keypress(keypress):
    press = key_dict.get(keypress)
    if press == "":
        time.sleep(0.2)
        return
    keyboard.press(press)
    time.sleep(0.2)
    keyboard.release(press)
    #keyboard.press_and_release(press)

def grabscreen(top_left_x, top_left_y,width,height):
    dsp = display.Display()
    image = None
    try:
        root = dsp.screen().root
        raw = root.get_image(top_left_x, top_left_y, width, height, X.ZPixmap, 0xffffffff)
        image = Image.frombytes("RGB", (width, height), raw.data, "raw", "BGRX")
    finally:
        dsp.close()
    return image

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



def getkeys():
    keys = []
    if keyboard.is_pressed('a'):
        keys.append('a')
    if keyboard.is_pressed('s'):
        keys.append('s')
    if keyboard.is_pressed('w'):
        keys.append('w')
    if keyboard.is_pressed('d'):
        keys.append('d')
    if keyboard.is_pressed('t'):
        keys.append('t')
    return keys

def drive():
    for i in list(range(4))[::-1]:
        print(i + 1)
        time.sleep(1)

    last_time = time.time()
    paused = True
    print('Press T to start')
    while (True):
        if not paused:
            screen = np.array(grabscreen(72,84,800,600))
            # resize to something a bit more acceptable for a CNN
            screen = cv2.resize(screen, (480, 270))
            # run a color convert:
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
            # Define a transform to convert the image to tensor
            transform = transforms.ToTensor()
            # screen is 480, 270
            speedo = screen[190:270, 350:480]
            horizon = screen[130:270, 0:480]


            # Convert the image to PyTorch tensor
            tensor1 = transform(horizon)
            tensor2 = transform(speedo)

            tensorId1 = model.store_tensor(tensor1)
            tensorId2 = model.store_tensor(tensor2)

            query = tensor_to_query(tensorId1, tensorId2)

            answer = query_model(query)

            keypress = get_keypress(answer)

            simulate_keypress(keypress)


        keys = getkeys()

        if 't' in keys:
            if paused:
                paused = False
                print('unpaused!')
                time.sleep(1)
            else:
                print('Pausing!')

                paused = True
                time.sleep(1)



drive()


