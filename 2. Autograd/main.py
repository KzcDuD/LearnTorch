import torch

x= torch.rand(3 ,requires_grad=True) #Is True if gradients need to be computed for this Tensor, default False otherwise.
# print(x)

y=x+2

# print(y)
# z= y*y+2
# z=z.mean()
# print(z)

# v= torch.tensor([0.1,1.0,0.001],dtype=torch.float32)
# z.backward(v) # dz/dx
# print(x.grad)

# x.requires_grad_(False)
# y= x.detach() # same value without grad
# with torch.no_grad():
#     y=x+2
# print(x)

weights= torch.ones(4,requires_grad=True)
for epoch in range(3):
    model_output = (weights*3).sum()
    model_output.backward()
    print(weights.grad)
    weights.grad.zero_()

# optimizer = torch.optim.SGD(weights, lr=0.01)
# optimizer.step()
# optimizer.zero_grad()

