from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import csv,os
import pandas as pd

def csv_details(filepath):
    print(filepath)
    #to display the fields
    '''f=open(filepath,"r",newline='')
    label_text=''
    rec=csv.reader(f)
    for i in rec:
        label_text+=str(i)
        label_text+="\n"
    f.close()'''
    df = pd.read_csv(filepath)
    newlabel2 = Label(f2,text=df,background='thistle1')
    newlabel2.place(x=15,y=30)
    newlabel3 = Label(f3,text=df,background='thistle2')
    newlabel3.place(x=15,y=600)
    
    
def menubutton_placement():
    menub1 = Menubutton(f1, text='Null Value Treatment', activebackground="red",width=100)
    menub1.place(x=10,y=530)
    menub1.menu = Menu(menub1, tearoff=0)
    menub1["menu"] = menub1.menu
    mayo_sauce = IntVar()
    ketchup = IntVar()
    menub1.menu.add_checkbutton(label='Remove null', variable=mayo_sauce)
    menub1.menu.add_checkbutton(label='Replace Null', variable=ketchup)

    menub2 = Menubutton(f1, text='Data Drop', activebackground="red",width=100)
    menub2.place(x=10,y=630)
    menub2.menu = Menu(menub2, tearoff=0)
    menub2["menu"] = menub2.menu
    row2 = IntVar()
    col2 = IntVar()
    menub2.menu.add_checkbutton(label='Remove row', variable=row2)
    menub2.menu.add_checkbutton(label='Replace  column', variable=col2)

    menub3 = Menubutton(f1, text='Data Creation', activebackground="red",width=100)
    menub3.place(x=10,y=730)
    menub3.menu = Menu(menub3, tearoff=0)
    menub3["menu"] = menub3.menu
    merge = IntVar()
    menub3.menu.add_checkbutton(label='Merge two datasets', variable=merge)

    menub4 = Menubutton(f1, text='Data Slicing', activebackground="red",width=100)
    menub4.place(x=10,y=830)
    menub4.menu = Menu(menub4, tearoff=0)
    menub4["menu"] = menub4.menu
    binning= IntVar()
    onehotencoding = IntVar()
    labelencoding = IntVar()
    menub4.menu.add_checkbutton(label='Binning', variable=binning)
    menub4.menu.add_checkbutton(label='One-Hot Encoding', variable=onehotencoding)
    menub4.menu.add_checkbutton(label='Label Encoding', variable=labelencoding)

    menub5 = Menubutton(f1, text='Feature Scaling', activebackground="red",width=100)
    menub5.place(x=10,y=930)
    menub5.menu = Menu(menub5, tearoff=0)
    menub5["menu"] = menub5.menu
    normalization = IntVar()
    standardization = IntVar()
    menub5.menu.add_checkbutton(label='Normalization', variable=normalization)
    menub5.menu.add_checkbutton(label='Standardization', variable=standardization)
    
def do_layout():
        f1.grid(row=0, column=0, rowspan=2, sticky="nsew")
        f2.grid(row=0, column=1, sticky="nsew")
        f3.grid(row=1, column=1, sticky="nsew")
        f4.grid(row=0, column=2, sticky="nsew")
        f5.grid(row=1, column=2, sticky="nsew")

        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)
        
def screen1_window():
    global f1,f2,f3,f4,f5,root
    #create root
    root = Tk()
    root.title("Pipeline")
    width1=root.winfo_screenwidth()
    height2 = root.winfo_screenheight()
    root.geometry("%dx%d" % (width1,height2))

    #create all 5 frames for the dropdowns, 2 file contents and 2 file statistics
    f1 = Frame(root, bg='grey', width=width1/3,height=height2)
    f2 = Frame(root, bg='thistle1', width=width1/3, height=height2/2)
    f3 = Frame(root, bg='thistle2', width=width1/3, height=height2/2)
    f4 = Frame(root, bg='AntiqueWhite1', width=width1/3, height=height2/2)
    f5 = Frame(root, bg='AntiqueWhite2', width=width1/3, height=height2/2)
    #place the frames on root with required rowspan and columnspan
    do_layout()
    menubutton_placement()

    def select_file():
        global filepath
        filetypes = (
            ('csv files', '*.csv'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(title='Choose a file',initialdir='/',filetypes=filetypes)
        showinfo(title='Selected File',message=filename)
        filepath = "Filepath : " + filename
        newlabel = Label(root,text=filepath)
        newlabel.place(x=10,y=130)
        continue_b = Button(f1,text="continue",command=lambda:csv_details(filename))
        continue_b.place(x=10,y=160)

    # open button
    open_button = ttk.Button(root, text='Choose a file', command=select_file)
    open_button.place(x=10,y=100)
    root.mainloop()
screen1_window()


