import torch

x = torch.tensor(1.0)
y = torch.tensor(2.0)

w = torch.tensor(1.0, requires_grad=True)

# forward pass and compute loss
y_hat =w*x # 1
loss = (y_hat -y)**2 #(1-2)^2=1

print(loss) # 1

# Backward pass
loss.backward()
print(w.grad) # dloss/dw = dloss/d(y_hat) * d(y_hat)/dw = -2*1 = -2
