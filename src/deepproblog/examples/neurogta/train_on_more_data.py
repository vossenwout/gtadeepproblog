import torch

from deepproblog.engines import ExactEngine
from deepproblog.examples.neurogta.data.dataset import train_dataset, test_dataset
from deepproblog.model import Model
from deepproblog.network import Network

from deepproblog.dataset import DataLoader
from deepproblog.engines import ExactEngine
from deepproblog.evaluate import get_confusion_matrix
from deepproblog.examples.neurogta.data.dataset import train_dataset, test_dataset
from deepproblog.model import Model
from deepproblog.network import Network
from deepproblog.train import train_model

from deepproblog.utils.standard_networks import smallnet, SmallNet, MLP
from deepproblog.utils.stop_condition import Threshold, StopOnPlateau
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


key_dict = {0:"w", 4 : "w, a", 5 : "w, d"}

lr = 1e-4


gta_network1 = SmallNet(num_classes=3, N=10752)
gta_network2 = SmallNet(num_classes=3, N=768)
batch_size = 5
loader = DataLoader(train_dataset, batch_size)
gta_net1 = Network(gta_network1, "gta_net1", batching=True)
gta_net1.optimizer = torch.optim.Adam(gta_network1.parameters(), lr=lr)
gta_net2 = Network(gta_network2, "gta_net2", batching=True)
gta_net2.optimizer = torch.optim.Adam(gta_network2.parameters(), lr=lr)

model = Model("model5.pl", [gta_net1, gta_net2])
model.add_tensor_source("train", train_dataset)
model.add_tensor_source("test", test_dataset)
model.set_engine(ExactEngine(model), cache=True)

model.load_state("saved_models/gtamodel.pth")

train_obj = train_model(
    model,
    loader,
    StopOnPlateau("Accuracy", warm_up=10, patience=10)
    | Threshold("Accuracy", 1.0, duration=1),
    log_iter=100 // batch_size,
    test_iter=100 // batch_size,
    test=lambda x: [("Accuracy", get_confusion_matrix(x, test_dataset).accuracy())],
    infoloss=0.25,
)

model.save_state("saved_models/gtamodel.pth")


