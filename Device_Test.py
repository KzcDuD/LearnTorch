import torch 

torch.cuda.is_available()

x_train = torch.FloatTensor([0.,1.,2.])
x_train.is_cuda

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)

X_train = x_train.to(device)
print(X_train.is_cuda)