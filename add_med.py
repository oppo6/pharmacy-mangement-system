from tkinter import *
from PIL import Image, ImageTk
import random
from tkinter import ttk, messagebox
import sqlite3
import os


root= Tk()
root.title("NEW MEDICINE")
root.geometry("450x380")
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
            except Exception as e:
                   messagebox.showerror("Error",f"Error due to:{str(e)}",parent= root)




def Delete_med( ):
        if  ref_variable.get()=="":
            messagebox.showerror("Error","Ref no is required",parent= root)
        else:

            try:
                    conn=sqlite3.connect(database=r'D:\Pharmacy_management-system-master\pharmacy.db')
                    my_cursor=conn.cursor()
                        
                    my_cursor.execute("Delete from pharma where Ref_no=? ", ref_variable.get())
                    conn.commit()
                    messagebox.showinfo("Delete","Successfully Deleted",parent= root)
                    fetch_datamed()
            except Exception as e:
                     messagebox.showerror("Error",f"Error due to:{str(e)}",parent= root)



def clear_med( ):
     ref_variable.set("")
     addmed_variable.set("")

right_frame = LabelFrame( bg='#1e85d0', bd=10, relief=RIDGE, padx=5,
text="New Medicine Add department", font=("arial", 13, "bold"), fg="white")
right_frame.place(x=0, y=0, width=450, height=380)

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

medicine_table.bind("<ButtonRelease-1>",  medget_cursor)
fetch_datamed()














