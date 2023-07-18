import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms
import matplotlib as plt
import numpy as np

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

train_loader = torchvision.datasets.Dataloader(train_dataset , batch_size=batch_size , shuffle=True)

test_loader = torchvision.datasets.Dataloader(test_dataset , batch_size=batch_size , shuffle=False)

classes = ('plane' , 'car' , 'brid' , 'cat', 'deer','dog','frog','horse','ship','truck')

# implement conv net
class ConvNet(nn.Module):
    def __init__(self):
        pass

    def forward(self,x):
        pass

model = ConvNet().to(device)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters() , lr =learning_rate)

n_total_steps =len(train_loader)
for epoch in range(num_epochs):
    for i,(image,labels) in enumerate(train_loader):
        # origin shape: [4,3,32,32] = 4,3,1024
        # input_layer: 3 input channels, 6 output channels, 5 kernel size
        images =images.to(device)
        labels =labels.to(device)

        # forward pass
        outputs =model(images)
        loss = criterion(outputs,labels)

        # Backward and optimizer
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if(i+1)%2000 ==0:
            print(f'Epoch[{epoch+1}/{num_epochs}], Step[{i+1}/{n_total_steps}], Loss: {loss.item():.4f}')
print("Finish Training.")

with torch.no_grad():
    n_correct =0
    n_samples =0
    n_class_correct =[0 for i in range(10)]
    n_class_samples = [0 for i in range(10)]
    for image , labels in test_loader:
        images =images.to(device)
        labels =labels.to(device)
        outputs =model(image)
        # max return (value , index)
        _,predicted = torch.max(outputs,1)
        n_samples += labels.size(0)
        n_correct +=(predicted ==labels).sum().item()

        for i in range(batch_size):
            label =labels[i]
            pred = predicted[i]
            if(label ==pred):
                n_class_correct[label]+=1
            n_class_samples[label] +=1

    acc = 100.0 * n_correct / n_class_samples
    print(f'Accuracy of the network:{acc} %')

    for i in range(10):
        acc =100.0 * n_class_correct[i] / n_class_samples[i]
        print(f'Accuracy of {classes[i]}: {acc} %')

