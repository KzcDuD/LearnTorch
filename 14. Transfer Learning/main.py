# imageFolder
# Scheduler
# Transfer Learning

import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
import numpy as np
import torchvision
from torchvision import datasets, models ,transforms
import matplotlib.pyplot as plt
import time
import os
import copy

device =torch.device("cuda" if torch.cuda.is_available() else"cpu")

mean = np.array([0.485,0.456,0.406])
std = np.array([0.229,0.224,0.225])

data_transforms={
    'train':transforms.Compose([
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(mean, std)
    ]),
    'val': transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean, std)
    ])
}

# import data
data_dir = '../data/hymenoptera_data'
sets = ['train','val']
image_datasets = { x:datasets.ImageFolder(os.path.join(data_dir,x),
                                         data_transforms[x])
                  for x in ['train','val']}

dataloaders = {x: torch.utils.data.DataLoader(image_datasets[x],batch_size=4,
                                              shuffle=True, num_workers=0)
               for x in ['train','val']}

dataset_sizes = {x: len(image_datasets[x]) for x in ['train','val']}
class_names =image_datasets['train'].classes
print(class_names)

def train_model(model, criterion, optimizer, scheduler, num_epochs=25):
    since =time.time()
    
    best_model_wts = copy.deepcopy(model.state_dict())
    best_acc = 0.0
    
    for epoch in range(num_epochs):
        print(f'Epoch {epoch}/{num_epochs-1}')
        print('-'*10)
        
        # Each epoch has a training ans validation phase
        for phase in ['train','val']:
            if phase =='train':
                model.train()
            else:
                model.eval()
            
            running_loss =0.0
            running_correct = 0
            
            # Iterate over data.
            for inputs, labels in dataloaders[phase]:
                inputs = inputs.to(device)
                labels = labels.to(device)
                
                # forward
                # track history if only in train
                with torch.set_grad_enabled(phase =='train'):
                    outputs =model(inputs)
                    _,preds = torch.max(outputs,1)
                    loss = criterion(outputs, labels)
                    
                    # backward + optimize only if in training phase
                    if phase =='train':
                        optimizer.zero_grad()
                        loss.backward()
                        optimizer.step()
                        
                # statistics
                running_loss += loss.item() * inputs.size(0)
                running_correct += torch.sum(preds==labels.data)
            
            if phase =='train':
                scheduler.step()
            epoch_loss = running_loss / dataset_sizes[phase]
            epoch_acc = 100.0 * running_correct.double() / dataset_sizes[phase]
            
            print('{} Loss {:.4f} Acc: {:.4f}%'.format(
                phase,epoch_loss,epoch_acc
            ))
            
            # deep copy the model
            if phase =='val' and epoch_acc > best_acc:
                best_acc =epoch_acc
                best_model_wts =copy.deepcopy(model.state_dict())
            
        print()
    
    time_elapsed = time.time()-since
    print('Training complete in {:.0f}m {:.0f}s'.format(
        time_elapsed//60, time_elapsed%60
    ))
    print('Best val Acc: {:4f}%'.format(best_acc))
    print()
    
    # load best model weights
    model.load_state_dict(best_model_wts)
    return model

#### Finetuning convnet
model = models.resnet18(pretrained =True)
num_ftrs =model.fc.in_features

model.fc =nn.Linear(num_ftrs, 2) # 2 classes
model.to(device)

criterion =nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.001)

# scheduler

step_lr_scheduler = lr_scheduler.StepLR(optimizer,step_size=7,gamma=0.1) 
# Every 7 epochs , learning rate is multiplied gamma value

# train() # optimizer.step()
# evaulate()
# scheduler.step()

model = train_model(model ,criterion, optimizer, step_lr_scheduler, num_epochs=2)

#### ConvNet as fixed feature extractor
model_conv = torchvision.models.resnet18(pretrained=True)
# we need to freeze all the network except the final layer.
for param in model_conv.parameters():
    param.requires_grad = False

# Parameters of newly constructed modules have requires_grad=True by default
num_ftrs = model_conv.fc.in_features
model_conv.fc = nn.Linear(num_ftrs, 2)

model_conv = model_conv.to(device)

criterion = nn.CrossEntropyLoss()

# Observe that only parameters of final layer are being optimized as
# opposed to before.
optimizer_conv = optim.SGD(model_conv.fc.parameters(), lr=0.001, momentum=0.9)

# Decay LR by a factor of 0.1 every 7 epochs
exp_lr_scheduler = lr_scheduler.StepLR(optimizer_conv, step_size=7, gamma=0.1)

model_conv = train_model(model_conv, criterion, optimizer_conv,
                         exp_lr_scheduler, num_epochs=2)