from tkinter import*
from tkinter import messagebox
root = Tk()

def replace_text(text):
    entry.delete(0, END)
    entry.insert(0, text)

def entry_Append(text):
    entryText = entry.get()
    text_length = len(entryText)
    if entryText == '0':
        replace_text(text)
    else:
        entry.insert(text_length,text)

def clear_text(text):
    replace_text(text)

def delete_text():
    entry_text = entry.get()
    text_length = len(entry_text)
    entry.delete(text_length-1,END)

def calculate():
    try:
        entrytext = entry.get()
        result = str(eval(entrytext))
        clear_text(result)
    except Exception:
        clear_text('Invalid Operation')

def calc_exit():
    prompt = messagebox.askquestion('Exit', 'Do you want to exit?')
    if prompt == 'yes':
        exit()

#***************************NUMBERS***************************
button_one = Button(root, text ='1',font = 'Helvetica 20', command = lambda: entry_Append('1'))
button_one.grid(row =4,column =0,sticky =W+E+N+S, padx =2, pady =2)

button_two = Button(root, text ='2',font = 'Helvetica 20', command =lambda: entry_Append('2'))
button_two.grid(row =4,column =1,sticky =W+E+N+S, padx =2, pady =2)

button_three = Button(root, text ='3',font = 'Helvetica 20', command =lambda: entry_Append('3'))
grid = button_three.grid(row=4, column=2, sticky =W+E+N+S, padx =2, pady =2)

button_four = Button(root, text ='4',font = 'Helvetica 20', command =lambda: entry_Append('4'))
button_four.grid(row =3,column =0,sticky =W+E+N+S, padx =2, pady =2)

button_five = Button(root, text ='5',font = 'Helvetica 20', command =lambda: entry_Append('5'))
button_five.grid(row =3,column =1,sticky =W+E+N+S, padx =2, pady =2)

button_six = Button(root, text ='6',font = 'Helvetica 20', command =lambda: entry_Append('6'))
button_six.grid(row =3,column =2, sticky =W+E+N+S, padx =2, pady =2)

button_seven = Button(root, text ='7',font = 'Helvetica 20', command =lambda: entry_Append('7'))
button_seven.grid(row =2,column =0,sticky =W+E+N+S, padx =2, pady =2)

button_eight = Button(root, text ='8',font = 'Helvetica 20', command =lambda: entry_Append('8'))
button_eight.grid(row =2,column =1,sticky =W+E+N+S, padx =2, pady =2)

button_nine = Button(root, text ='9',font = 'Helvetica 20', command =lambda: entry_Append('9'))
button_nine.grid(row =2,column =2, sticky =W+E+N+S, padx =2, pady =2)

button_zero = Button(root, text ='0',font = 'Helvetica 20', command =lambda: entry_Append('0'))
button_zero.grid(row =5,column =1,sticky =W+E+N+S, padx =2, pady =2)


#***************************OPERATORS***************************
button_add = Button(root, text ='+',font = 'Helvetica 20', command =lambda: entry_Append('+'))
button_add.grid(row =5, column =3, sticky =W+E+N+S, padx =2, pady =2)

button_subtract = Button(root, text ='-',font = 'Helvetica 20', command =lambda: entry_Append('-'))
button_subtract.grid(row =3, column =3, sticky =W+E+N+S, padx =2, pady =2)

button_mult = Button(root,text ='*',font = 'Helvetica 20', command =lambda: entry_Append('*'))
button_mult.grid(row =4, column =3, sticky =W+E+N+S, padx =2, pady =2)

button_divide = Button(root, text='/',font = 'Helvetica 20', command =lambda: entry_Append('/'))
button_divide.grid(row =2, column =3, sticky =W+E+N+S, padx =2, pady =2)

button_equal = Button(root, text ='=',font = 'Helvetica 20', command = lambda: calculate())
button_equal.grid(row =5, column =2, sticky =W+E+N+S, padx =2, pady =2)

button_dot = Button(root, text ='.',font = 'Helvetica 20', command = lambda: entry_Append('.'))
button_dot.grid(row =5, column =0, sticky =W+E+N+S, padx =2, pady =2)

button_clear = Button(root, text ='C',font = 'Helvetica 20', command = lambda: clear_text('0'))
button_clear.grid(row =1, columnspan =2, sticky =W+E, padx =2, pady =2)

button_delete = Button(root, text ='Del',font = 'Helvetica 15', command = lambda: delete_text())
button_delete.grid(row =1, column =2,sticky =W+E+N+S, padx =2, pady =2)

button_exit = Button(root, text ='Exit',font = 'Helvetica 20', command = lambda: calc_exit())
button_exit.grid(row =1, column =3,sticky =W+E+N+S, padx =2, pady =2)

entry = Entry(root,text ='0', font ='Helvetica 20')
entry.insert(0,'0')
entry.grid(row =0,columnspan =4, padx =2, pady =2)

root.title('Calculator')
root.mainloop()
