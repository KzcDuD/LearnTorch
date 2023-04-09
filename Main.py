import torch
import numpy as np

int_x = torch.tensor(1) # 整數型態tensor
float_x = torch.tensor(1.0) # 浮點數型態tensor
x=torch.tensor([[1,2],[3,4],[5,6]],dtype=torch.float64)
print(type(x))

torch.zeros([2, 2])
