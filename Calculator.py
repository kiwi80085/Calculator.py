from tkinter import *
import math
import random
import tkinter as tk
from tkinter import messagebox

class Main(Frame):
    before = None
    history_list = []

    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula,
                         font=("Times New Roman", 30, "bold"),
                         bg="#000", foreground="#FFF")
        self.lbl.place(x=11, y=50)

        btns = [
            "AC", "n^2", "sqrt", "n!", 'DEL',
            "sin", "1", "2", "3", '/',
            "cos", "4", "5", "6", '*',
            "tan", "7", "8", "9", '-',
            "ctg", "(", "0", ")", '+',
            "ran", 'pi', '.', '=', 'e^n'
        ]

        x = 10
        y = 140
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="black", fg='white',
                   font=("Times New Roman", 30),
                   command=com).place(x=x, y=y,
                                      width=115,
                                      height=79)
            x += 117
            if x > 500:
                x = 10
                y += 81

    # History Window
        def create_history_window():
            hist_window = tk.Toplevel(root)
            hist_window.title('History')
            label = tk.Label(hist_window, text='').place(x=260, y=10, height=20)
            hist_window.geometry("300x329+500+200")
            lbox = Listbox(hist_window, width=600, height=629, selectmode=EXTENDED)
            lbox.pack(side=LEFT)
            scroll = Scrollbar(hist_window, command=lbox.yview)
            scroll.pack(side=RIGHT, fill=Y)

            for i in self.history_list:
                lbox.insert(END, f'# {i}')

        self.panel = Frame(root)
        self.HistButton = Button(self.panel, text="History", fg='black',
                                 font=("Roboto", 12, 'bold'),
                                 command=create_history_window)
        self.panel.pack(fill=X, padx=260, pady=4)
        self.HistButton.pack()

    # LOGIC
    def logicalc(self, operation):
        try:
            if operation == "AC":
                self.formula = ""
            elif operation == "DEL":
                self.formula = self.formula[0:-1]
            elif operation == "n^2":
                self.before = self.formula
                self.formula = str((eval(self.before))**2)
                self.history_list.append(f'{self.before}^2 = {self.formula}')
            elif operation == "=":
                self.before = self.formula
                self.formula = str(eval(self.before))
                self.history_list.append(f'{self.before} = {self.formula}')
            elif operation == 'sin':
                self.before = self.formula
                self.formula = str(math.sin(float(self.before)))
                self.history_list.append(f'sin({self.before}) = {self.formula}')
            elif operation == 'cos':
                self.before = self.formula
                self.formula = str(math.cos(float(self.before)))
                self.history_list.append(f'cos({self.before}) = {self.formula}')
            elif operation =='n!':
                self.before = self.formula
                self.formula = str(math.factorial(int(self.before)))
                self.history_list.append(f'({self.before})! = {self.formula}')
            elif operation =='e^n':
                self.before = self.formula
                self.formula = str(math.exp(float(self.before)))
                self.history_list.append(f'e^({self.before}) = {self.formula}')
            elif operation =='sqrt':
                self.before = self.formula
                self.formula = str(math.sqrt(float(self.before)))
                self.history_list.append(f'sqrt({self.before}) = {self.formula}')
            elif operation == 'tan':
                self.before = self.formula
                self.formula = str(math.tan(float(self.before)))
                self.history_list.append(f'tan({self.before}) = {self.formula}')
            elif operation == 'ctg':
                self.before = self.formula
                self.formula = str(math.cos(float(self.before))/math.sin(float(self.before)))
                self.history_list.append(f'ctg({self.before}) = {self.formula}')
            elif operation == 'pi':
                self.formula = str(math.pi)
            elif operation == 'ran':
                self.formula = str(round(random.uniform(0, 1),7))

            else:
                if self.formula == "0":
                    self.formula = ""
                self.formula += operation
            self.update()
        except ZeroDivisionError:
            messagebox.showerror("ERROR", 'DIVIDING BY ZERO IS UNACCEPTABLE!')
        except SyntaxError:
            messagebox.showerror("ERROR", 'CHECK YOUR SYNTAX')


    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "orange"
    root.geometry("600x629+800+200")
    root.title("Simple Calculator")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()