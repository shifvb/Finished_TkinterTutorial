### grid布局

----------------------------------------------

1. `row`和`column`

    用户必须指定`row`和`column`的值(从0开始)
    
    单元格的宽度由同一列最宽的控件决定。单元格高度由同一行中最高的控件决定。
    
        tk.Button(root, text="communism", width=10, height=2, bg="#ff9999").grid(row=0, column=0)
        tk.Button(root, text="socialism", width=10, height=5, bg="#00ffff").grid(row=0, column=1)
        tk.Button(root, text="capitalism", width=20, height=2, bg="#9999ff").grid(row=1, column=0)
        tk.Button(root, text="anarchism", width=10, height=2, bg="#999999").grid(row=1, column=1)
        
    ![](static/6ad4f1d9264e46372093a1eaf04192b5.png)