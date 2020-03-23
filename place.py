import os
import shutil
from os.path import join
from tkinter import filedialog
from tkinter import *

def show_entry_fields():

    p = e1.get()
    q = e2.get()
    z = e3.get()

    f = open(p, "r")
    a = f.readlines()
    b = []
    for item in a:
        splitof = item.split()
        b.append(splitof)
    n = []
    for x in b:
        for y in x:
            n.append(y)
    print(n)
    a = len(n)
    b = []
    for i in range(0, a):
        b = n[i]
        for root, dirs, files in os.walk(q):
            print("searching", root)
            #if b not in files:
                #("not found: %s" % join(root, b))
                #Label(master, text="File not copied:%s"%join(root,b), bg='firebrick1', fg='black',font=("Times New Roman Bold", 20)).place(x=620,y=470)
            if b in files:
                print("found: %s" % join(root, b))
                copy_file = join(root, b)
                print("--------")
                print(copy_file)
                print("--------")
                shutil.copy(copy_file, z)
                print("The file Copied Successfully -->, z)
                Label(master, text="File copied successfully",bg='pale green', fg='black' ,font=("Times New Roman Bold", 20)).place(x=650,y=520)
                break
        print("\n")

master = Tk()
master.title("WELCOME TO VTU")
master.geometry('1450x800')
master.config(bg='linen')

photo = PhotoImage(file="vtulogo33.png",height='270',width='210')
Label(master, image=photo,bg='linen').place(x=5,y=2)

Label(master, text="Visvesvaraya Technological University,Belagavi ",bg='linen', fg='black', font=("Times new roman Bold",25)).place(x=450,y=10)
Label(master, text="Welcome to VTU",bg='linen', fg='black', font=("Times new roman Bold",20)).place(x=650,y=50)
Label(master, text="Search File",bg='linen', fg='black', font=("Times new roman Bold",25)).place(x=650,y=180)
Label(master, text="Internship @ Computer Network Centre(C.N.C),\n VTU, Belagavi.Karnataka.India \n",bg='grey', fg='black', font=("times new roman Bold",12)).place(x=650,y=580)

Label(master, text="Input file \n",bg='linen', fg='black', font=("Times New Roman Bold",16)).place(x=450,y=280)
Label(master, text="Search input file in \n",bg='linen', fg='black', font=("Times New Roman Bold",16)).place(x=450,y=330)
Label(master, text="Target directory \n",bg='linen', fg='black', font=("Times New Roman Bold",16)).place(x=450,y=380)

def browse_button1():
    global file_path
    filename = filedialog.askopenfilename()
    file_path.set(filename)
    print(filename)
file_path = StringVar()
e1 = Entry(master,textvariable=file_path,bg='alice blue',fg='black', font=("Times New Roman Bold",15))
e1.place(x=680,y=280)
b1= Button(master,text='Select file',bg='alice blue', fg='black', font=("Times New Roman Bold", 12),command=browse_button1).place(x=900,y=280)

def browse_button2():
    global dir_path1
    dir1 = filedialog.askdirectory()
    dir_path1.set(dir1)
    print(dir1)
dir_path1 = StringVar()
e2 = Entry(master,textvariable=dir_path1,bg='alice blue',fg='black', font=("Times New Roman Bold",15))
e2.place(x=680,y=330)
b2= Button(master,text='Select directory',bg='alice blue', fg='black', font=("Times New Roman Bold", 12),command=browse_button2).place(x=900,y=330)

def browse_button3():
    global dir_path
    dir = filedialog.askdirectory()
    dir_path.set(dir)
    print(dir)
dir_path = StringVar()
e3 = Entry(master,textvariable=dir_path,bg='alice blue',fg='black', font=("Times New Roman Bold",15))
e3.place(x=680,y=380)
b3= Button(master,text='Select target directory',bg='alice blue', fg='black', font=("Times New Roman Bold", 12),command=browse_button3).place(x=900,y=380)

b4 = Button(master, text='Submit',bg='powder blue', fg='black',font=("Times New Roman Bold",15), command=show_entry_fields).place(x=750,y=420)
b5= Button(master, text='quit',bg='powder blue', fg='black',font=("Times New Roman Bold",15), command=master.quit).place(x=950,y=420)
mainloop( )




