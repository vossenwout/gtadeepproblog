import torch

from deepproblog.dataset import DataLoader
from deepproblog.engines import ExactEngine
from deepproblog.evaluate import get_confusion_matrix
from deepproblog.examples.neurogta.data.dataset import train_dataset, test_dataset, Traffic_keypress_data
from deepproblog.model import Model
from deepproblog.network import Network
from deepproblog.train import train_model

from deepproblog.utils.standard_networks import smallnet, MLP
from deepproblog.query import Query
from problog.logic import Term, Constant, Var

lr = 1e-4

gta_network1 = smallnet(num_classes=3, pretrained=True)
gta_net1 = Network(gta_network1, "gta_net1", batching=True)
gta_net1.optimizer = torch.optim.Adam(gta_network1.parameters(), lr=lr)



model = Model("../schets_experiment.pl", [gta_net1])

model.load_state("../saved_models/schetsmodel.pth")
model.set_engine(ExactEngine(model), cache=True)
sub = {Term("a"): Term("tensor", Term("train", Constant(0)))}
query = Query(Term("drivinginput", Term("a"), Constant(1)), sub)
query = query.variable_output()


#query = Query(Term("drivinginput", Term("tensor", Term("train", Constant(0))), Var("X_1")))
print(model.solve([query]))
#model.evaluate_nn([["gta_net1",query]])

