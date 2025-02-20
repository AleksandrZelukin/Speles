from tkinter import *
import random as rdm


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.startUI()

    def startUI(self):
        btn = Button(root, text="Akmens", font=("Times New Roman", 15),
                     command=lambda x=1: self.btn_click(x))
        btn2 = Button(root, text="Šķeres", font=("Times New Roman", 15),
                      command=lambda x=2: self.btn_click(x))
        btn3 = Button(root, text="Pāpirs", font=("Times New Roman", 15),
                      command=lambda x=3: self.btn_click(x))

        btn.place(x=10, y=100, width=120, height=50)
        btn2.place(x=155, y=100, width=120, height=50)
        btn3.place(x=300, y=100, width=120, height=50)

        self.lbl = Label(root, text="Speles sakums!", bg="#FFF", font=("Times New Roman", 21, "bold"))
        self.lbl.place(x=200, y=25)

        self.win = self.drow = self.lose = 0

        self.lbl2 = Label(root, justify="left", font=("Times New Roman", 13),
                         text=f"Uzvarus: {self.win}\nzaudējas:"
                              f" {self.lose}\nnav uzvaretajus: {self.drow}",
                         bg="#FFF")
        self.lbl2.place(x=5, y=5)

    def btn_click(self, choise):
        comp_choise = rdm.randint(1, 3)

        if choise == comp_choise:
            self.drow += 1
            self.lbl.configure(text="Nav uzvaretaju")
        elif choise == 1 and comp_choise == 2 \
                or choise == 2 and comp_choise == 3 \
                or choise == 3 and comp_choise == 1:
            self.win += 1
            self.lbl.configure(text="Uzvara")
        else:
            self.lose += 1
            self.lbl.configure(text="paspēle")

        self.lbl2.configure(text=f"Uzvarus: {self.win}\npaspēles:"
                              f" {self.lose}\nNav uzvaretajus: {self.drow}")

        del comp_choise


if __name__ == '__main__':
    root = Tk()
    root.geometry("600x160+200+200")
    root.title("Akmens, šķeres, pāpirs")
    root.resizable(False, False)
    root["bg"] = "#FFF"
    app = Main(root)
    app.pack()
    root.mainloop()


