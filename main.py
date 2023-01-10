import streamlit as st
import pandas as pd
import lib1

FILE = "test.txt"     #FIRST FILE FOR PREPROCESSING
FILE2 = "buff.txt"    #SECOND FILE
ATTFILE = "att.txt"   #THIRD FILE STORING ATTRIBUTES

df = pd.DataFrame()
df1 = pd.DataFrame()

def write_to(FILE,num,Rem = False):
    f = open(FILE,"r")
    i = f.readlines()
    if i == []:
        i = ''
    else:
        i = i[0]
    f.close()
    if(i == '' and Rem):
        return -1
    i = i.split(",")
    try:
        i.remove('')
    except:
        pass
    i.append(str(num))
    f = open(FILE,"w")
    for j in i:
        f.write(j)
        f.write(",")
    return 1

def att_write(ATTFILE,att,Rem = False):
    f = open(ATTFILE,"r")
    i = f.readlines()
    if i == []:
        i = ''
    else:
        i = i[0]
    f.close()
    if(i == '' and Rem):
        return -1
    i = i.split(",")
    i.remove('')
    i.append(str(att))
    f = open(ATTFILE,"w")
    for j in i:
        f.write(j)
        f.write(",")
    return 1

#CONFIGURE WEBSITE TO TAKE UP ENTIRE WIDTH OF THE SCREEN
st.set_page_config(page_title = "Pipeline", layout = "wide")

st.title("PIPELINE")
st.write("The processing site for all your preprocessing needs")
st.write("\n\n")

df = pd.DataFrame()   #CREATING AN EMPTY DATAFRAME

#CREATE A SIDE-BAR FOR ALL THE DATA PRE-PROCESSING METHODS IN THE FORM OF DROP-DOWNS
with st.sidebar:
    st.write("OPERATIONS")

    with st.form("Transform"):
        option = st.selectbox("VALUE TRANSFORMS", ["","Null Value Removal","Fill Null Values", "Remove Outliers"])
        if option == "Null Value Removal":
            o1 = st.text_input("Enter column name:")
        elif option == "Fill Null Values":
            o1 = st.radio(" * Fill Null Values",["Mean","Median","Value"])
            o2 = st.text_input("Value: ")
        else:
            o1 = st.text_input("Upper Quantile")
            o2 = st.text_input("Lower Quantile")
        st.form_submit_button("Remove")



        if option == "Null Value Removal":
            if o1 in df.columns:
                write_to(FILE,110)
                att_write(ATTFILE,o1)
                option = ""
                o1 = ""
        elif option == "Fill Null Values":
            if o1 == "Mean":
                write_to(FILE,121)
                att_write(ATTFILE,"none")
                option = ""
                o1 = ""
            elif o1 == "Median":
                write_to(FILE,122)
                att_write(ATTFILE,"none")
                option = ""
                o1 = ""
            elif o1 == "Value":
                write_to(FILE,123)
                att_write(ATTFILE,o2)
                option = ""
                o1 = ""
        elif option == "Remove Outliers":
            if o1< 1 and o2 < 1:
                write_to(FILE,130)
                att_write(ATTFILE,str(o1)+"+"+str(o2))
                option = ""
                o1 = ""






    with st.form("Creation"):
        option = st.selectbox("CREATION OPERATIONS", ["","Replace","Append"])
        f1 = st.file_uploader("Upload a csv: ")
        f2 = st.file_uploader("Upload an excel file: ")
        st.form_submit_button("Create")

        if option == "Replace":
            if f1:
                write_to(FILE,211)
                att_write(ATTFILE,f1)
                option = ""
                f1 = ""
            elif f2:
                write_to(FILE,212)
                att_write(ATTFILE,f2)
                option = ""
                f2 = ""
        elif option == "Append":
            if f1:
                write_to(FILE,221)
                att_write(ATTFILE,f1)
                option = ""
                f1 = ""
            elif f2:
                write_to(FILE,222)
                att_write(ATTFILE,f2)
                option = ""
                f2 = ""





    with st.form("Drop"):
        option = st.selectbox("DROP OPERATIONS",["","Drop Row","Drop Column"])
        if option == "Drop Row":
            o = st.text_input("Enter row to be deleted")
        elif option == "Drop Column":
            o = st.text_input("Enter Column to be deleted")
        st.form_submit_button("Drop")
        
        if option == "Drop Row":
            if o:
                write_to(FILE,310)
                att_write(ATTFILE,o)
                option = ""
                o = ""
        elif option == "Drop Column":
            if o:
                write_to(FILE,320)
                att_write(ATTFILE,o)
                option = ""
                o = ""
    





    with st.form("Scale"):
        option = st.selectbox("FEATURE SCALING",["","Encode", "Normalize","Transform"])
        if option == "Encode":
            o = st.radio("Numerize",["One-Hot Encoding","Label Encoding"])
        elif option == "Normalize":
            o = st.radio("Normalize",["Min-Max","Standard"])
        elif option == "Transform":
            o = st.radio("Transform",["Log","Square"])
        st.form_submit_button("Scale")

        if option == "Encode":
            if o == "One-Hot Encoding":
                write_to(FILE,411)
                att_write(ATTFILE,"none")
                option = ""
                o = ""
            elif o == "Label Encoding":
                write_to(FILE,412)
                att_write(ATTFILE,"none")
                option = ""
                o = ""
        elif option == "Normalize":
            if o == "Min-Max":
                write_to(FILE,421)
                att_write(ATTFILE,"none")
                option = ""
                o = ""
            elif o == "Standard":
                write_to(FILE,422)
                att_write(ATTFILE,"none")
                option = ""
                o = ""
        elif option == "Transform":
            if o == "Log":
                write_to(FILE,431)
                att_write(ATTFILE,"none")
                option = ""
                o = ""
            elif o == "Square":
                write_to(FILE,432)
                att_write(ATTFILE,"none")
                option = ""
                o = ""

with st.container():
    col1,col2,col3 = st.columns([1,2,2])
    with col1:
        form3 = st.form("3")
        with form3:
            l = st.form_submit_button("Back")
        data = st.file_uploader("Upload a csv: ")
        if data is not None:
            df = pd.read_csv(data)
        df,df1 = lib1.make(FILE,ATTFILE,df)
    with col2:
        col2.write(df)

    with col3:
        col3.write(df1)


'''WORKING - DO NOT TOUCH'''

with st.container():
    col1,col2,col3 = st.columns([1,2,2])
    with col1:
        SAVEFILE = st.text_input("Enter location and name of save file: ")
        if SAVEFILE:
            try:
                f = df.to_csv(SAVEFILE)
            except FileNotFoundError:
                pass
        
    with col2:
        f = open(FILE2,"w")
        df.info(buf=f)
        f.close()
        f = open(FILE2,"r")
        e = f.readlines()
        f.close()
        for i in e:
            st.write(i)

    with col3:
        f = open(FILE2,"w")
        df.info(buf=f)
        f.close()
        f = open(FILE2,"r")
        e = f.readlines()
        f.close()
        for i in e:
            st.write(i)
