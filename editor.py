import os
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
import time
def lucida():
    text_bar.config(font="Times 18")
    root.update()
def arial():
    text_bar.config(font="Arial 18")
    root.update_idletasks()
def comic():
    text_bar.config(font="tahoma 18")
    root.update()
def algerian():
    text_bar.config(font="algerian 18")
    root.update()
def save():
    global file
    a= text_bar.get(1.0,END)
    b= t.get()
    
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(f"{a}")
            f.close()

            root.title(f"{b}" + " - Notepad")
            messagebox.showinfo("Saved","File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(f"{a}")
        f.close()
def new():
    res= messagebox.askyesnocancel("Save","Do you want to save changes?")
    if res==True:
        save()
        t.delete(0,END)
        text_bar.delete(1.0,END)
        root.title("Notepad -- Untitled1")
    elif res== None:
        pass        
    else:
        t.delete(0,END)
        text_bar.delete(1.0,END)
        root.title("Notepad -- Untitled1")
    
def copy():
    text_bar.event_generate(("<<Copy>>"))
def cut():
    text_bar.event_generate(("<<Cut>>"))
def paste():
    text_bar.event_generate(("<<Paste>>"))
def about():
    messagebox.showinfo("About Editor","Editor created by Rahul\nTo simplify editing of simple text.")
def but():
    o= len(text_bar.get(1.0,END))
    q= len(title.get())
    status.set('Busy...')
    root.update()
    time.sleep(2)
    status.set(f'Ready          Characters: {o+q-1}        Click me to update!!!')
    root.update()
def quitapp():
    res= messagebox.askyesnocancel("Save","Do you want to save changes?")
    if res==True:
        save()
        root.destroy()
    elif res== None:
        pass        
    else:
        root.destroy()
def Open():
    file= askopenfilename(filetypes=[("Text Documents","*.txt")],defaultextension=".txt")
    root.title(os.path.basename(file)+ str("-- Notepad"))
    with open(file,"r+") as f:

        text_bar.insert(1.0,f.read())
    
root= Tk()
root.geometry("544x600")
root.resizable(0,0)
root.title("Notepad -- Untitled1")
f= Frame(root,bg="grey")
title= StringVar()
t= Entry(f,textvariable= title,font="algerian 30 bold",justify='center')
l= Label(f,text="Title",font="lucida 20")
file=None
l.pack()
t.pack()
f.pack()
text_bar= Text(root,font="lucida 18")
text_bar.pack(expand=True,fill=BOTH)
menubar= Menu(root)
m= Menu(menubar,tearoff=0)
m.add_command(label="Save",command=save)
m.add_command(label="New",command=new)
m.add_command(label="Open",command=Open)
menubar.add_cascade(label="File",menu=m)
m1= Menu(menubar,tearoff=0)
m1.add_command(label="copy",command=copy)
m1.add_command(label="cut",command=cut)
m1.add_command(label="paste",command=paste)
menubar.add_cascade(label="Edit",menu=m1)
m2= Menu(menubar,tearoff=0)
m2.add_command(label="about",command=about)
menubar.add_cascade(label="Help",menu=m2)
m3= Menu(menubar,tearoff=0)
m3.add_radiobutton(label="Times",command=lucida)
m3.add_radiobutton(label="Arial",command=arial)
m3.add_radiobutton(label="Tahoma",command=comic)
m3.add_radiobutton(label="algerian",command=algerian)
menubar.add_cascade(label="Font",menu=m3)
menubar.add_command(label="Exit",command=quitapp)
root.config(menu=menubar)
scroll= Scrollbar(text_bar)
scroll.pack(side=RIGHT,fill=Y)
scroll.config(command=text_bar.yview)
text_bar.config(yscrollcommand=scroll.set)
status= StringVar()
status.set('Press to know status')
l6= Button(root,textvariable= status,command=but,anchor='w',relief=SUNKEN)
l6.pack(side=BOTTOM,fill=X)
root.mainloop()