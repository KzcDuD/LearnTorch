# Convolutional Neural Network (CNN)

## Archiecture

+ Feature learning
  + convolution,ReLU
  + Max Pooling
    small the image
+ Classification
  + Flatten 
  + Fully connected
  + softmax

## Dataset
`CIFAR-10`

## TestCNN

[Source](./TestCNN.py)

### Output_size

`output_size = (input_size - kernel_size + 2 * padding) / stride + 1`

+ Explain:
    1. `Input Size`: The input size refers to the spatial dimensions of the input image or feature map that is fed into the convolutional layer.

    2. `Kernel (Filter) Size`: The kernel (or filter) size is the size of the sliding window that moves across the input image during the convolution operation. Common kernel sizes are 3x3, 5x5, and 7x7, but other sizes can be used as well.

    3. `Stride`: The stride is the step size at which the kernel moves across the input. A stride of 1 means the kernel moves one pixel at a time, a stride of 2 means it moves two pixels at a time, and so on.

    4. `Padding`: Padding is the process of adding extra pixels around the input image to preserve its spatial dimensions after convolution. This is useful to avoid shrinking the feature maps too quickly and losing important information at the edges.

+ Code Example

    ```
    conv1 =nn.Conv2d(3, 6 ,5)
    pool = nn.MaxPool2d(2,2)
    conv2 = nn.Conv2d(6, 16 ,5)

    print(image.shape)
    x = conv1(images)
    print(x.shape) 
    x=pool(x)
    print(x.shape)
    x=conv2(x)
    print(x.shape)
    x = pool(x)
    print(x.shape)
    ```
+ Function Intro:
    1. `nn.Conv2d(in_channels, out_channels, kernel_size)`

        `in_channels`: This parameter specifies the number of input channels. In the code snippet, the input to conv1 has 3 channels, indicating a color image with Red, Green, and Blue channels.

        `out_channels`: This parameter specifies the number of output channels (also known as filters or feature maps). In the code snippet, conv1 will produce 6 output channels.

        `kernel_size`: This parameter specifies the size of the convolutional kernel (filter). In the code snippet, the kernel size for both conv1 and conv2 is set to 5x5.

    So, in summary, the nn.Conv2d function defines a 2D convolutional layer that takes input with 3 channels, applies 6 filters of size 5x5, and produces 6 output channels (feature maps).

    2. `nn.MaxPool2d(kernel_size, stride)`

        `kernel_size`: This parameter specifies the size of the max-pooling window. In the code snippet, a max-pooling window of size 2x2 is used.

        `stride`: This parameter specifies the stride of the max-pooling operation. In the code snippet, a stride of 2 is used, meaning the max-pooling window will move 2 pixels at a time.
        The max-pooling operation reduces the spatial dimensions of the input feature maps, effectively downsampling the data and capturing the most important information. Max-pooling helps in reducing the computational complexity and the number of parameters in the network while retaining the most salient features.
+ output: 
    ```
    torch.Size([4, 3, 32, 32])
    torch.Size([4, 6, 28, 28]) # (32-5+0)/1+1 =28
    torch.Size([4, 6, 14, 14]) # (28-2+0)/2 +1 =14
    torch.Size([4, 16, 10, 10])
    torch.Size([4, 16, 5, 5]) 
    ```
+ Size Conculation
    1. `conv layer`
        ```
        (W-F +2P)/S +1
        ```
        Example: 5x5 input, 3x3 filter, padding=0, stride=1

        (5-3+0)/1+1 =  -> 3x3
    
    2. `pooling layer`

        With kernel size 2 by 2 and a stride of 2 
        ,will reduce image by a factor of 2

## Problems

+ [SSL](https://ithelp.ithome.com.tw/articles/10230087) error ( dataset download )

  + Sol
    ```
    import ssl
    ssl._create_default_https_context = ssl_create_unverified_context
    ```
+ package error (連結了多個 OpenMP 執行時函式庫 (libiomp5md.dll))
  + Sol

    1. update package ( better )
       ```
       pip install --upgrade <package>
       ```

    2. setting environment ( bad )
       ```
       import os
       os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
       ```

## Reference

[CNN Intro](https://medium.com/jameslearningnote/%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90-%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92-%E7%AC%AC5-1%E8%AC%9B-%E5%8D%B7%E7%A9%8D%E7%A5%9E%E7%B6%93%E7%B6%B2%E7%B5%A1%E4%BB%8B%E7%B4%B9-convolutional-neural-network-4f8249d65d4f)

[Full Intro](https://cs231n.github.io/convolutional-networks/)

[How Do Convolutional Layers Work in Deep Learning Neural Networks?](https://machinelearningmastery.com/convolutional-layers-for-deep-learning-neural-networks/)