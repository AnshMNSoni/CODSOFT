from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import json


FONT = ('Courier', 16, 'normal')
THEME = '#1C1678'

class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title('Contact Book')
        self.window.config(height=700, width=500, bg=THEME)
        self.row = 50
        self.button_lst = []
        self.new_data = {}
        self.user_number = None
        self.search_number = None
        
        
        # Add Button:
        self.plus_img = PhotoImage(file='./add.png')
        self.plus_button = Button(image=self.plus_img, bg=THEME, command=self.get_user_input)
        self.plus_button.place(x=400, y=600)

        
        # Add Number of list available:
        self.num_list = Label(text="Contact's :: 0", bg=THEME, fg='white', font=('Courier', 16, 'bold'))
        self.num_list.place(x=0, y=0)
            
        
        # Search Button:
        self.search = Button(text='Search', command=self.search_contact, bg=THEME, fg='white', font=('Courier', 16, 'bold'))
        self.search.place(x=394, y=0)
         
            
        self.window.mainloop()


    def get_user_input(self):
        self.username = simpledialog.askstring("Input", "Enter Name here:")
        self.user_number = simpledialog.askinteger("Input", "Enter number here:")
        

        if (self.username.isnumeric() == False and (str(self.user_number).isnumeric() == True and len(str(self.user_number)) == 10)):
            self.user_input = f"{self.username} {self.user_number}"
            
            self.var = IntVar()
            self.check_button = Checkbutton(self.window, text=self.user_input, variable=self.var, font=('Courier', 16, 'bold'), fg='#FFF9D0', bg=THEME, command=self.delete)
            self.check_button.place(x=0, y=self.row)
    
            self.button_lst.append((self.var, self.check_button))
            self.update_contact()
            
            self.save_file()
            
            self.row += 50
            
        else:
            if (self.username.isnumeric() == True):
                messagebox.showinfo(title='⚠️ Warning ⚠️', message='Username must be Name')
            elif (len(str(self.username)) != 10):
                messagebox.showinfo(title='⚠️ Warning ⚠️', message='10-digit phone number missing')
            else:
                messagebox.showinfo(title='⚠️ Warning ⚠️', message='Field must not be empty')
                
            
    def delete(self):
        for items in self.button_lst:
            if (items[0].get() == 1):
                items[1].destroy()
                self.button_lst.remove(items)
                self.reposition_button()
                self.update_contact()
            
            
    def reposition_button(self):
        self.row = 50
        for check_button in self.button_lst:
            check_button[1].place(x=0, y=self.row)
            self.row += 50
            
            
    def update_contact(self):
        self.num_list.config(text=f"Contact's :: {len(self.button_lst)}")
        
        
    def save_file(self):
        self.new_data.update({self.user_number:self.username})
    
    
    def search_contact(self):
        self.search_number = simpledialog.askinteger("Input", "Enter number here:")
        
        try:
            if (self.new_data[self.search_number] != None):
                messagebox.showinfo(title='Info', message=f"Name: {self.new_data[self.search_number]}\nNumber: {self.search_number}")
            
        except KeyError:
            messagebox.showinfo(title='Oops..', message='Contact Not Found')
            
            
GUI()