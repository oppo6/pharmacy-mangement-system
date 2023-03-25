from tkinter import *
from PIL import Image, ImageTk
import random
from tkinter import ttk, messagebox
import sqlite3

root= Tk()
root.title("Pharmacy Management System")
root.geometry("1350x734+0+0")
root.resizable(0,0)
root.iconbitmap("doc.ico")

ref_variable = StringVar()
addmed_variable = StringVar()
refno_var = StringVar()
companyname_var = StringVar()
typemed_var = StringVar()
medicine_var = StringVar()
lotno_var = StringVar()
issuedt_var = StringVar()
expdt_var = StringVar()
uses_var = StringVar()
sideeffect_var = StringVar()
warning_var = StringVar
dosage_var = StringVar()
price_var = StringVar()
quantity_var = StringVar()

search_by = StringVar()
search_txt = StringVar()

######## title animation #########
txt = "PHARMACY MANAGEMENT SYSTEM"
count =0
text=""
color = ["BLACK"]
heading = Label( root, text= txt, font=( "times new roman", 30, "bold"), bg='WHITE', fg="blue", bd=9, relief=RIDGE)
heading.pack(side=TOP, fill=X)



# lbltitle=Label( root,text=" PHARMACY MANAGEMENT SYSTEM",bd=11,relief=RIDGE
    # ,bg='#7FFFD4',fg='#0020C2',font=('times new roman',35,'bold'),padx=2,pady=4)
# lbltitle.pack(side=TOP,fill=X)

######### pharmacy logo label #######
##img1 = Image.open("new.png")
##img1 = img1.resize(70, 45)
##photoimg1 = ImageTk.PhotoImage(img1)
##b1 = Button( root, image= photoimg1,
##    borderwidth=0, bg='#1e85d0')
##b1.place(x=15, y=8)

###### Top Frame #####
topframe = Frame( root, bg='#1e85d0', bd=10, relief=RIDGE, padx=20)
topframe.place(x=0, y=62, width=1350, height=400)

########  down button frame #######
down_buttonframe = Frame(
     root, bg='#1e85d0', bd=10, relief=RIDGE, padx=20)
down_buttonframe.place(x=0, y=462, width=1350, height=60)



def AddMed( ):

        if  ref_variable.get() == "" or  addmed_variable.get() == "":
            messagebox.showerror("Error", "All fields are required")

        else:
            conn = sqlite3.connect(database=r'D:\Pharmacy_management-system-master\pharmacy.db')
            my_cursor = conn.cursor()
            my_cursor.execute("Insert into pharma(Ref_no,Med_name) values(?,?)", (
            ref_variable.get(),
            addmed_variable.get()))
            conn.commit()
            fetch_datamed()
            conn.close()

            messagebox.showinfo("Success", "MEDICINE ADDED")

def fetch_datamed( ):
    conn = sqlite3.connect(database=r'D:\Pharmacy_management-system-master\pharmacy.db')
    my_cursor = conn.cursor()
    my_cursor.execute("select * from pharma")
    rows = my_cursor.fetchall()

    if len(rows) != 0:
         medicine_table.delete(* medicine_table.get_children())

    for i in rows:
                 medicine_table.insert("", END, values=i)

    conn.commit()
    conn.close()

    ###### for show data on click #####

def medget_cursor( event=""):
        cursor_row =  medicine_table.focus()
        content =  medicine_table.item(cursor_row)
        row = content["values"]
        ref_variable.set(row[0])
        addmed_variable.set(row[1])

def Update_med( ):

        if  ref_variable.get() == "" or  addmed_variable.get()=="":

            messagebox.showerror("Error", "Ref No. and med name is required")
        else:
            try:
                    conn = sqlite3.connect(database=r'D:\Pharmacy_management-system-master\pharmacy.db')
                    my_cursor = conn.cursor()

                    my_cursor.execute("Update pharma set Med_name=? where Ref_no=?", (
                     addmed_variable.get(),
                     ref_variable.get()
                    ))

                    conn.commit()
                    messagebox.showinfo("Update", "Successfully Updated", parent= root)
                    fetch_datamed()
                    conn.close()
                    root.destroy()
                    import e
            except Exception as e:
                   messagebox.showerror("Error",f"Error due to:{str(e)}",parent= root)




def Delete_med( ):
        if  ref_variable.get()=="" or addmed_variable.get=="":
            messagebox.showerror("Error","Ref no is required",parent= root)
        else:

            try:
                    conn=sqlite3.connect(database=r'D:\Pharmacy_management-system-master\pharmacy.db')
                    my_cursor=conn.cursor()
                        
                    my_cursor.execute("Delete from pharma where Ref_no=? and Med_name= ? ",( ref_variable.get(),addmed_variable.get()))
                    conn.commit()
                    messagebox.showinfo("Delete","Successfully Deleted",parent= root)
                    fetch_datamed()
            except Exception as e:
                     messagebox.showerror("Error",f"Error due to:{str(e)}",parent= root)



def clear_med( ):
     ref_variable.set("")
     addmed_variable.set("")



    


    
    
    ######## MEDICINE DEPARTMENT FUNCTIONALITY #######
def addmedicine( ):
        if  refno_var.get() == "" or  lotno_var.get() == "" or  typemed_var.get() == "":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=sqlite3.connect(database=r'D:\Pharmacy_management-system-master\pharmacy.db')
            new_cursor=conn.cursor()
            new_cursor.execute("Insert into Information(REF_NO,COMPANY_NAME,TYPE_OF_MED,MED_NAME,LOT_NO,ISSUE_DT,EXP_DT,USES,SIDE_EFFECT) values(?, ?, ?, ?, ?, ?, ?, ?, ?)",(            
             refno_var.get(),
             companyname_var.get(),
             typemed_var.get(),
             medicine_var.get(),
             lotno_var.get(),
             issuedt_var.get(),
             expdt_var.get(),
             uses_var.get(),
             sideeffect_var.get()))
            conn.commit()
            fetch_new()
##            warning_var.get(),dosage_var.get(),price_var.get(),quantity_var.get()  ,PRECAUTION,DOSAGE,PRICE,QUANTITY
            messagebox.showinfo("Success","Successfully added")

def fetch_new( ):
        conn=sqlite3.connect(database=r'D:\Pharmacy_management-system-master\pharmacy.db')
        new_cursor=conn.cursor()
        new_cursor.execute("select * from Information")
        row=new_cursor.fetchall()

        if len(row)!=0:
             info_table.delete(* info_table.get_children())

        for i in row:
               info_table.insert("",END,values=i)
        conn.commit()
            
def get_cursor(event="" ):
        cursor_row= info_table.focus()
        content= info_table.item(cursor_row)
        row=content["values"]
        refno_var.set(row[0])
        companyname_var.set(row[1])
        typemed_var.set(row[2])
        medicine_var.set(row[3])
        lotno_var.set(row[4])
        issuedt_var.set(row[5])
        expdt_var.set(row[6])
        uses_var.set(row[7])
        sideeffect_var.set(row[8])
##        warning_var.set(row[9])
##        dosage_var.set(row[10])
##        price_var.set(row[11])
##        quantity_var.set(row[12])

def update_new( ):

    if  refno_var.get() == "" or  lotno_var.get() == "" or  typemed_var.get() == "":
        messagebox.showerror("Error","All fields are required")
    else:
        conn=sqlite3.connect(database=r'D:\Pharmacy_management-system-master\pharmacy.db')
        new_cursor=conn.cursor()
        new_cursor.execute("Update Information set COMPANY_NAME=?,TYPE_OF_MED=?,MED_NAME=?,LOT_NO=?,ISSUE_DT=?,EXP_DT=?,USES=?,SIDE_EFFECT=? where REF_NO=?",
                           (companyname_var.get(),typemed_var.get(),medicine_var.get(),lotno_var.get(),
                            issuedt_var.get(),expdt_var.get(),uses_var.get(),sideeffect_var.get(),
                            refno_var.get()))
        conn.commit()
        fetch_new()
        
        clear_new()
        messagebox.showinfo("Success","Successfully updated")

def clear_new( ):
     refno_var.set("")
     companyname_var.set("")
     typemed_var.set("")
     medicine_var.set("")
     lotno_var.set("")
     issuedt_var.set("")
     expdt_var.set("")
     uses_var.set("")
     sideeffect_var.set("")
##     warning_var.set("")
##     dosage_var.set("")
##     price_var.set("")
##     quantity_var.set("")
    

def search_data( ):

        conn=sqlite3.connect(database=r'D:\Pharmacy_management-system-master\pharmacy.db')
        new_cursor=conn.cursor()
        selected =  search_combo.get()
        if selected == "Select Options":
            messagebox.showerror("Error","You have to choose an option")

        else:
            new_cursor.execute("Select * from Information where REF_NO=?",( search_txt.get(),))
            row=new_cursor.fetchone()

            if len(row)!=0:
              info_table.delete(* info_table.get_children())

            for i in row:
                    info_table.insert("",END,values=i)

        conn.commit()


def Delete( ):
        if refno_var.get()=="" or medicine_var.get()=="":
            messagebox.showerror("Error","Ref no is required")
        else:

            try:
                    conn=sqlite3.connect(database=r'D:\Pharmacy_management-system-master\pharmacy.db')
                    my_cursor=conn.cursor()
                        
                    my_cursor.execute("Delete from Information where REF_NO=? and MED_NAME=?", (refno_var.get(),medicine_var.get()))
                    conn.commit()
                    fetch_new()
        
                    clear_new()
                    messagebox.showinfo("Delete","Successfully Deleted")
            except Exception as e:
                     messagebox.showerror("Error",f"Error due to:{str(e)}")

def destroy():
    root.destroy()










    ###### all buttons ######
add_button = Button(down_buttonframe, text="Add Medicine", command= addmedicine, font=(
    "arial", 12, "bold"), width=14, fg="white", bg="black", bd=3, relief=RIDGE, activebackground="black", activeforeground="white")
add_button.grid(row=0, column=0)

update_button = Button(down_buttonframe, command= update_new, text="Update", font=(
    "arial", 13, "bold"), width=14, fg="white", bg="black", bd=3, relief=RIDGE, activebackground="black", activeforeground="white")
update_button.grid(row=0, column=1)

delete_button = Button(down_buttonframe,command=Delete, text="Delete", font=("arial", 13, "bold"), width=13,
       fg="white", bg="black", bd=3, relief=RIDGE, activebackground="black", activeforeground="white")
delete_button.grid(row=0, column=2)

reset_button = Button(down_buttonframe, text="Reset", command= clear_new, font=("arial", 13, "bold"), width=12,
      fg="white", bg="black", bd=3, relief=RIDGE, activebackground="black", activeforeground="white")
reset_button.grid(row=0, column=3)

exit_button = Button(down_buttonframe, command= destroy, text="Exit", font=(
    "arial", 13, "bold"), width=10, fg="white", bg="black", bd=3, relief=RIDGE, activebackground="black", activeforeground="white")
exit_button.grid(row=0, column=4)

search_by = Label(down_buttonframe, text="Search By", font=(
    "arial", 15, "bold"), fg="black", bg="#1e85d0", bd=3, padx=3)
search_by.grid(row=0, column=5, sticky=W)

search_combo = ttk.Combobox(down_buttonframe, width=12, font=(
    "arial", 13, "bold"), state="readonly", textvariable= search_by)
search_combo["values"] = ( "Ref No.")
search_combo.grid(row=0, column=6)
search_combo.current(0)

entry_button = Entry(down_buttonframe, font=("arial", 15, "bold"), fg="black",
     bg="#1e85d0", bd=3, width=12, relief=RIDGE, textvariable= search_txt)
entry_button.grid(row=0, column=7)

search_button = Button(down_buttonframe, text="Search", font=("arial", 13, "bold"), width=10, fg="white", bg="black",
       bd=3, relief=RIDGE, activebackground="black", activeforeground="white", command= search_data)
search_button.grid(row=0, column=8)

show_button = Button(down_buttonframe, text="Show All", font=("arial", 13, "bold"), fg="white", bg="black",
     width=10, bd=3, relief=RIDGE, activebackground="black", activeforeground="white", command= fetch_new)
show_button.grid(row=0, column=9)

######## left small frame #######
left_smallframe = LabelFrame(topframe, bg='#1e85d0', bd=10, relief=RIDGE,
     padx=20, text="Medicine Information", font=("arial", 13, "bold"), fg="white")
left_smallframe.place(x=0, y=5, width=820, height=350)

   #### labeling & entry box #########

# 1

ref_label = Label(left_smallframe, text="Reference No. :", padx=2, pady=4, font=(
    "times new roman", 13, "bold"), bg="#1e85d0")
ref_label.grid(row=0, column=0, sticky=W)

conn = sqlite3.connect(database=r'D:\Pharmacy_management-system-master\pharmacy.db')
my_cursor = conn.cursor()
my_cursor.execute("Select Ref_no from pharma")
row_01 = my_cursor.fetchall()

ref_combo = ttk.Combobox(left_smallframe, textvariable= refno_var, width=22, font=(
    "times new roman", 13, "bold"), state="readonly")
ref_combo["values"] = (row_01)
ref_combo.grid(row=0, column=1)
ref_combo.current(0)

# 2

company_label = Label(left_smallframe, text="Company Name  :", padx=2, pady=4, font=(
    "times new roman", 13, "bold"), bg="#1e85d0")
company_label.grid(row=1, column=0)

company_entry = Entry(left_smallframe, textvariable= companyname_var, width=24, font=(
    "times new roman", 13, "bold"), fg="black", bg="white")
company_entry.grid(row=1, column=1)

# 3
type_label = Label(left_smallframe, text="Type Of Medicine :", padx=2, pady=4, font=(
    "times new roman", 13, "bold"), bg="#1e85d0")
type_label.grid(row=2, column=0, sticky=W)

type_combo = ttk.Combobox(left_smallframe, textvariable= typemed_var, width=22, font=(
    "times new roman", 13, "bold"), state="readonly")
type_combo["values"] = (
    " Select  ", "Tablet", "Capsule", "Injection", "Ayurvedic", "Drops", "Inhales")
type_combo.grid(row=2, column=1)
type_combo.current(0)

# 4

medname_label = Label(left_smallframe, text="Medicine Name :", padx=2, pady=4, font=(
    "times new roman", 13, "bold"), bg="#1e85d0")
medname_label.grid(row=3, column=0, sticky=W)

conn = sqlite3.connect(database=r'D:\Pharmacy_management-system-master\pharmacy.db')
my_cursor = conn.cursor()
my_cursor.execute("Select Med_name from pharma")
row_02 = my_cursor.fetchall()

medname_combo = ttk.Combobox(left_smallframe, textvariable= medicine_var, width=22, font=(
    "times new roman", 13, "bold"), state="readonly")
medname_combo["values"] = (row_02)
medname_combo.grid(row=3, column=1)
medname_combo.current(0)

# 5

lot_label = Label(left_smallframe, text="PRICE :", padx=2, pady=4, font=(
    "times new roman", 13, "bold"), bg="#1e85d0")
lot_label.grid(row=4, column=0)

lot_entry = Entry(left_smallframe, textvariable= lotno_var, width=24, font=(
    "times new roman", 13, "bold"), fg="black", bg="white")
lot_entry.grid(row=4, column=1)

# 6

issue_label = Label(left_smallframe, text=" Issue Date :", padx=2, pady=4, font=(
    "times new roman", 13, "bold"), bg="#1e85d0")
issue_label.grid(row=5, column=0)

issue_entry = Entry(left_smallframe, textvariable= issuedt_var, width=24, font=(
    "times new roman", 13, "bold"), fg="black", bg="white")
issue_entry.grid(row=5, column=1)

# 7

exp_label = Label(left_smallframe, text=" Expiry Date :", padx=2, pady=4, font=(
    "times new roman", 13, "bold"), bg="#1e85d0")
exp_label.grid(row=6, column=0)

exp_entry = Entry(left_smallframe, textvariable= expdt_var, width=24, font=(
    "times new roman", 13, "bold"), fg="black", bg="white")
exp_entry.grid(row=6, column=1)

# 8

use_label = Label(left_smallframe, text=" Uses :", padx=2, pady=4, font=(
    "times new roman", 13, "bold"), bg="#1e85d0")
use_label.grid(row=7, column=0)

use_entry = Entry(left_smallframe, textvariable= uses_var, width=24, font=(
    "times new roman", 13, "bold"), fg="black", bg="white")
use_entry.grid(row=7, column=1)

# 9

sideeffect_label = Label(left_smallframe, text=" Side Effect :", padx=2, pady=4, font=(
    "times new roman", 13, "bold"), bg="#1e85d0")
sideeffect_label.grid(row=8, column=0)

sideeffect_entry = Entry(left_smallframe, textvariable= sideeffect_var, width=24, font=(
    "times new roman", 13, "bold"), fg="black", bg="white")
sideeffect_entry.grid(row=8, column=1)

# 10
##
##warn_label = Label(left_smallframe, text=" Prec & warning:", padx=2, pady=4, font=(
##    "times new roman", 13, "bold"), bg="#1e85d0")
##warn_label.grid(row=9, column=0)
##
##warn_entry = Entry(left_smallframe, textvariable= warning_var, width=24, font=(
##    "times new roman", 13, "bold"), fg="black", bg="white")
##warn_entry.grid(row=9, column=1)

# 11

##dosage_label = Label(left_smallframe, text=" Dosage :", padx=2, pady=4, font=(
##    "times new roman", 13, "bold"), bg="#1e85d0")
##dosage_label.grid(row=0, column=2)
##
##dosage_entry = Entry(left_smallframe, textvariable= dosage_var, width=28, font=(
##    "times new roman", 13, "bold"), fg="black", bg="white")
##dosage_entry.grid(row=0, column=3)
##
### 12
##
##price_label = Label(left_smallframe, text=" Tablet Price :", padx=2, pady=4, font=(
##    "times new roman", 13, "bold"), bg="#1e85d0")
##price_label.grid(row=1, column=2)
##
##price_entry = Entry(left_smallframe, textvariable= price_var, width=28, font=(
##    "times new roman", 13, "bold"), fg="black", bg="white")
##price_entry.grid(row=1, column=3)

# 13

##qt_label = Label(left_smallframe, text=" Tablet Quantity :", padx=2, pady=4, font=(
##    "times new roman", 13, "bold"), bg="#1e85d0")
##qt_label.grid(row=2, column=2)
##
##qt_entry = Entry(left_smallframe, textvariable= quantity_var, width=28, font=(
##    "times new roman", 13, "bold"), fg="black", bg="white")
##qt_entry.grid(row=2, column=3)

    ######## image in left small frame #####
# image 1
bg = ImageTk.PhotoImage(file="med.jpg")
lbl_bg = Label(left_smallframe, image= bg)
lbl_bg.place(x=370, y=165, width=200, height=150)
# image 2
bgg = ImageTk.PhotoImage(file="medi.jpg")
lbl_bgg = Label(left_smallframe, image= bgg)
lbl_bgg.place(x=570, y=165, width=200, height=150)

# save life label
save_bgg = Label(left_smallframe, text="----------- Stay Home Stay Safe -----------",
                font=("arial", 13, "bold"), bg='#1e85d0', fg="white")
save_bgg.place(x=370, y=120, width=400)

############ right frame #########
right_frame = LabelFrame(topframe, bg='#1e85d0', bd=10, relief=RIDGE, padx=5,
text="New Medicine Add department", font=("arial", 13, "bold"), fg="white")
right_frame.place(x=846, y=5, width=452, height=350)

  # image & label

# image 1
bg1 = ImageTk.PhotoImage(file="co.jpg")
lbl_bg1 = Label(right_frame, image= bg1)
lbl_bg1.place(x=0, y=0, width=240, height=100)
# image 2
bg2 = ImageTk.PhotoImage(file="inject.jpg")
lbl_bg2 = Label(right_frame, image= bg2)
lbl_bg2.place(x=242, y=0, width=180, height=150)

#### label & entry in right frame ####
# 1
no_label = Label(right_frame, text="Reference No:", font=(
    "times new roman", 11, "bold"), bg="#1e85d0")
no_label.place(x=0, y=105)

no_entry = Entry(right_frame, textvariable= ref_variable, width=16, font=(
    "times new roman", 11, "bold"), bg="white")
no_entry.place(x=100, y=105)
# 2
med_label = Label(right_frame, text="Med. Name:", font=(
    "times new roman", 11, "bold"), bg="#1e85d0")
med_label.place(x=0, y=130)

med_entry = Entry(right_frame, textvariable= addmed_variable, width=16, font=(
    "times new roman", 11, "bold"), bg="white")
med_entry.place(x=100, y=130)

#### in right frame small frame #####

newframe = Frame(right_frame, bg='darkgreen', bd=5, relief=RIDGE)
newframe.place(x=256, y=160, width=150, height=150)

  ###### button in this frame ###
add_button = Button(newframe, text="Add", font=("arial", 13, "bold"), width=13, fg="white", bg="black",
    bd=3, command= AddMed, relief=RIDGE, activebackground="black", activeforeground="white")
add_button.grid(row=0, column=0)

updatenew_button = Button(newframe, text="Update", font=("arial", 13, "bold"), width=13, fg="white", bg="black",
  bd=3, command= Update_med, relief=RIDGE, activebackground="black", activeforeground="white")
updatenew_button.grid(row=1, column=0)

delnew_button = Button(newframe, text="Delete", font=("arial", 13, "bold"), width=13, fg="white", bg="black",
       bd=3, relief=RIDGE, activebackground="black", activeforeground="white", command= Delete_med)
delnew_button.grid(row=2, column=0)

clr_button = Button(newframe, text="Clear", command= clear_med, font=("arial", 13, "bold"), width=13,
    fg="white", bg="black", bd=3, relief=RIDGE, activebackground="black", activeforeground="white")
clr_button.grid(row=3, column=0)

##### scrollbar frame in right frame ####
side_frame = Frame(right_frame, bd=4, relief=RIDGE, bg="dark green")
side_frame.place(x=0, y=160, width=250, height=150)

### scrollbar code ###

sc_x = ttk.Scrollbar(side_frame, orient=HORIZONTAL)
sc_y = ttk.Scrollbar(side_frame, orient=VERTICAL)
medicine_table = ttk.Treeview(side_frame, column=(
    "ref", "medname"), xscrollcommand=sc_x.set, yscrollcommand=sc_y.set)

sc_x.pack(side=BOTTOM, fill=X)
sc_y.pack(side=RIGHT, fill=Y)

sc_x.config(command= medicine_table.xview)
sc_y.config(command= medicine_table.yview)

medicine_table.heading("ref", text="Ref")
medicine_table.heading("medname", text="Medicine Name")

medicine_table["show"] = "headings"
medicine_table.pack(fill=BOTH, expand=1)

medicine_table.column("ref", width=100)
medicine_table.column("medname", width=100)

medicine_table.bind("<ButtonRelease-1>",medget_cursor)
fetch_datamed()

######### down frame #######
down_frame = Frame( root, bg='#1e85d0', bd=10, relief=RIDGE)
down_frame.place(x=0, y=522, width=1350, height=212)

########## scrollbar in down frame ########
scroll_frame = Frame(down_frame, bd=2, relief=RIDGE, bg="white")
scroll_frame.place(x=0, y=0, width=1330, height=192)

##### scrollbar code #####
scroll_x = ttk.Scrollbar(scroll_frame, orient=HORIZONTAL)
scroll_y = ttk.Scrollbar(scroll_frame, orient=VERTICAL)
info_table = ttk.Treeview(scroll_frame, column=("ref no", "comp name", "type", "medi name", "PRICE", "issue", "exp",
  "uses", "side effect"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)

scroll_x.config(command= info_table.xview)
scroll_y.config(command= info_table.yview)

info_table.heading("ref no", text="Ref No.")
info_table.heading("comp name", text="Company Name")
info_table.heading("type", text="Type Of Medicine")
info_table.heading("medi name", text="Medicine Name")
info_table.heading("PRICE", text="PRICE")
info_table.heading("issue", text="Issue Date")
info_table.heading("exp", text="Expiry Date")
info_table.heading("uses", text="Uses")
info_table.heading("side effect", text="Side Effects")
##info_table.heading("warning", text="Prec & Warning")
##info_table.heading("dosage", text="Dosage")
##info_table.heading("price", text="Medicine Price")
##info_table.heading("product", text="Product Qt.")

info_table["show"] = "headings"
info_table.pack(fill=BOTH, expand=1)

info_table.column("ref no", width=100)
info_table.column("comp name", width=100)
info_table.column("type", width=100)
info_table.column("medi name", width=100)
info_table.column("PRICE", width=100)
info_table.column("issue", width=100)
info_table.column("exp", width=100)
info_table.column("uses", width=100)
info_table.column("side effect", width=100)
##info_table.column("warning", width=100)
##info_table.column("dosage", width=100)
##info_table.column("price", width=100)
##info_table.column("product", width=100)

info_table.bind("<ButtonRelease-1>",get_cursor)

fetch_new()




##, "warning", "dosage", "price", "product"


