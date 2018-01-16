### Text

Text被设计用来显示多行文字。和Entry不同的是，Text中的文字可以以不同的字体、大小显示，还可以显示图片、窗口

-----------------------

1. 设置`width`和`height`属性

    `width`和`height`属性设定了`tk.Text`的宽和高(按字符计)
    
        tk.Text(root, width=30, height=12).pack()
    
    ![](static/0875bc15eee8db9d02928aaa03cdb7c8.png)
    
2. 设置`font`属性

    `font`属性可以改变字体的种类和样式，此外还可以改变字体的大小，从而间接改变`tk.Text`的大小：
    
        tk.Text(root, width=30, height=12, font=tk.font.Font(size=13)).pack()
    
    ![](static/102ee8c0b3fc4647a3030093bc53f9f4.png)

3. 设置`borderwidth`属性

    有时不需要显示`tk.Text`的边框(默认为2像素)
    
        tk.Text(root, width=30, height=12, borderwidth=0).pack()
    
    ![](static/e1ce45307dcf124bec209c82c8e8660e.png)
    

4. `bg`和`fg`属性

    有时需要设置前景色`fg`和背景色`bg`
    
        tk.Text(root, width=30, height=12, bg="black", fg="#16c60c", font=tk.font.Font(size=15)).pack()
    
    ![](static/5a1254c1de0c308d51fe97c18ba64f8d.png)


3. 索引方式

    `tk.Text`的索引方式和`tk.Entry`类似
    
    值得注意的是，line(行索引)从1开始，而column(列索引)和`tk.Entry`相同，从0开始。
    指定越界索引不会报错，而是会“粘”到最近的位置。共有11种索引类型：
    
        "{line}.{column}"
        "{line}.end"
        tk.INSERT
        tk.CURRENT
        tk.END
        用户定义的marks
        用户定义的tags("tag.first", "tag.last")
        selection(SEL_FIRST, SEL_LAST)
        窗口坐标("@x,y")
        嵌入对象(窗口，对象)的名称
        表达式
        
    "{line}.{column}"是最基本的索引方式。
    
        text = tk.Text(root, width=30, height=12)
        text.pack()
        text.insert("1.0", "capitalism,socialism\ncommunism and anarchism")
        # 按钮回调函数
        def btn_callback(*args):
            text.insert("1.2", "*")
        tk.Button(root, text="insert at \"1.2\" (row 0, column 2)", command=btn_callback).pack()
        
    ![](static/b26921f0bbd649ee57b3a825b04fe674.gif)
    


