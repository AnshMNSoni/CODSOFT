# Basic Calculator:

import tkinter as tk
from tkinter import *
from tkinter import messagebox

FONT = ('Courier', 18, 'bold')

class Calculator:
    def __init__(self):
        self.window = Tk()
        self.window.title('Basic Calculator')
        self.window.config(height=200, width=400)
        
        # number1:
        self.num1 = tk.Entry(font=FONT)
        self.num1.place(x=65, y=80, width=50)
        
        
        # Operation:
        self.symbol = Label(text='', fg='red', font=FONT)
        self.symbol.place(x=120, y=80)
        
        
        # number2:
        self.num2 = tk.Entry(font=FONT)
        self.num2.place(x=145, y=80, width=50)
        
        # Equal to:
        self.equal = Label(text='=', fg='red', font=FONT)
        self.equal.place(x=205, y=80)
        
        # Result:
        self.answer = Label(text='', fg='black', font=FONT)
        self.answer.place(x=235, y=80)
        
        # Calculate Button:
        self.button =  Button(text='Calculate', font=('Courier', 12, 'italic'), command=self.Calculation)
        self.button.place(x=235, y=120)
        
        # Summation Button:
        self.sum = Button(text='+', fg='blue', font=FONT, command=self.Summation)
        self.sum.place(x=55, y=0)
        
        # Subtraction Button:
        self.sub = Button(text='-', fg='blue', font=FONT, command=self.Subtraction)
        self.sub.place(x=95, y=0)
        
        # Multiplication Button:
        self.mul = Button(text='x', fg='blue', font=FONT, command=self.Multiplication)
        self.mul.place(x=135, y=0)
        
        # Division:
        self.div = Button(text='/', fg='blue', font=FONT, command=self.Division)
        self.div.place(x=175, y=0)
        
        # Power:
        self.power = Button(text='^', fg='blue', font=FONT, command=self.Power)
        self.power.place(x=215, y=0)
        
        # Modulus:
        self.remainder = Button(text='%', fg='blue', font=FONT, command=self.Modulus)
        self.remainder.place(x=255, y=0)
        
        
        self.window.mainloop()
        
    def Summation(self):
        self.symbol.config(text='+')
    
    
    def Subtraction(self):
        self.symbol.config(text='-')
    
    
    def Multiplication(self):
        self.symbol.config(text='x')
        
        
    def Division(self):
        self.symbol.config(text='/')
        
        
    def Power(self):
        self.symbol.config(text='^')
        
        
    def Modulus(self):
        self.symbol.config(text='%')
    
    def final_answer(self):
        self.answer.config(text=str(self.result))
        
    def Calculation(self):
        self.user = self.symbol['text']
        
        try:
            if (self.user == '+'):
                self.Summation()
                self.result = float(self.num1.get()) + float(self.num2.get())
                self.final_answer()
                
            elif (self.user == '-'):
                self.Subtraction()
                self.result = float(self.num1.get()) - float(self.num2.get())
                self.final_answer()
                
            elif (self.user == 'x'):
                self.Multiplication()
                self.result = float(self.num1.get()) * float(self.num2.get())
                self.final_answer()
            
            elif (self.user == '/'):
                self.Multiplication()
                self.result = float(self.num1.get()) / float(self.num2.get())
                self.final_answer()
                
            elif (self.user == '^'):
                self.Multiplication()
                self.result = pow(float(self.num1.get()), float(self.num2.get()))
                self.final_answer()
                
            elif (self.user == '%'):
                self.Multiplication()
                self.result = float(self.num1.get()) % float(self.num2.get())
                self.final_answer()
                
        except ValueError:
            messagebox.showinfo(title='⚠️ Warning ⚠️', message='Something went Wrong.')
            
Calculator()