import torch
import torchvision
from torch.utils.data import Dataset,DataLoader
import numpy as np
import math

# gradient computation etc. not efficient for whole data set
# -> divide dataset into small batches

'''
# training loop
for epoch in range(num_epochs):
    # loop over all batches
    for i in range(total_batches):
        batch_x, batch_y = ...
'''

# epoch = one forward and backward pass of ALL training samples
# batch_size = number of training samples used in one forward/backward pass
# number of iterations = number of passes, each pass (forward+backward) using [batch_size] number of sampes
# e.g : 100 samples, batch_size=20 -> 100/20=5 iterations for 1 epoch

# --> DataLoader can do the batch computation for us

# Implement a custom Dataset:
# inherit Dataset
# implement __init__ , __getitem__ , and __len__

class WineDataset(Dataset):
    
    def __init__(self):
        # data loading
        xy = np.loadtxt('./wine.csv',delimiter=",",dtype=np.float32 ,skiprows=1)
        self.x= torch.from_numpy(xy[:,1:])
        self.y =torch.from_numpy(xy[:,[0]]) # n_samples , 1
        self.n_samples =xy.shape[0]
        
    def __getitem__(self,index):
        return self.x[index],self.y[index]
    
    def __len__(self):
        return self.n_samples

dataset = WineDataset()
# first_data =dataset[0]
# features , labels = first_data
# print(features , labels)

dataloader =DataLoader(dataset=dataset , batch_size =4,shuffle =True,num_workers=0) # num_worker 多執行續

# datatiter =iter(dataloader)
# data = datatiter.next()
# features,labels = data
# print(features ,labels)

# training loop
num_epochs =2
total_sample =len(dataset)
n_iterations = math.ceil(total_sample/4)
print(total_sample ,n_iterations)

for epoch in range(num_epochs):
    for i ,(inputs,labels) in enumerate(dataloader):
        # forward backward ,update
        if(i+1)%5 ==0:
            print(f'epoch {epoch+1}/{num_epochs}, step {i+1}/{n_iterations}, input {inputs.shape}')

# torchvision.datasets.MNIST()
# fashion-mnist ,, cifar ,coco