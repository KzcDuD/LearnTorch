import torch
import torchvision
import torchvision.transforms as transforms
import torch.nn as nn
import matplotlib.pyplot as plt
import numpy as np
import ssl

# close SSL Verification
ssl._create_default_https_context = ssl._create_unverified_context

# device configuration
device  = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Hyper-parameters
num_epochs =4
batch_size = 4
learning_rate =0.001

# dataset has PILImage images of range [0,1]
# We transform them to Tensor of normalized rage [-1,1]
transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))])

train_dataset = torchvision.datasets.CIFAR10(root='../data',train=False,
                                             download=True, transform=transform)

test_dataset = torchvision.datasets.CIFAR10(root='../data',train=False,
                                             download=True,transform=transform)

train_loader = torch.utils.data.DataLoader(train_dataset , batch_size=batch_size , shuffle=True)

test_loader = torch.utils.data.DataLoader(test_dataset , batch_size=batch_size , shuffle=False)

classes = ('plane' , 'car' , 'brid' , 'cat', 'deer','dog','frog','horse','ship','truck')

def imshow(img):
    img =img /2+0.5
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.show()

# get some random training images
dataiter =iter(train_loader)
images , labels = next(dataiter)

# show images
imshow(torchvision.utils.make_grid(images))

conv1 =nn.Conv2d(3, 6 ,5)
pool = nn.MaxPool2d(2,2)
conv2 = nn.Conv2d(6, 16 ,5)
print(images.shape)

x = conv1(images)
print(x.shape) # (32-5+0)/1+1 =28
x=pool(x)
print(x.shape)
x=conv2(x)
print(x.shape)
x = pool(x)
print(x.shape) 