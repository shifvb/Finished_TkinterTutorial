### Event

`tkinter`维护着一个`eventloop`。当用户触发了某事件(亦或其它情景)，此时一个`tk.Event`对象就产生了。

-----------------------------

1. 使用`bind()`方法绑定事件

    1. 使用`bind()`方法捕捉鼠标事件
        
        本例在`tk.Frame`上绑定了`<Button-1>`(即鼠标左键点击)事件到函数`callback()`上。
        
        `<Button-2>`和`<Button-3>`分别对应了鼠标滚轮(如果有)点击和鼠标右键点击，而`<Motion>`对应鼠标移动。
    
            frame = tk.Frame(root, width=320, height=240, bg="cyan")
            frame.pack()
            def callback(event):
                root.title("({}, {}) {}".format(event.x, event.y, event))
            frame.bind("<Button-1>", callback)
        
        ![](static/660f2f9c80dceffefa0046ec1e16d07f.png)
            
    2. 使用`bind()`方法捕捉键盘事件
    
        和捕捉鼠标事件不同的是，键盘事件会传给当前处于`focus`状态的控件，默认是`root`。
        本例中则需要使用`focus_set()`方法将键盘事件导向`frame`。
        
        `<Key>`默认捕捉所有键盘按键，如果需要捕捉特定按键可以更具体一些，比如`<Key-w>`(小写w)，`<Key-Up>`(上方向键)。
        
            frame = tk.Frame(root, width=320, height=240, bg="cyan")
            frame.pack()
            def callback(event):
                root.title("{} {}".format(event.char, event))
            frame.bind("<Key>", callback)
            frame.focus_set()
    
        ![](static/0259ef22e7b8a1ef183886cca9d95a09.png)
        
2. `tk.Event`

    `tk.Event`是一个事件的container。在三种情况下会被创建：
    
    * 鼠标事件`ButtonPress`，`ButtonRelease`，`Motion`，`Enter`，`Leave`，`MouseWheel`
    * 键盘事件`KeyPress`，`KeyRelease`
    * 窗口事件`Visibility`， `Unmap`，`Map`，`Expose`，`FocusIn`，`FocusOut`，`Circulate`，`Colormap`，`Gravity`，
    `Reparent`，`Property`，`Destory`，`Activate`，`Deactivate`
    
    如果用户通过`bind()`，`bind_all()`，`bind_class()`或者`tag_bind()`方法绑定了一个回调函数，
    那么当事件发生时这个回调函数会被调用，且第一个参数是一个`tk.Event`对象。这个对象里有如下常用属性：
    
    * `x`，`y`：当前鼠标坐标
    * `x_root`，`y_root`：当前鼠标绝对坐标
    * `char`：char(仅限键盘事件)
    * `widget`：生成事件的控件
    * `width`, `height`：控件新的高度和宽度(仅限Configure事件)
    
    `tk.Event`源码中有详细介绍，此处不再赘述。

3. 构建`bind()`方法中`sequence`参数

    在`tkinter`的设计中，用户使用一个特殊格式的字符串来描述事件的种类(比如`"<Button-1>"`表示鼠标左键点击)。
    既然了解了`tk.Event`，那么现在可以开始介绍如何构建`sequence`字符串了。
    
    格式为`<MODIFIER-MODIFIER-TYPE-DETAIL>`，其中`TYPE`字段最重要。
    
    * `TYPE`字段可为
    `Activate`, `Enter`, `Map`,`ButtonPress`, `Button`, `Expose`, `Motion`, `ButtonRelease`，`FocusIn`,
    `MouseWheel`, `Circulate`, `FocusOut`, `Property`,`Colormap`, `Gravity Reparent`, `Configure`, `KeyPress`, `Key`,
    `Unmap`, `Deactivate`, `KeyRelease Visibility`, `Destroy`,`Leave`其中之一
    * `MODIFIER`字段可为`Control`, `Mod2`, `M2`, `Shift`, `Mod3`, `M3`, `Lock`, `Mod4`, `M4`,`Button1`, `B1`, `Mod5`,
     `M5`, `Button2`, `B2`, `Meta`, `M`, `Button3`,`B3`, `Alt`, `Button4`, `B4`, `Double`, `Button5`, `B5`, `Triple`,
     `Mod1`, `M1`其中之一
    * `DETAIL`字段可为如下：
        * `ButtonPress`/`ButtonRelease`的number
        * `KeyPress`/`KeyRelease`的keysym(key-symbol)
        
    举个例子，`<Control-Button-1>`就是按住`Control`按键和鼠标左键。
    下面列举一些常用格式
    
    * `<Button-1>`：在控件上按下鼠标左键。1对应左键，2对应滚轮(如果有),3对应右键。
    值得注意的是，如果你需要监听用户释放鼠标左键，那么请使用`<ButtonRelease-1>`。
    此外还有很多等价表达方法。`<Button-1>`，`<ButtonPress-1>`和`<1>`是等价的。
    
    * `<B1-Motion>`：按下鼠标左键且鼠标移动。`<Button1-Motion>`和`<B1-Motion>`等价(请查阅`MODIFIER`字段)。
    
    * `<Double-Button-1>`：双击鼠标左键
    
    * `<Enter>`/`<Leave>`鼠标移入/移出控件(并不是指用户按下回车)
    
    * `<FocusIn>`/`<FocusOut>`具有/取消控件`focus`状态
    
    * `<Return>`是用户按下回车键。其余的特殊键位(请思考这属于`<MODIFIER-MODIFIER-TYPE-DETAIL>`中的哪一类？)如下：
        
        常用键位：
        * `<LEFT>`, `<RIGHT>`，`<Up>`，`<Down>`：小键盘方向键
        * `<Alt_L>`/`<Alt_R>`：左/右Alt键
        * `<Control_L>`/`<Control_R>`：左/右Control键
        * `<Shift_L>`/`<Shift_R>`：左/右Shift键
        
        其它键位：
        * `<BackSpace>`：退格键
        * `<Cancel>`/`<Pause>`：break键/pause键
        * `<End>`/`<Home>`：End键/Home键
        * `<Insert>`/`<Delete>`：Insert键/Delete键
        * `<Num_Lock>`/`<Scroll_Lock>`：NumberLock键/ScrollLock键
        * `<Prior>`/`<Next>`：PageUp键/PageDown键
        * `<Tab>`/`<Caps_Lock>`：Tab键/CapsLk键
        * `<F1>`, `<F2>`...`<F12>`：功能键F1-F12
