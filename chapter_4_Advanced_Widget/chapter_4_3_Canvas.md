### Canvas

Canvas可用于创建各种自定义控件

------------------

1. 声明一个`tk.Canvas`

    `tk.Canvas`默认没有任何样式

        canvas = tk.Canvas(root, width=320, height=240)
        canvas.pack()
        
    ![](static/a521da8a328dd198ab074a15738f29e1.jpg)
    

2. 使用`create_xxx()`方法在`tk.Canvas`对象上描绘图形

    1. 使用`create_line()`绘制直线或折线
        
        查看源码可得方法声明：
        
            def create_line(self, *args, **kw):
                """Create line with coordinates x1,y1,...,xn,yn."""
                return self._create('line', args, kw) 
                
        那么只要指定相应的`x1`，`y1`，`x2`，`y2`即可描出一条直线(多指定即是折线)。
        可以使用`fill`参数（而不是`color`）指定绘制颜色，`width`指定绘制宽度：
        
            canvas = tk.Canvas(root, width=320, height=240)
            canvas.pack()
            canvas.create_line(50, 50, 100, 100, fill="#aaaaaa", width=3)
        
        ![](static/ab19e225768ed6bcd4f083e3eebde8a9.png)
    
    2. 使用`create_rectangle()`方法绘制矩形
    
        查看源码可得方法声明：
        
            def create_rectangle(self, *args, **kw):
                """Create rectangle with coordinates x1,y1,x2,y2."""
                return self._create('rectangle', args, kw)
    
        那么只要指定相应的矩形左上角`x1`，`y1`坐标和右下角`x2`，`y2`坐标即可。
        可以使用`outline`参数指定边框颜色，`width`参数指定边框宽度，
        而`fill`参数指定填充颜色(默认透明)
        
            canvas = tk.Canvas(root, width=320, height=240)
            canvas.pack()
            canvas.create_rectangle(50, 50, 100, 100, outline="cyan", fill="#aaaaaa", width=3)
        
        ![](static/499771305abad3188e4de3ead10bde00.png)
    
    3. 使用`create_polygon()`方法绘制多边形
    
        查看源码可得方法声明：
       
            def create_polygon(self, *args, **kw):
                """Create polygon with coordinates x1,y1,...,xn,yn."""
                return self._create('polygon', args, kw) 
        
        那么指定四个点就可以绘制四边形了。
        可以使用`outline`参数指定边框颜色，`width`参数指定边框宽度，
        而`fill`参数指定填充颜色(默认黑色)
        
            canvas = tk.Canvas(root, width=320, height=240)
            canvas.pack()
            canvas.create_polygon(50, 50, 50, 100, 100, 100, 120, 30, outline="cyan", width=3, fill="#aaaaaa")
        
        ![](static/5f63310a71f0fe88fa8aeaf227a481ef.png)
        
    4. 使用`create_oval()`方法绘制椭圆
    
        查看源码可得方法声明：
        
            def create_oval(self, *args, **kw):
                """Create oval with coordinates x1,y1,x2,y2."""
                return self._create('oval', args, kw)
    
        那么只要指定相应包围椭圆的矩形(bounding-box)左上角`x1`，`y1`坐标和右下角`x2`，`y2`坐标即可。
        可以使用`outline`参数指定边框颜色，`width`参数指定边框宽度，
        而`fill`参数指定填充颜色(默认透明)
        
            canvas = tk.Canvas(root, width=320, height=240)
            canvas.pack()
            canvas.create_oval(20, 20, 100, 100, outline="cyan", width=3, fill="#aaaaaa")
   
        ![](static/19f09380f41d50a7e00a8b703b14962e.png)
        
    5. 使用`create_arc()`方法绘制扇形、弦或弧
    
        查看源码可得方法声明：
        
            def create_arc(self, *args, **kw):
                """Create arc shaped region with coordinates x1,y1,x2,y2."""
                return self._create('arc', args, kw)

        和绘制椭圆类似，此方法也指定包围矩形(bounding-box)的左上和右下角坐标。
        不同的是有额外的参数`start`控制起始角度，`extent`控制弧形扫过的角度，
        `style`控制绘制形状：
        
        * `tk.PIESLICE`为扇形(默认)
        * `tk.CHORD`为弦
        * `tk.ARC`为弧
        
        可以使用`outline`参数指定边框颜色，`width`参数指定边框宽度，
        而`fill`参数指定填充颜色(默认透明)
        
            canvas = tk.Canvas(root, width=320, height=240)
            canvas.pack()
            canvas.create_arc(20, 20, 100, 100, start=0, extent=90, style=tk.PIESLICE, outline="cyan", width=3, fill="#999999")
            canvas.create_arc(20, 100, 100, 180, start=0, extent=90, style=tk.CHORD, outline="cyan", width=3, fill="#999999")
            canvas.create_arc(20, 180, 100, 260, start=0, extent=90, style=tk.ARC, outline="cyan", width=3, fill="#999999")
        
        ![](static/47ba6a40070b6ba6d08aedda99383456.png)    