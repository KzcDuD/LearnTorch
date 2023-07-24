# Dataset and DataLoader

## Dataset

### Itro

+ Arranging Data and giving number
+ 獲取每個數據及其Label
+ Sum of Data

### arcitecture

+ Data
+ give Label ,like
  + **floder name**
  + **file name**
  + **use other .txt file**

## Dataloader

+ `package`: 為Network 提供不同數據形式

`dataloader =DataLoader(dataset=dataset , batch_size =4,shuffle =True,num_workers=0)`

+ `num_workers=0`(default) 設>1 GPU Ram 不夠會出錯
