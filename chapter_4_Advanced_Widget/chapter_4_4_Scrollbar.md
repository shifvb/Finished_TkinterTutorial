### Scrollbar 

通常滚动条和`tk.Listbox`，`tk.Text`或`tk.Canvas`共同使用。

--------------------------------------

1. 使用
    
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
            lb.pack(side=tk.LEFT, fill=tk.BOTH)
            [lb.insert(tk.END, _) for _ in range(30)]
            # 绑定事件
            sb.configure(command=lb.yview)
            lb.configure(yscrollcommand=sb.set)
        
        ![](static/4639c9eda1da87ba0c88b9adafbe9d22.png)
