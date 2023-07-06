# Autograd

## Gradient 計算

[ithome](https://ithelp.ithome.com.tw/articles/10274333)

### forward *+-x/*

+ 進行運算  `eg: y=x+2`

### backward *du/dx*

+ `x=torch.ones(4,requires_grad=True)`
+ `y.backward()` <- dy/dx
+ `x.grad`
+ `x.grad.zero_()` <- grad 運算是會疊加的
