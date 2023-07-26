# Backpropagation

## Expain

+ 誤差反向傳播

+ 與最優化方法 (如梯度下降法) 結合使用

+ 對網路中所有權重計算損失函數的梯度，反饋給最優化方法，用來更新權值以最小化損失函數。

+ 被認為是一種監督式學習的方法，對每層迭代計算梯度

---

1. Forward pass : Compute Loss

2. Compute local gradi

3. Backward pass : Compute

    + dloss/dWeight using the Chain rule

## Local gradents

+ `x*y=z`
+ `x=dy/dx`
+ `y=dz/dx`

## Loss function

+ `dloss/dx=dloss/dz*dz/dx`

+ [example & explain](./main.py)
