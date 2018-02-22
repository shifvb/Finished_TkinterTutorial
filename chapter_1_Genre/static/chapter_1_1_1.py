import tkinter as tk


def main():
    root = tk.Tk()
    # 设置窗口标题
    root.title("The Hello World Example")
    # 设置窗口大小和位置
    root.geometry("640x480+0+0")

    # 声明一个label
    hello_world_label = tk.Label(root, text="Hello, world!")
    #
    hello_world_label.pack()

    # mainloop
    tk.mainloop()


if __name__ == '__main__':
    main()
