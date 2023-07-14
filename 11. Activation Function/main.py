import torch
import torch.nn as nn

# option 1 (create nn modules)
class NeuralNet1(nn.Module):
    def __init__(self , input_size ,hidden_size):
        super(NeuralNet1 , self(input_size ,hidden_size))
        self.linear1  = nn.Linear(input_size , hidden_size)
        self.relu =nn.ReLU()
        self.linear2 = nn.Linear(hidden_size, 1)
        
    def forward(self, x):
        out =self.linear1(x)
        out =self.relu(out)
        out =self.linear2(out)
        # sigmoid at the end
        y_pred =torch.sigmoid(out)
        return y_pred


# option 2 (use activation functions directly in forward pass)
class NeuralNet(nn.Module):
    def __init__(self , input_size ,hidden_size):
        super(NeuralNet1 , self(input_size ,hidden_size))
        self.linear1  = nn.Linear(input_size , hidden_size)
        self.linear2 = nn.Linear(hidden_size, 1)
        
    def forward(self, x):
        out =torch.relu(self.Linear1(x))
        out = torch.sigmoid(self.Linear2(out))
        return out