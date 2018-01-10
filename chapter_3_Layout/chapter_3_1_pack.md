###`tkinter`支持三种布局管理方式`pack`，`grid`和`place`

---------------------

1. 不使用任何参数

`pack`类似于浏览器中的流式布局，不需要指定具体位置而是自适应排列控件。

如果使用`pack()`时不加任何参数，那么就会垂直排列，并且每个控件都水平居中。

    label_1 = tk.Label(root, text="communism", bg="#ff9999")
    label_1.pack()
    label_2 = tk.Label(root, text="socialism", bg="cyan")
    label_2.pack()
    label_3 = tk.Label(root, text="capitalism", bg="#9999ff")
    label_3.pack()

![](static/d2b9da6d207cdd35b48e27d39708eb77.png)


2. `fill`和`expand`参数

使用`fill`参数可以将每个控件的宽度/高度统一，共三种:`tk.X`，`tk.Y`，`tk.BOTH`

在上文垂直排列的情况下，设定`fill=tk.X`可以将每个控件的宽度充满父控件(root，宽度预设为320)

    label_1 = tk.Label(root, text="communism", bg="#ff9999")
    label_1.pack(fill=tk.X)
    label_2 = tk.Label(root, text="socialism", bg="cyan")
    label_2.pack(fill=tk.X)
    label_3 = tk.Label(root, text="capitalism", bg="#9999ff")
    label_3.pack(fill=tk.X)

![](static/459007b6ab6ad5127cdf7b7822dab9bf.png)

而`expand`属性设置为1的时候，那么控件将尽可能居中，此时可以使用`fill`充填空间

        label_1 = tk.Label(root, text="communism", bg="#ff9999")
        label_1.pack(expand=1, fill=tk.X)
        label_2 = tk.Label(root, text="socialism", bg="cyan")
        label_2.pack(expand=1, fill=tk.Y)
        label_3 = tk.Label(root, text="capitalism", bg="#9999ff")
        label_3.pack(expand=1, fill=tk.BOTH)
        
![](static/d5502512b7e9fea0e90097fcda23540d.png)

3. `side`参数

使用`side`参数可以改变控件的排列方式

`side`参数有4种：`tk.TOP`, `tk.BOTTOM`, `tk.LEFT`和`tk.RIGHT`,默认为`tk.TOP`

    # 仅给出从左到右排列(`tk.LEFT`)的代码
    label_1 = tk.Label(root, text="communism(LEFT)", bg="#ff9999")
    label_1.pack(side=tk.LEFT)
    label_2 = tk.Label(root, text="socialism(LEFT)", bg="cyan")
    label_2.pack(side=tk.LEFT)
    label_3 = tk.Label(root, text="capitalism(LEFT)", bg="#9999ff")
    label_3.pack(side=tk.LEFT)
    
![](static/defb494020769e29640c40d95bc0a06e.png)

4. `padx`, `pady`，`ipadx`，`ipady`参数

`padx`： 类似于CSS中`margin-left` +  `margin-right`，即左外边距和右外边距

`pady`： 类似于CSS中`margin-top` + `margin-bottom`，即上外边距和下外边距

`ipadx`：类似于CSS中`padding-left` + `padding-right`，即左内边距和右内边距

`ipady`：类似于CSS中`padding-top` + `padding-bottom`，即上内边距和下内边距

注意和CSS样式的不同是，margin不会折叠（下例）

    label_1 = tk.Label(root, text="communism", bg="#ff9999")
    label_1.pack(pady=30)
    label_2 = tk.Label(root, text="socialism", bg="cyan")
    label_2.pack(pady=30)
    label_3 = tk.Label(root, text="capitalism", bg="#9999ff")
    label_3.pack()
    
![](static/50f1c0aa00ccdd1ab19c9b3147f70481.png)






