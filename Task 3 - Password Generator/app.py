from customtkinter import *
from datetime import datetime 
import random
import string

app = CTk()
app.geometry('538x400')
app.title('Password Generator')

set_appearance_mode('dark')
set_default_color_theme("theme.json")


s=16
u=13
l=13
d=5

def getSlider(value, btn, label):
    global s,u,l,d
    value=int(value)
    what = label.cget('text')
    if what == 'Special Characters':
        s = value 
    elif what == 'Upper Case Letters':
        u = value 
    elif what == 'Lower Case Letters':
        l = value 
    else:
        d=value

    btn.configure(text=value)

def genPassword():
    randoms = []
    [randoms.append(_) for _ in [ random.choice(string.punctuation) for _ in range(s) ]]
    [randoms.append(_) for _ in [ random.choice(string.ascii_uppercase) for _ in range(u) ]]
    [randoms.append(_) for _ in [ random.choice(string.ascii_lowercase) for _ in range(l) ]]
    [randoms.append(_) for _ in [ random.choice(string.digits) for _ in range(d) ]]
    random.shuffle(randoms)
    password=''.join(randoms)
    entry.delete(0,'end')
    entry.insert('end',password)

entry = CTkEntry(master=app, width=538, height=100, font=(None,20))
entry.pack()
frame = CTkFrame(master=app,width=538,height=300)
frame.pack()

label = CTkLabel(frame, text='Special Characters', font=(None,16))
label.grid(row=0,column=0,padx=10,pady=10)
slider = CTkSlider(frame, from_=0, to=32,number_of_steps=32)
slider.grid(row=0,column=1,padx=10,pady=10)
btn = CTkButton(frame,text=slider.get() , state='disabled',border_color='#1c1c1c',text_color_disabled='#57c8ff')
btn.grid(row=0, column=2, padx = 10, pady=10)
slider.configure(command=lambda value, button=btn,label=label: getSlider(value,button,label))

label = CTkLabel(frame, text='Upper Case Letters', font=(None,16))
label.grid(row=1,column=0,padx=10,pady=10)
slider = CTkSlider(frame, from_=0, to=26,number_of_steps=26)
slider.grid(row=1,column=1,padx=10,pady=10)
btn = CTkButton(frame,text=slider.get() , state='disabled',border_color='#1c1c1c',text_color_disabled='#57c8ff')
btn.grid(row=1, column=2, padx=10, pady=10)
slider.configure(command=lambda value, button=btn,label=label: getSlider(value,button,label))

label = CTkLabel(frame, text='Lower Case Letters', font=(None,16))
label.grid(row=2,column=0,padx=10,pady=10)
slider = CTkSlider(frame, from_=0, to=26,number_of_steps=26)
slider.grid(row=2,column=1,padx=10,pady=10)
btn = CTkButton(frame,text=slider.get() , state='disabled',border_color='#1c1c1c',text_color_disabled='#57c8ff')
btn.grid(row=2, column=2, padx=10, pady=10)
slider.configure(command=lambda value, button=btn,label=label: getSlider(value,button,label))

label = CTkLabel(frame, text='Numeric Digits', font=(None,16))
label.grid(row=3,column=0,padx=10,pady=10)
slider = CTkSlider(frame, from_=0, to=10,number_of_steps=10)
slider.grid(row=3,column=1,padx=10,pady=10)
btn = CTkButton(frame,text=slider.get() , state='disabled',border_color='#1c1c1c',text_color_disabled='#57c8ff')
btn.grid(row=3, column=2, padx=10, pady=10)
slider.configure(command=lambda value, button=btn,label=label: getSlider(value,button,label))

btn = CTkButton(frame,text='Generate!', height=60, font=(None,20), command=genPassword)
btn.grid(row=4, column=1, padx=0, pady=30)

app.mainloop()