import torch 
import torch.nn as nn

class Model(nn.Module):
    def __init__(self, n_input_features):
        super(Model,self).__init__()
        self.linear =nn.Linear(n_input_features,1)
        
    def forward(self,x):
        y_pred =torch.sigmoid(self.linear(x))
        return y_pred

model =Model(n_input_features=6)
### train model

FILE ="model.pth"
torch.save(model.state_dict(), FILE)

for parm in model.parameters():
    print(parm)


### load model
# model =torch.load(FILE)
# model.eval()

loaded_model =Model(n_input_features=6)
loaded_model.load_state_dict(torch.load(FILE))
loaded_model.eval()

for parm in model.parameters():
    print(parm)