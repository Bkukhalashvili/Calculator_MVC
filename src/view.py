from tkinter import * 

class View():

    win = Tk()
    
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        #style
        self.win.title('Simple Calculator')
        self.equation = StringVar()
        self.win.resizable(width=False, height=False)
        self.win.configure(bg="#141414")
        #components
        self._make_entry()
        self._make_buttons()


    def _make_entry(self):
        entry = Entry(self.win, justify='right', textvariable=self.equation, bg='#141414', fg='white', font='Calibri 13 bold italic', width=35)
        entry.grid(row=0, columnspan=1000, sticky=W)
        self.equation.set('Enter your expression')
    
    def _make_buttons(self):

        #row 1
        btn_pct = Button(self.win, command=self.controller.percent, text='%')
        btn_pct.config(bg='#2B2D2F', fg='white', font='Calibri 14 bold italic', height=1, width=7)
        btn_pct.grid(row=1, column=0)

        btn_clr = Button(self.win, command=self.controller.clear, text='C')
        btn_clr.config(bg='#2B2D2F', fg='green', font='Calibri 14 bold italic', height=1, width=7)
        btn_clr.grid(row=1, column=1)

        btn_del = Button(self.win, command=self.controller.delete, text='<<')
        btn_del.config(bg='#2B2D2F', fg='green', font='Calibri 14 bold italic', height=1, width=7)
        btn_del.grid(row=1, column=2)

        btn_divide = Button(self.win, command=lambda: self.controller.button_click("/"), text='/')
        btn_divide.config(bg='#2B2D2F', fg='green', font='Calibri 14 bold italic', height=1, width=7)
        btn_divide.grid(row=1, column=3)


        #row 2
        btn_7 = Button(self.win, command=lambda: self.controller.button_click(7), text='7')
        btn_7.config(bg='#2B2D2F', fg='white', font='Calibri 14 bold italic', height=1, width=7)
        btn_7.grid(row=2, column=0)

        btn_8 = Button(self.win, command=lambda: self.controller.button_click(8), text='8')
        btn_8.config(bg='#2B2D2F', fg='white', font='Calibri 14 bold italic', height=1, width=7)
        btn_8.grid(row=2, column=1)

        btn_9 = Button(self.win, command=lambda: self.controller.button_click(9), text='9')
        btn_9.config(bg='#2B2D2F', fg='white', font='Calibri 14 bold italic', height=1, width=7)
        btn_9.grid(row=2, column=2)

        btn_multi = Button(self.win, command=lambda: self.controller.button_click("*"), text='*')
        btn_multi.config(bg='#2B2D2F', fg='green', font='Calibri 14 bold italic', height=1, width=7)
        btn_multi.grid(row=2, column=3)


        #row 3
        btn_4 = Button(self.win, command=lambda: self.controller.button_click(4), text='4')
        btn_4.config(bg='#2B2D2F', fg='white', font='Calibri 14 bold italic', height=1, width=7)
        btn_4.grid(row=3, column=0)

        btn_5 = Button(self.win, command=lambda: self.controller.button_click(5), text='5')
        btn_5.config(bg='#2B2D2F', fg='white', font='Calibri 14 bold italic', height=1, width=7)
        btn_5.grid(row=3, column=1)

        btn_6 = Button(self.win, command=lambda: self.controller.button_click(6), text='6')
        btn_6.config(bg='#2B2D2F', fg='white', font='Calibri 14 bold italic', height=1, width=7)
        btn_6.grid(row=3, column=2)

        btn_minus = Button(self.win, command=lambda: self.controller.button_click("-"), text='-')
        btn_minus.config(bg='#2B2D2F', fg='green', font='Calibri 14 bold italic', height=1, width=7)
        btn_minus.grid(row=3, column=3)
        

        #row 4
        btn_1 = Button(self.win, command=lambda: self.controller.button_click(1), text='1')
        btn_1.config(bg='#2B2D2F', fg='white', font='Calibri 14 bold italic', height=1, width=7)
        btn_1.grid(row=4, column=0)

        btn_2 = Button(self.win, command=lambda: self.controller.button_click(2), text='2')
        btn_2.config(bg='#2B2D2F', fg='white', font='Calibri 14 bold italic', height=1, width=7)
        btn_2.grid(row=4, column=1)

        btn_3 = Button(self.win, command=lambda: self.controller.button_click(3), text='3')
        btn_3.config(bg='#2B2D2F', fg='white', font='Calibri 14 bold italic', height=1, width=7)
        btn_3.grid(row=4, column=2)

        btn_plus = Button(self.win, command=lambda: self.controller.button_click("+"), text='+')
        btn_plus.config(bg='#2B2D2F', fg='green', font='Calibri 14 bold italic', height=1, width=7)
        btn_plus.grid(row=4, column=3)
        

        #row 5
        btn_pom = Button(self.win, command=self.controller.plus_or_minus, text='+/-')
        btn_pom.config(bg='#2B2D2F', fg='white', font='Calibri 14 bold italic', height=1, width=7)
        btn_pom.grid(row=5, column=0)

        btn_0 = Button(self.win, command=lambda: self.controller.button_click(0), text='0')
        btn_0.config(bg='#2B2D2F', fg='white', font='Calibri 14 bold italic', height=1, width=7)
        btn_0.grid(row=5, column=1)

        btn_dot = Button(self.win, command=lambda: self.controller.button_click('.'), text='.')
        btn_dot.config(bg='#2B2D2F', fg='white', font='Calibri 14 bold italic', height=1, width=7)
        btn_dot.grid(row=5, column=2)

        btn_equals = Button(self.win, command=self.controller.equals, text='=')
        btn_equals.config(bg='#2B2D2F', fg='green', font='Calibri 14 bold italic', height=1, width=7)
        btn_equals.grid(row=5, column=3)


    def main(self):
        self.win.mainloop()
