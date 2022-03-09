import torch.nn as nn
import torch.nn.functional as F

class GTA_CNN(nn.Module):
    def __init__(self):
        super(GTA_CNN, self).__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(3, 10, 5),
            nn.MaxPool2d(32, 32),  # 6 24 24 -> 6 12 12
            nn.ReLU(True),
            #nn.Linear(254,1)
            #nn.Conv2d(10, 16, 5),  # 6 12 12 -> 16 8 8
            #nn.MaxPool2d(2, 2),  # 16 8 8 -> 16 4 4
            #nn.ReLU(True),
            #nn.Linear()
        )
        self.fc1 = nn.Linear(2250, 3)

    def forward(self, x):
        #x = x.unsqueeze(0)

        x = self.encoder(x)
        #flatten the tensor for the linear layer
        x = x.view(-1, 2250)
        x = self.fc1(x)

        return x



