import torch

from deepproblog.dataset import DataLoader
from deepproblog.engines import ExactEngine
from deepproblog.evaluate import get_confusion_matrix
from deepproblog.examples.neurogta.data.dataset import train_dataset, test_dataset
from deepproblog.model import Model
from deepproblog.network import Network
from deepproblog.train import train_model

from deepproblog.utils.standard_networks import smallnet, SmallNet, MLP
from deepproblog.utils.stop_condition import Threshold, StopOnPlateau

from deepproblog.examples.Forth import EncodeModule
from network import GTA_CNN

batch_size = 5
loader = DataLoader(train_dataset, batch_size)
lr = 1e-4

gta_network1 = smallnet(num_classes=3, pretrained=True)
#gta_network1 = SmallNet(num_classes=3, N=10752) #10752
gta_network2 = SmallNet(num_classes=3, N=768)
#gta_network2 = smallnet(num_classes=3, pretrained=True)
#gta_network3 = SmallNet(num_classes=3, N=10752)
gta_network3 = smallnet(num_classes=3, pretrained=True)
#gta_network1 = MLP(3,512,512)
#gta_network1 = GTA_CNN()

gta_net1 = Network(gta_network1, "gta_net1", batching=True)
gta_net1.optimizer = torch.optim.Adam(gta_network1.parameters(), lr=lr)
gta_net2 = Network(gta_network2, "gta_net2", batching=True)
gta_net2.optimizer = torch.optim.Adam(gta_network2.parameters(), lr=lr)
gta_net3 = Network(gta_network3, "gta_net3", batching=True)
gta_net3.optimizer = torch.optim.Adam(gta_network3.parameters(), lr=lr)

model = Model("model5.pl", [gta_net1, gta_net2, gta_net3])
model.add_tensor_source("train", train_dataset)
model.add_tensor_source("test", test_dataset)
model.set_engine(ExactEngine(model), cache=True)


#print(gta_network1.features[0].weight)
"""
train_obj = train_model(
    model,
    loader,
    StopOnPlateau("Accuracy", warm_up=10, patience=10)
    | Threshold("Accuracy", 1.0, duration=2),
    log_iter=100 // batch_size,
    test_iter=100 // batch_size,
    test=lambda x: [("Accuracy", get_confusion_matrix(x, test_dataset).accuracy())],
    infoloss=0.25,
)
"""
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




#print(gta_network1.features[0].weight)




