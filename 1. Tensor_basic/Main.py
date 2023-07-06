import torch
import numpy as np

int_x = torch.tensor(1) # 整數型態tensor
float_x = torch.tensor(1.0) # 浮點數型態tensor
x=torch.tensor([[1,2],[3,4],[5,6]],dtype=torch.float64)
print(type(x))

torch.zeros([2, 2])
x= torch.rand(2,2)
y= torch.rand(2,2)
print(x+y)

y.add_(x)
print(y)

z= torch.sub(x,y)
z=torch.mul(x,y)

x=torch.rand(5,3)
print(x)
print(x[1,1].item())

a=torch.ones(5)
print(a)
b=a.numpy()
print(b)

a.add_(1)
print(a)
print(b) #same memory loc ,there will be a.add().numpy()
