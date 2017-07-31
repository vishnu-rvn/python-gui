from tkinter import*
from tkinter import messagebox
textEditor = Tk()

def exitApp():
    prompt = messagebox.askquestion('Exit?','Do you want to exit?')
    if prompt == 'yes':
        exit()
menubar = Menu(textEditor)
filemenu = Menu(menubar, tearoff =0)
filemenu.add_command(label ='New')
filemenu.add_command(label ='Open')
filemenu.add_command(label ='Save')
filemenu.add_separator()
filemenu.add_command(label ='Exit',command =lambda:exitApp())
menubar.add_cascade(label ='File',menu =filemenu)

editmenu = Menu(menubar, tearoff =0)
editmenu.add_command(label ='Cut')
editmenu.add_command(label ='Copy')
menubar.add_cascade(label ='Edit', menu =editmenu)

sizesList = [8, 10, 12, 13, 14, 16, 18, 22, 26, 32, 40]
var = IntVar()
var.set(8)
dropdown = OptionMenu(textEditor,var, *sizesList)
dropdown.grid(sticky =W)

textEditor.config(menu =menubar)
text = Text(textEditor)
text.grid()
textEditor.geometry('500x400')
textEditor.mainloop()