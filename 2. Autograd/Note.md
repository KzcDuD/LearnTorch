# Autograd

## Keyword

+ `.sum()`: sum of tensor
+ `.item()`: transform tensor to scalar

## Explain

+ 『權重』(Weight)
+ [『梯度』(gradint): 求backward](../5.%20Gradients%20Descent/Note.md)
+ forward
+ backward

## Gradient 梯度

+ 梯度是指多變量函數在某一點的方向導數。
    在一元函數中，梯度就是該函數的一階導數，表示函數在該點的變化率和方向。
    而在多變量函數中，梯度是一個向量，包含各個自變量方向上的偏導數，用來指示函數在該點上升最快的方向。

+ 對於一個多變量函數 f(x1, x2, ..., xn)，其梯度表示為∇f(x1, x2, ..., xn)或grad(f)。
    其中，∇是 nabla 符號，它是一個向量算子，根據不同的坐標系有不同的表示方式。

+ 梯度在優化算法中扮演重要的角色，特別是在機器學習和深度學習中的梯度下降法（Gradient    Descent）。
    在梯度下降中，我們通常使用梯度的反方向（負梯度方向）來更新模型參數，以尋找目標函數的最小值。

[ithome](https://ithelp.ithome.com.tw/articles/10274333)

### Forward Propagation 正向傳播

+ 正向傳播是神經網絡中的一個前向計算過程，它將輸入數據通過一系列層和神經元的權重、偏差和激活函數，計算並產生模型的預測輸出。這是神經網絡中訓練和推理的第一步。

+ 在正向傳播完成後，我們可以根據預測結果來計算模型的損失，並使用反向傳播演算法來更新模型的參數，以使得模型更接近真實的目標輸出。

### Backward Propagation 反向傳播

+ 從輸出層開始，根據損失函數計算神經網絡參數（權重和偏差）的梯度。

+ 通過使用連鎖律（Chain Rule）來將損失在每一層向前傳遞，計算每個參數對損失的貢獻。

---

## Code explain

```python
  x=torch.ones(4,requires_grad=True)
  y=x+2 # Forward
  y.backward() # <- dy/dx
  x.grad
  x.grad.zero_() # <- grad 運算是會疊加的
```

1. `x=torch.ones(4,requires_grad=True)`：這創建了一個包含四個元素且值均為1的PyTorch張量x，並設定requires_grad=True，這樣PyTorch就會記錄對x的操作，以便後續計算梯度。

1. `y=x+2`：這一行定義了一個新的張量y，它是x加上2的結果。這是一個簡單的運算，y的每個元素都是x對應元素的值加2。

1. `y.backward()`：這是關鍵步驟，它計算了y相對於x的梯度。由於y是由x計算而來，這裡的梯度即dy/dx。計算完畢後，梯度值將保存在x.grad中。

1. `x.grad`：這將顯示x的梯度。計算完y.backward()後，梯度值將保存在x.grad中。

1. `x.grad.zero_()`：這一行將梯度值歸零。這是因為在PyTorch中，**梯度是會被累加的**，每次調用backward()方法都會累加梯度值。在進行下一輪的反向傳播之前，通常需要將梯度歸零。
