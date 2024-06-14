from customtkinter import *
from datetime import datetime 


app = CTk()
app.geometry('400x400')
app.title('Calculator')

set_appearance_mode('dark')
set_default_color_theme("theme.json")

entry = CTkEntry(master=app, width=400, height=100, font=(None,50),state='disabled')
entry.pack()
frame = CTkFrame(master=app,width=400,height=300)
frame.pack()

def calc(exp):
    exp=exp.replace('x','*').replace('÷','/')
    try:
        resp = eval(exp)
        return resp 
    except:
        return 'Error'

def getButton(val):
    btn = val.cget('text')
    entry.configure(state='normal')
    if btn == 'C':
        current_text = entry.get()
        entry.delete(0,'end')
        entry.insert('end',current_text[:-1])
    elif btn == 'AC':
        entry.delete(0,'end')
        btnEq.configure(text='C')
    elif btn == '=':
        if entry.get()[-1] not in ['+','-','x','÷']:
            exp = entry.get()
            response = calc(exp)
            entry.delete(0,'end')
            entry.insert('end',response)
            btnEq.configure(text='AC')
    elif btn in ['+','-','x','÷']:
        current_text = entry.get()
        last_var = current_text[-1]
        if last_var in ['+','-','x','÷']:
            entry.delete(0, 'end')
            entry.insert('end', current_text[:-1] + btn)
        else:
            entry.delete(0, 'end')
            entry.insert('end', current_text + btn)
    else:
        current_text = entry.get()
        if current_text == 'Error':
            current_text = ''
        entry.delete(0, 'end')
        entry.insert('end', current_text + btn)
    entry.configure(state='disabled')


btn = CTkButton(master=frame, text='1',width=80,height=55, border_color='#292929')
btn.configure(command = lambda val=btn: getButton(val))
btn.grid(row=0,column=0,padx=10, pady=10)
btn = CTkButton(master=frame, text='2',width=80,height=55, border_color='#292929')
btn.configure(command = lambda val=btn: getButton(val))
btn.grid(row=0,column=1,padx=10, pady=10)
btn = CTkButton(master=frame, text='3',width=80,height=55, border_color='#292929')
btn.configure(command = lambda val=btn: getButton(val))
btn.grid(row=0,column=2,padx=10, pady=10)
btn = CTkButton(master=frame, text='+',width=80,height=55)
btn.configure(command = lambda val=btn: getButton(val))
btn.grid(row=0,column=3,padx=10, pady=10)
btn = CTkButton(master=frame, text='4',width=80,height=55, border_color='#292929')
btn.configure(command = lambda val=btn: getButton(val))
btn.grid(row=1,column=0,padx=10, pady=10)
btn = CTkButton(master=frame, text='5',width=80,height=55, border_color='#292929')
btn.configure(command = lambda val=btn: getButton(val))
btn.grid(row=1,column=1,padx=10, pady=10)
btn = CTkButton(master=frame, text='6',width=80,height=55, border_color='#292929')
btn.configure(command = lambda val=btn: getButton(val))
btn.grid(row=1,column=2,padx=10, pady=10)
btn = CTkButton(master=frame, text='-',width=80,height=55)
btn.configure(command = lambda val=btn: getButton(val))
btn.grid(row=1,column=3,padx=10, pady=10)
btn = CTkButton(master=frame, text='7',width=80,height=55, border_color='#292929')
btn.configure(command = lambda val=btn: getButton(val))
btn.grid(row=2,column=0,padx=10, pady=10)
btn = CTkButton(master=frame, text='8',width=80,height=55, border_color='#292929')
btn.configure(command = lambda val=btn: getButton(val))
btn.grid(row=2,column=1,padx=10, pady=10)
btn = CTkButton(master=frame, text='9',width=80,height=55, border_color='#292929')
btn.configure(command = lambda val=btn: getButton(val))
btn.grid(row=2,column=2,padx=10, pady=10)
btn = CTkButton(master=frame, text='x',width=80,height=55)
btn.configure(command = lambda val=btn: getButton(val))
btn.grid(row=2,column=3,padx=10, pady=10)
btn = CTkButton(master=frame, text='0',width=80,height=55, border_color='#292929')
btn.configure(command = lambda val=btn: getButton(val))
btn.grid(row=3,column=0,padx=10, pady=10)

btnEq = CTkButton(master=frame, text='C',width=80,height=55)
btnEq.configure(command = lambda val=btnEq: getButton(val))
btnEq.grid(row=3,column=1,padx=10, pady=10)

btn = CTkButton(master=frame, text='=',width=80,height=55)
btn.configure(command = lambda val=btn: getButton(val))
btn.grid(row=3,column=2,padx=10, pady=10)
btn = CTkButton(master=frame, text='÷',width=80,height=55)
btn.configure(command = lambda val=btn: getButton(val))
btn.grid(row=3,column=3,padx=10, pady=10)

#frame.configure(height=200)

app.mainloop()