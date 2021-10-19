import tkinter

class myinter:
    window = None
    title = "My Class Window"
    frame = None
    def __init__(self) -> None:
        self.window = tkinter.Tk(title = self.title)
        self.window.title
        self.frame = tkinter.Frame(self.window)
        self.frame.pack()
        print(tkinter.TkVersion)

if __name__ == "__main__":
    try:
        main_win = myinter()

    except:
        print("error")
