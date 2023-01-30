from tkinter import *  
  
  
window = Tk()  
window.title("Добро пожаловать в информационную систему Образование")
window.geometry('640x480')  
menu = Menu(window)  
new_item = Menu(menu)  
new_item.add_command(label='Новый')  
new_item.add_separator()  
new_item.add_command(label='Изменить')  
menu.add_cascade(label='Файл', menu=new_item)  
window.config(menu=menu)  
window.mainloop()