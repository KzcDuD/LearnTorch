# Gradient Descent

## Explain

1. 先任意假設一組權重(W)，每一層的 output 就等於前一層的 input 乘以權重(W)
2. 即 y = sum(w * x)，這個過程就是 **Forward Propagation**。
3. 我們反推回去(*Backpropagation*)，用『梯度下降法』，逐步調整權重(W)，逼近最佳解，以達到『損失函數最小化』。
4. 不斷循環，直到損失的縮小已經不顯著了，我們就認定那一組權重是最佳解了。

## Example

[numpy example](./numpy_predict.py)

+ `X = np.array([1,2,3,4], dtype=np.float32)`
+ `Y = np.array([2,4,6,8], dtype =np.float32)`

+ 從X , Y 逼近w 求出 `forward(x)` 預測值

[pytorch example](./pytorch_predict.py)

+ `l.backward() = gradient(X,Y,y_pred)`
+ `dw = w.grad`

## Referance

[ithome Gradient Descent](https://ithelp.ithome.com.tw/articles/10198147)