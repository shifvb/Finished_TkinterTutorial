import tkinter as tk


class App(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hello World Object-Oriented Style")
        self.root.geometry("640x480+0+0")
        self.btn = tk.Button(self.root, text="click me!", command=self.btn_callback)
        self.btn.pack()
        self.root.mainloop()

    def btn_callback(self):
        print("Hello world!")


if __name__ == '__main__':
    App()
