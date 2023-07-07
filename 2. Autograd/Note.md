# Autograd

## Explain

+ 『權重』(Weight)
+ [『梯度』(gradint): 求backward](../5.%20Gradients%20Descent/Note.md)
+ forward
+ backward

## Gradient 計算

[ithome](https://ithelp.ithome.com.tw/articles/10274333)

### forward *+-x/*

`eg: y=x+2`

### backward *du/dx*

+ `x=torch.ones(4,requires_grad=True)`
+ `y.backward()` <- dy/dx
+ `x.grad`
+ `x.grad.zero_()` <- grad 運算是會疊加的
