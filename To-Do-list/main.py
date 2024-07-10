from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

FONT = ('Courier', 16, 'normal')
THEME = '#FFFFCC'

class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title('TODO list')
        self.window.config(height=700, width=500, bg=THEME)
        self.row = 50
        self.button_lst = []
        
        
        # Todo logo:
        self.todo_img = PhotoImage(file='.//todo_logo.png')
        self.todo_logo = Label(image=self.todo_img, bg=THEME)
        self.todo_logo.place(x=400, y=100)
        
        
        # Add Button:
        self.plus_img = PhotoImage(file='./To-Do-list/add.png')
        self.plus_button = Button(image=self.plus_img, bg=THEME, command=self.get_user_input)
        self.plus_button.place(x=400, y=600)

        
        # Add Number of list available:
        self.num_list = Label(text="TODO's :: 0", bg=THEME, font=('Courier', 12, 'italic'))
        self.num_list.place(x=0, y=0)
            
            
        self.window.mainloop()


    def get_user_input(self):
        self.user_input = simpledialog.askstring("Input", "Please enter your input:")
        
        if (self.user_input != ''):
            self.var = IntVar()
            self.check_button = Checkbutton(self.window, text=self.user_input, variable=self.var, font=FONT, bg=THEME, command=self.delete)
            self.check_button.place(x=0, y=self.row)
    
            self.button_lst.append((self.var, self.check_button))
            self.update_todo_list()
            
            
            self.row += 50
        else:
            messagebox.showinfo(title='⚠️ Warning ⚠️', message='Field must not be empty')
            
    def delete(self):
        for items in self.button_lst:
            if (items[0].get() == 1):
                items[1].destroy()
                self.button_lst.remove(items)
                self.reposition_button()
                self.update_todo_list()

                
    def reposition_button(self):
        self.row = 50
        for check_button in self.button_lst:
            check_button[1].place(x=0, y=self.row)
            self.row += 50
            
            
    def update_todo_list(self):
        self.num_list.config(text=f"TODO's :: {len(self.button_lst)}")

GUI()