### place布局

--------------------

使用`place`布局直接指定控件相对于父控件的位置。不建议使用。

    label_1 = tk.Label(root, text="communism", bg="#ff9999")
    label_1.place(x=30, y=100)
    label_2 = tk.Label(root, text="socialism", bg="cyan")
    label_2.place(x=110, y=20)
    label_3 = tk.Label(root, text="capitalism", bg="#9999ff")
    label_3.place(x=10, y=10, width=100, height=100)

![](static/3ffdc1c018b4dd37134123854c21eb35.png)