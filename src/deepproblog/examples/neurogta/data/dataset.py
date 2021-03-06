import os

import torchvision.transforms as transforms

from deepproblog.dataset import ImageDataset
from deepproblog.query import Query
from problog.logic import Term, Constant

path = os.path.dirname(os.path.abspath(__file__))

transform = transforms.Compose(
    [transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]
)


class Traffic_keypress_data_schets(ImageDataset):
    def __init__(
        self,
        subset,
    ):
        # ???
        super().__init__("{}/image_data_schets_experiment/{}/".format(path, subset), transform=transform)
        #super().__init__("{}/image_data/{}/".format(path, subset), transform=transform)
        self.data = []
        self.subset = subset
        # we halen alle key inputs op en steken ze in array
        with open("{}/label_data_schets_experiment/{}.csv".format(path, subset)) as f:
        #with open("{}/label_data/{}.csv".format(path, subset)) as f:
            for line in f:
                self.data.append(line)

    def to_query(self, i):
        key_input = int(self.data[i])

        # we formuleren input query
        sub = {Term("a"): Term("tensor", Term(self.subset, Constant(i)))}
        #return Query(Term("drivinginput", Term("a"), Term(key_input)), sub)
        return Query(Term("drivinginput", Term("a"), Constant(key_input)), sub)

    def __len__(self):
        return len(self.data)


class Traffic_keypress_data(ImageDataset):
    def __init__(
        self,
        subset,
    ):
        # ???
        super().__init__("{}/image_data/{}/".format(path, subset), transform=transform)
        #super().__init__("{}/image_data/{}/".format(path, subset), transform=transform)
        self.data = []
        self.subset = subset
        # we halen alle key inputs op en steken ze in array
        with open("{}/label_data/{}.csv".format(path, subset)) as f:
        #with open("{}/label_data/{}.csv".format(path, subset)) as f:
            for line in f:
                self.data.append(line)

    def to_query(self, i):
        key_input = int(self.data[i])

        # we formuleren input query
        sub = {Term("a"): Term("tensor", Term(self.subset, Constant(i*2))),
               Term("b") : Term("tensor", Term(self.subset, Constant(i*2+1))),
               Term("c"): Term("tensor", Term(self.subset, Constant(i*2)))}
        #return Query(Term("drivinginput", Term("a"), Term(key_input)), sub)
        return Query(Term("drivinginput", Term("a"),Term("b"),Term("c"), Constant(key_input)), sub)

    def __len__(self):
        return len(self.data)


#train_dataset = Traffic_keypress_data_schets("train")
train_dataset = Traffic_keypress_data("train")
test_dataset = Traffic_keypress_data("test")
