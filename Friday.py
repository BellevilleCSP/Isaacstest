from tkinter import Tk, Label, Button
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Farrar")

        self.label = Label(master, text="Click the button below to see which class is the best.")
        self.label.pack()

        self.greet_button = Button(master, text="Best Class?", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=self.no)
        self.close_button.pack()

    def greet(self):
        print("This class is totally the best")
    def no(self):
        print("HA Farrar will not let you leave D:")
root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
