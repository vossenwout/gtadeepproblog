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


from deepproblog.utils.standard_networks import smallnet
from deepproblog.query import Query
from problog.logic import Term, Constant

"""
THIS SCRIPT REQUIRES solver.solve() IN solver.py TO NOT CLEAR THE CACHE
REMEMBER TO UNDO THE COMMENT WHEN TRAINING A NEW MODEL
REMEMBER TO COMMENT WHEN RUNNING THIS SCRIPT


W
"""


key_dict = {0:"w", 4 : "w, a", 5 : "w, d"}

lr = 1e-4

gta_network1 = smallnet(num_classes=3, pretrained=True)
gta_net1 = Network(gta_network1, "gta_net1", batching=True)
gta_net1.optimizer = torch.optim.Adam(gta_network1.parameters(), lr=lr)

model = Model("../model4.pl", [gta_net1])
model.set_engine(ExactEngine(model), cache=True)
#model.add_tensor_source("live_dataset", train_dataset)
model.load_state("../saved_models/gtamodel.pth")


def tensor_to_query(tensor):
    #sub = {Term("a"): Term("tensor", Term("train", Constant(id)))}
    #sub = {Term("a"):  Term("tensor", Constant(0) ) }
    sub = {Term("a"): tensor}
    query = Query(Term("drivinginput", Term("a"), Constant(1)), sub)
    return query.variable_output()

def query_model(query):
    return model.solve([query])


def get_keypress(tensor):
    answer = tensor[0]
    max_ans = max(answer.result, key=lambda x: answer.result[x])
    print("answer= {}".format(max_ans))
    print("prob = {}".format(answer.result[max_ans]))
    answer = max_ans.args[1]
    return int(answer)


def simulate_keypress(keypress):
    press = key_dict.get(keypress)

    keyboard.press(press)
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
            screen = np.array(grabscreen(0,0,800,600))
            # resize to something a bit more acceptable for a CNN
            screen = cv2.resize(screen, (480, 270))
            # run a color convert:
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
            # Define a transform to convert the image to tensor
            transform = transforms.ToTensor()

            # Convert the image to PyTorch tensor
            tensor = transform(screen)

            tensorId = model.store_tensor(tensor)

            query = tensor_to_query(tensorId)

            answer = query_model(query)

            keypress = get_keypress(answer)

            simulate_keypress(keypress)

            keys = getkeys()

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


