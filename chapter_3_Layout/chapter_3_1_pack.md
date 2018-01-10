###`tkinter`支持三种布局管理方式`pack`，`grid`和`place`

---------------------

1.

`pack`类似于浏览器中的流式布局，不需要指定具体位置而是自适应排列控件。

如果使用`pack()`时不加任何参数，那么就会垂直排列，并且每个控件都水平居中。

    label_1 = tk.Label(root, text="communism", bg="#ff9999")
    label_1.pack()
    label_2 = tk.Label(root, text="socialism", bg="cyan")
    label_2.pack()
    label_3 = tk.Label(root, text="capitalism", bg="#9999ff")
    label_3.pack()

![](static/d2b9da6d207cdd35b48e27d39708eb77.png)


2. `fill`参数

使用`fill`参数可以将每个控件的宽度统一。

在上文垂直排列的情况下，设定`fill=tk.X`可以将每个控件的宽度充满父控件(root，宽度预设为320)

    label_1 = tk.Label(root, text="communism", bg="#ff9999")
    label_1.pack(fill=tk.X)
    label_2 = tk.Label(root, text="socialism", bg="cyan")
    label_2.pack(fill=tk.X)
    label_3 = tk.Label(root, text="capitalism", bg="#9999ff")
    label_3.pack(fill=tk.X)

![](static/459007b6ab6ad5127cdf7b7822dab9bf.png)

3. `side`参数

使用`side`参数可以改变控件的排列方式

`side`参数有4种：`tk.TOP`, `tk.BOTTOM`, `tk.LEFT`和`tk.RIGHT`,默认为`tk.TOP`

仅给出从左到右排列(`tk.LEFT`)的代码

    label_1 = tk.Label(root, text="communism(LEFT)", bg="#ff9999")
    label_1.pack(side=tk.LEFT)
    label_2 = tk.Label(root, text="socialism(LEFT)", bg="cyan")
    label_2.pack(side=tk.LEFT)
    label_3 = tk.Label(root, text="capitalism(LEFT)", bg="#9999ff")
    label_3.pack(side=tk.LEFT)
    
![](static/defb494020769e29640c40d95bc0a06e.png)





