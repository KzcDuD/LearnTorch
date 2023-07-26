# Gradient Descent 梯度下降

## Explain

+ 先任意假設一組權重(W)，每一層的 output 就等於前一層的 input 乘以權重(W)
  即 y = sum(w * x)，這個過程就是 **Forward Propagation**。

+ 我們反推回去(*Backpropagation*)，用『梯度下降法』，逐步調整權重(W)，逼近最佳解，以達到『損失函數最小化』。

+ 不斷循環，直到損失的縮小已經不顯著了，我們就認定那一組權重是最佳解了。

---

1. 隨機初始化參數的值。
2. 計算目標函數對於這些參數的梯度。
3. 根據梯度的方向和學習率（一個控制更新步幅的超參數）來更新參數的值。
4. 重複步驟2和步驟3，直到達到收斂條件或達到一個事先設定的迭代次數。

## Example

[numpy example](./numpy_predict.py)

+ 從X , Y 逼近w 求出 `forward(x)` 預測值

```python
X = np.array([1,2,3,4], dtype=np.float32)`
Y = np.array([2,4,6,8], dtype =np.float32)`
```

[pytorch example](./pytorch_predict.py)

```python
backward() = gradient(X,Y,y_pred)
dw = w.grad
```

## Referance

[ithome Gradient Descent](https://ithelp.ithome.com.tw/articles/10198147)

[梯度最佳解](https://chih-sheng-huang821.medium.com/%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92-%E5%9F%BA%E7%A4%8E%E6%95%B8%E5%AD%B8-%E4%B8%89-%E6%A2%AF%E5%BA%A6%E6%9C%80%E4%BD%B3%E8%A7%A3%E7%9B%B8%E9%97%9C%E7%AE%97%E6%B3%95-gradient-descent-optimization-algorithms-b61ed1478bd7)
