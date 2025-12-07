from tkinter import *

class Taschenrechner:

    def __init__(self, root) :

        self.root = root
        self.root.title("Taschenrechner")
        self.root.geometry("615x690+400+100")
        self.root.configure(bg = 'pink')

        self.MainFrame= Frame(self.root, bd =18, width = 600, height= 670, relief=RIDGE, bg = 'pink')
        self.MainFrame.grid()
        self.WidgetFrame= Frame(self.MainFrame, bd =18, width = 590, height= 660, relief=RIDGE, bg = 'pink')
        self.WidgetFrame.grid()

        self.lblDisplay = Label(self.WidgetFrame, width =30, height=2, bg='white', font=('arial', 20, 'bold'), anchor='e')
        self.lblDisplay.grid(row =0, column=0, columnspan=4, padx =10, pady=10)

        self.input_button = ""

        self.create_buttons("←",  1, 0)
        self.create_buttons("CE", 1, 1)
        self.create_buttons("C", 1, 2) 
        self.create_buttons("±",  1, 3) 

        
        self.create_buttons("7",  2, 0)
        self.create_buttons("8",  2, 1) 
        self.create_buttons("9",  2, 2)
        self.create_buttons("+",  2, 3) 

        
        self.create_buttons("4",  3, 0)
        self.create_buttons("5",  3, 1)
        self.create_buttons("6", 3, 2)
        self.create_buttons("-",  3, 3) 

        
        self.create_buttons("1",  4, 0)
        self.create_buttons("2",  4, 1)
        self.create_buttons("3",  4, 2)
        self.create_buttons("*",  4, 3)  

        
        self.create_buttons("0",  5, 0)
        self.create_buttons(".",  5, 1)
        self.create_buttons("=",  5, 2)
        self.create_buttons("/",  5, 3) 
    
    def create_buttons(self, text, row, column):
        btnWidget = Button(self.WidgetFrame, text=text, width =6, height =2,  bd=4, bg='dark orchid', font=('arial', 20, 'bold'),
                           command=lambda: self.button_click(text)) 
        btnWidget.grid(row=row, column=column, padx=5, pady=5)

    def  button_click(self, text,):

        if text == "←":
            self.input_button = self.input_button[:-1]
        elif text == "CE":
            self.input_button = ""
        elif text == "C":
            self.input_button = ""

        elif text == "=": 
            try:
                self.input_button = str(eval(self.input_button))
            except:
                self.input_button = "Fehler"
        elif text == "±":
                self.input_button = str(-1 * float(self.input_button))
        
        else:
            self.input_button += text          
        self.lblDisplay.config(text=self.input_button) 

    


root = Tk() 
App  = Taschenrechner(root)
root.mainloop()
