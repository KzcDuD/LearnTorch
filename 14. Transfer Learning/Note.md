# Transfer Learning

+ First task reused as the starting point for ,model to second part
+ Example: We can train a model to classify cats ans burds ,ans use the same model modified only in the last layer ans then used a new model to classify bees and gocks.
+ advantage: Use transfer learning Can don't need to train a whole model again.

---

## Program Explain

+ `Data Preparation`:

    The data is loaded from the "FaceR_Dataset" directory using datasets.ImageFolder.
    Two sets are created ['train' , 'val'] , with different data transformations defined in data_transforms.

+ `Transfer Learning Setup`:

    A pre-trained ResNet-18 model is loaded with torchvision.models.resnet18(pretrained=True).
    The last fully connected layer of the ResNet model (fc) is replaced with a new nn.Linear layer to match the number of classes in the new dataset (2 classes for binary classification).
    Freezing Layers:

    All layers of the pre-trained ResNet model, except the final fully connected layer, are frozen (i.e., their gradients will not be computed during backpropagation).

+ `Training Function (train_model)`:

    This function trains the modified ResNet model.
    It performs the training and validation in each epoch.
    For each epoch, it runs the training and validation phases, updating the model weights accordingly.
    The learning rate scheduler is applied during the training phase to adjust the learning rate based on the epoch number.
    The best model weights (highest validation accuracy) are saved and later used for testing.

+ `Loss and Optimization`:

    The cross-entropy loss (nn.CrossEntropyLoss) is used as the loss function.
    Stochastic Gradient Descent (optim.SGD) is used as the optimizer to update the parameters of the final fully connected layer.

+ `Learning Rate Scheduling`:

    The learning rate is decayed by a factor of 0.1 every 7 epochs using lr_scheduler.StepLR. This helps in fine-tuning the model efficiently.

+ `Device and Main Execution`:

    The code checks whether a CUDA-capable GPU is available and sets the device accordingly.
    The model is trained by calling the train_model function with the appropriate parameters.

---

## Reference

[轉移學習](https://medium.com/%E6%88%91%E5%B0%B1%E5%95%8F%E4%B8%80%E5%8F%A5-%E6%80%8E%E9%BA%BC%E5%AF%AB/transfer-learning-%E8%BD%89%E7%A7%BB%E5%AD%B8%E7%BF%92-4538e6e2ffe4)
