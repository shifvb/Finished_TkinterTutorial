### Scrollbar 

通常滚动条和`tk.Listbox`，`tk.Text`或`tk.Canvas`共同使用。

--------------------------------------

1. 和`tk.Listbox`共同使用
    
    1. 竖直滚动条

        绑定控件`yscrollcommand`为滚动条的`set()`方法，这样控件滚动时，滚动条也会随之变化
        
        绑定滚动条的`command`为控件的`yview()`方法，这样滚动条变化时，控件也会随之变化。
        
        下例使用了`tk.Listbox`作为示范。为了让滚动条足够美观(默认滚动条很短)，使用了`pack`布局。
        
            frame = tk.Frame()
            frame.pack()
            # 声明滚动条
            sb = tk.Scrollbar(frame)
            sb.pack(side=tk.RIGHT, fill=tk.Y)
            # 声明Listbox
            lb = tk.Listbox(frame)
            lb.pack(fill=tk.BOTH)
            [lb.insert(tk.END, _) for _ in range(30)]
            # 绑定事件
            sb.configure(command=lb.yview)
            lb.configure(yscrollcommand=sb.set)
        
        ![](static/4639c9eda1da87ba0c88b9adafbe9d22.png)
        
    2. 水平滚动条
    
        滚动条默认是竖直方向(`tk.VERTICAL`)的，需要设置`orient`为`tk.HORIZONTAL`。
        还需要将`yscrollcommand`改为`xscrollcommand`，`yview`改为`xview`。
        
        此外还需要调整`pack`布局参数使得滚动条合乎常理。滚动条默认没有边框，而`tk.Listbox`默认有边框。
        所以显示外围`tk.Frame`的边框，并隐藏`tk.Listbox`的边框将会更加美观：
        
            frame = tk.Frame(relief=tk.SUNKEN, border=1)
            frame.pack()
            # 声明滚动条
            sb = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
            sb.pack(side=tk.BOTTOM, fill=tk.X)
            # 声明Listbox
            lb = tk.Listbox(frame, border=0)
            lb.pack(fill=tk.BOTH)
            lb.insert(tk.END, "capitalism, socialism, communism and anarchism")
            # 绑定事件
            sb.configure(command=lb.xview)
            lb.configure(xscrollcommand=sb.set)
            
        ![](static/2038eab3f5e6b7a47d192e846c1a2a80.png)
        
    3. 竖直和水平滚动条
        
        当使用两个方向的滚动条的时候，你会发现使用`pack`布局比较复杂(如果)。
        
        所以本例使用了`grid`布局
        

        
        