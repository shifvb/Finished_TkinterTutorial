### MessageBoxes

------------------------------

1. `showinfo`， `showwarning`和`showerror`

    `tkinter.messagebox`共有3个`showxxx`的函数:

        tk.Button(root, text="show info", command=lambda: messagebox.showinfo(title="info", message="message")).grid()
        tk.Button(root, text="show warning", command=lambda: messagebox.showwarning(title="warning", message="message")).grid()
        tk.Button(root, text="show error", command=lambda: messagebox.showerror(title="error", message="message")).grid()
    
    ![](static/b265af430fa5d22ccf02cf9cd7949dc3.png)
    
2. `askyesno`，`askokcancel`，`askquestion`，`asktrycancel`和`askyesnocancel`

    `tkinter.messagebox`共有5个`askxxx`的函数
    
    此例和上例不同的是，`askxxx`是有不同返回值的

        tk.Button(root, text="ask yesno", command=lambda: print(messagebox.askyesno(title="yesno", message="message"))).grid()
        tk.Button(root, text="ask okcancel", command=lambda: print(messagebox.askokcancel(title="okcancel", message="message"))).grid()
        tk.Button(root, text="ask question", command=lambda: print(messagebox.askquestion(title="question", message="message"))).grid()
        tk.Button(root, text="ask trycancel", command=lambda: print(messagebox.askretrycancel(title="trycancel", message="message"))).grid()
        tk.Button(root, text="ask yesnocancel", command=lambda: print(messagebox.askyesnocancel(title="yesnocancel", message="message"))).grid()

    ![](static/e0e04697003b26f43c71a1fe1354c988.png)
