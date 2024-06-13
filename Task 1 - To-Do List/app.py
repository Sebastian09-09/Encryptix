from customtkinter import *
from datetime import datetime 
import json 


def get():
    with open('data.json','r') as f:
        return json.load(f)
    
def set(data):
    with open('data.json','w') as f:
        json.dump(data,f)


app = CTk()
app.geometry('800x600')
app.title('To-Do List')

set_appearance_mode('dark')
set_default_color_theme("theme.json")

def moveToExpired():
    global data, frame, all_expired_tasks
    delThis = []
    remThis = []
    for i in data['data']['to-do']:
        if i != datetime.today().strftime('%d/%m/%Y'):
            if i not in data['data']['expired']:
                data['data']['expired'][i] = []

            for x in data['data']['to-do'][i]:
                all_expired_tasks += 1
                data['data']['expired'][i].append(x)
                innereFrame = CTkFrame(master=eframe)
                innereFrame.grid(row=all_expired_tasks,column=0)
                en=CTkEntry(master=innereFrame ,width=600)
                en.grid(row=all_expired_tasks,column=0,padx=10, pady=10)
                en.delete(0,'end')
                en.insert(0,x)
                en.configure(state='disabled')

                om=CTkOptionMenu(master=innereFrame, values=["Activate","Delete"], width=20, command=lambda choice , task=en, frame=innereFrame: e_optionmenu_callback(choice, task, frame))
                om.grid(row=all_expired_tasks,column=1,padx=10, pady=10)
                om.set('Options') 
                remThis.append(x)  
            
            delThis.append(i)
    for j in delThis:
        data['data']['to-do'].pop(j)
    
    for widget in frame.winfo_children():
        for ent in widget.winfo_children():
            if isinstance(ent, CTkEntry):
                if ent.get() in remThis:
                    widget.destroy()
        
    set(data)

def fillToDo():
    all_tasks = 0
    for x in data['data']['to-do'][datetime.today().strftime('%d/%m/%Y')]:
        all_tasks += 1
        innerFrame = CTkFrame(master=frame)
        innerFrame.grid(row=all_tasks,column=0)
        en=CTkEntry(master=innerFrame ,width=600)
        en.grid(row=all_tasks,column=0,padx=10, pady=10)
        en.delete(0,'end')
        en.insert(0,x)
        en.configure(state='disabled')

        om=CTkOptionMenu(master=innerFrame, values=["Completed","Delete"], width=20, command=lambda choice , task=en, frame=innerFrame: optionmenu_callback(choice, task, frame))
        om.grid(row=all_tasks,column=1,padx=10, pady=10)
        om.set('Options')
    return all_tasks

def fillCompleted():
    all_completed_tasks = 0
    for i in data['data']['completed']:
        for x in data['data']['completed'][i]:
            all_completed_tasks += 1
            innercFrame = CTkFrame(master=cframe)
            innercFrame.grid(row=all_completed_tasks,column=0)
            en=CTkEntry(master=innercFrame ,width=600)
            en.grid(row=all_completed_tasks,column=0,padx=10, pady=10)
            en.delete(0,'end')
            en.insert(0,x)
            en.configure(state='disabled')

            om=CTkOptionMenu(master=innercFrame, values=["Delete"], width=20, command=lambda choice , task=en, frame=innercFrame: c_optionmenu_callback(choice, task, frame))
            om.grid(row=all_completed_tasks,column=1,padx=10, pady=10)
            om.set('Options')   

    return all_completed_tasks
    
    

def fillExpired():
    all_expired_tasks = 0
    for i in data['data']['expired']:
        for x in data['data']['expired'][i]:
            all_expired_tasks += 1
            innereFrame = CTkFrame(master=eframe)
            innereFrame.grid(row=all_expired_tasks,column=0)
            en=CTkEntry(master=innereFrame ,width=600)
            en.grid(row=all_expired_tasks,column=0,padx=10, pady=10)
            en.delete(0,'end')
            en.insert(0,x)
            en.configure(state='disabled')

            om=CTkOptionMenu(master=innereFrame, values=["Activate","Delete"], width=20, command=lambda choice , task=en, frame=innereFrame: e_optionmenu_callback(choice, task, frame))
            om.grid(row=all_expired_tasks,column=1,padx=10, pady=10)
            om.set('Options')   
    
    return all_expired_tasks


def on_tab_change():
    global label
    moveToExpired()
    
    #if tabview.get() == 'To-Do':
    #    label.configure(text=datetime.today().strftime('%d/%m/%Y'))
    #    fillToDo()
    
    #elif tabview.get() == 'Completed':
    #    fillCompleted()
    
    #elif tabview.get() == 'Expired':
    #    fillExpired()
    

tabview = CTkTabview(master=app , width=800, height=600, command=on_tab_change)
tabview.pack(padx=20, pady=20)

tabview.add("To-Do")  # add tab at the end
tabview.add("Completed")  # add tab at the end
tabview.add("Expired")  # add tab at the end
tabview.set("To-Do")  # set currently visible tab



label = CTkLabel(master=tabview.tab("To-Do"), text= datetime.today().strftime('%d/%m/%Y'))
label.pack()

#To-DO
frame = CTkScrollableFrame(master=tabview.tab('To-Do'), width=800, height=600)
frame.pack(padx=5,pady=10)


data = get()
moveToExpired()

def optionmenu_callback(choice, var, frame):
    global data, all_completed_tasks
    txt = var.get()
    frame.destroy()
    if choice == 'Delete':
        data['data']['to-do'][datetime.today().strftime('%d/%m/%Y')].remove(txt)
    elif choice == 'Completed':
        all_completed_tasks += 1
        data['data']['to-do'][datetime.today().strftime('%d/%m/%Y')].remove(txt)
        if datetime.today().strftime('%d/%m/%Y') in data['data']['completed']:
            data['data']['completed'][datetime.today().strftime('%d/%m/%Y')].append(txt)
        else:
            data['data']['completed'][datetime.today().strftime('%d/%m/%Y')] = [txt]

        innercFrame = CTkFrame(master=cframe)
        innercFrame.grid(row=all_completed_tasks,column=0)
        en=CTkEntry(master=innercFrame ,width=600)
        en.grid(row=all_completed_tasks,column=0,padx=10, pady=10)
        en.delete(0,'end')
        en.insert(0,txt)
        en.configure(state='disabled')

        om=CTkOptionMenu(master=innercFrame, values=["Delete"], width=20,command=lambda choice , task=en, frame=innercFrame: c_optionmenu_callback(choice, task, frame))
        om.grid(row=all_completed_tasks,column=1,padx=10, pady=10)
        om.set('Options')   

    set(data)
         

def c_optionmenu_callback(choice, var, frame):
    global data
    txt = var.get()
    frame.destroy()
    for i in data['data']['completed']:
        if txt in data['data']['completed'][i]:
            data['data']['completed'][i].remove(txt)
    set(data)

def e_optionmenu_callback(choice, var, DElframe):
    global data, all_tasks
    txt = var.get()
    DElframe.destroy()
    if choice == 'Delete':
        for i in data['data']['expired']:
            if txt in data['data']['expired'][i]:
                data['data']['expired'][i].remove(txt)

    elif choice == 'Activate':
        all_tasks += 1
        for i in data['data']['expired']:
            if txt in data['data']['expired'][i]:
                data['data']['expired'][i].remove(txt) 
        if datetime.today().strftime('%d/%m/%Y') not in data['data']['to-do']:
            data['data']['to-do'][datetime.today().strftime('%d/%m/%Y')] = []
        set(data)

        data['data']['to-do'][datetime.today().strftime('%d/%m/%Y')].append(txt)

        innerFrame = CTkFrame(master=frame)
        innerFrame.grid(row=all_tasks,column=0)
        en=CTkEntry(master=innerFrame ,width=600)
        en.grid(row=all_tasks,column=0,padx=10, pady=10)
        en.delete(0,'end')
        en.insert(0,txt)
        en.configure(state='disabled')

        om=CTkOptionMenu(master=innerFrame, values=["Completed","Delete"], width=20, command=lambda choice , task=en, frame=innerFrame: optionmenu_callback(choice, task, frame))
        om.grid(row=all_tasks,column=1,padx=10, pady=10)
        om.set('Options')

    set(data)   



if datetime.today().strftime('%d/%m/%Y') not in data['data']['to-do']:
    data['data']['to-do'][datetime.today().strftime('%d/%m/%Y')] = []
    set(data)

all_tasks = fillToDo()

#Completed
cframe = CTkScrollableFrame(master=tabview.tab('Completed'), width=800, height=600)
cframe.pack(padx=5,pady=10)

all_completed_tasks = fillCompleted()

#Expired
eframe = CTkScrollableFrame(master=tabview.tab('Expired'), width=800, height=600)
eframe.pack(padx=5,pady=10)

all_expired_tasks = fillExpired()

def add_handler():
    if entry.get().strip() == '':
        return False 
    global all_tasks,data 
    all_tasks += 1
    innerFrame = CTkFrame(master=frame)
    innerFrame.grid(row=all_tasks,column=0)
    en=CTkEntry(master=innerFrame ,width=600)
    en.grid(row=all_tasks,column=0,padx=10, pady=10)
    en.delete(0,'end')
    en.insert(0,entry.get().strip())
    en.configure(state='disabled')
    om=CTkOptionMenu(master=innerFrame, values=["Completed","Delete"], width=20, command=lambda choice , task=en, frame=innerFrame: optionmenu_callback(choice, task, frame))
    om.grid(row=all_tasks,column=1,padx=10, pady=10)
    om.set('Options')
    data['data']['to-do'][datetime.today().strftime('%d/%m/%Y')].append(entry.get().strip())
    set(data)
    entry.delete(0, 'end')


innerFrame = CTkFrame(master=frame)
innerFrame.grid(row=0,column=0)
entry = CTkEntry(master=innerFrame, placeholder_text="Enter New Task ...",width=600 )
entry.grid(row=0,column=0,padx=10, pady=10)
add = CTkButton(master=innerFrame, text='Add', width=80, border_width=2, command=add_handler)
add.grid(row=0,column=1,padx=10, pady=10)

#frame.configure(height=100)

app.mainloop()