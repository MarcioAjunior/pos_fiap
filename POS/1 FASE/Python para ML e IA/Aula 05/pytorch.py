import torch
import torch.nn as nn

class DynamicModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(DynamicModel, self).__init__()
        self.layer1 = nn.Linear(input_size, hidden_size)
        self.layer2 = nn.Linear(hidden_size, output_size)
        
    def forward(self, x):
        x = torch.relu(self.layer1(x))
        return self.layer2(x)
    
#Criando uma instancia do modelo
modelo = DynamicModel(input_size = 10, hidden_size=64, output_size=5)