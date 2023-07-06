import torch 

torch.cuda.is_available()

x_train = torch.FloatTensor([0.,1.,2.])
#x_train.is_cuda

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device) #cuda

X_train = x_train.to(device)
print(X_train.is_cuda) #True

#------------------------------------

x= torch.ones(5,device=device)
y=torch.ones(5)
y=y.to(device)
z=x+y
z=z.to("cpu")
print(z.is_cuda) #False
