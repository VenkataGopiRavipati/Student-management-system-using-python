import sqlite3
from tkinter import*
from tkinter import ttk,messagebox
from Dashboard import *

class Studentclass:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Result management System")
        self.root.geometry("1640x700+0+0")  # width x height + x -axis + y- axis
        self.root.config(bg="white")
        self.root.focus_force()
        #home button
        self.btn_add = Button(self.root, text="Home", font=("goudy old style", 15, "bold"), bg="#033054", fg="white",cursor="hand2", command=self.Home)
        self.btn_add.place(x=5, y=15, width=55, height=35)

        #Title
        title = Label(self.root, text=" Manage Student Details", font=("goudy old style", 20, "bold"),bg="#033054", fg="white").place(x=61,y=15,width=1640,height=35)

        #variables
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email= StringVar()
        self.var_gender= StringVar()
        self.var_address= StringVar()
        self.var_state= StringVar()
        self.var_city= StringVar()
        self.var_zip= StringVar()
        self.var_dob= StringVar()
        self.var_contact = StringVar()
        self.var_status = StringVar()
        self.var_course = StringVar()





        # widgets
        # Column 1
        lbl_roll = Label(self.root, text="Roll Number", font=("goudy old style", 15, "bold"),bg="white").place(x=10,y=60)
        lbl_name= Label(self.root, text="Name", font=("goudy old style", 15, "bold"),bg="white").place(x=10,y=100)
        lbl_email = Label(self.root, text="Email id", font=("goudy old style", 15, "bold"),bg="white").place(x=10,y=140)
        lbl_gender = Label(self.root, text="Gender", font=("goudy old style", 15, "bold"),bg="white").place(x=10,y=180)
        lbl_address= Label(self.root, text="Address", font=("goudy old style", 15, "bold"),bg="white").place(x=10,y=220)

        lbl_state= Label(self.root, text="State", font=("goudy old style", 15, "bold"),bg="white").place(x=10,y=280)
        lbl_city= Label(self.root, text="City", font=("goudy old style", 15, "bold"),bg="white").place(x=310,y=280)
        lbl_zip= Label(self.root, text="Zip", font=("goudy old style", 15, "bold"),bg="white").place(x=510,y=280)





        # Column 2
        lbl_roll = Label(self.root, text="D.O.B ", font=("goudy old style", 15, "bold"), bg="white").place(x=380, y=60)
        lbl_name = Label(self.root, text="Contact", font=("goudy old style", 15, "bold"), bg="white").place(x=380, y=100)
        lbl_email = Label(self.root, text="course", font=("goudy old style", 15, "bold"), bg="white").place(x=380,y=140)
        lbl_gender = Label(self.root, text="Account Status", font=("goudy old style", 15, "bold"), bg="white").place(x=380,y=180)

        #EDIT field1
        self.gender_list =["Male","Female","Other"]
        self.txt_roll = Entry(self.root,textvariable=self.var_roll,font=("goudy old style", 15, "bold"),bg="white")
        self.txt_roll.place(x=170,y=60, width=200)
        txt_name = Entry(self.root,textvariable=self.var_name,  font=("goudy old style", 15, "bold"),bg="white").place(x=170,y=100,width=200)
        txt_email = Entry(self.root, textvariable=self.var_email, font=("goudy old style", 15, "bold"),bg="white").place(x=170,y=140,width=200)
        self.txt_gender = ttk.Combobox(self.root, textvariable=self.var_gender,values=self.gender_list, font=("goudy old style", 15, "bold"),state = "readonly")
        self.txt_gender.place(x=170,y=180,width=200)
        self.txt_gender.set("Select")
        self.txt_address = Text(self.root,font=("goudy old style", 15, "bold"),bg="white")
        self.txt_address .place(x=170,y=220,width=500,height=30)
        txt_state = Entry(self.root,textvariable=self.var_state,  font=("goudy old style", 15, "bold"),bg="white").place(x=170,y=280,width=120)
        txt_city = Entry(self.root,textvariable=self.var_city,  font=("goudy old style", 15, "bold"),bg="white").place(x=360,y=280,width=120)
        txt_zip = Entry(self.root,textvariable=self.var_zip,  font=("goudy old style", 15, "bold"),bg="white").place(x=550,y=280,width=120)

        # EDIT field2
        self.course_list=["Enable", "Disable"]
        self.txt_dob = Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 15, "bold"), bg="white")
        self.txt_dob.place(x=520, y=60, width=200)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15, "bold"), bg="white").place(x=520, y=100, width=200)
        txt_course = Entry(self.root, textvariable=self.var_course, font=("goudy old style", 15, "bold"),bg="white").place(x=520, y=140, width=200)
        self.txt_status = ttk.Combobox(self.root, textvariable=self.var_status,values=self.course_list,font=("goudy old style", 15, "bold"), state="readonly")
        self.txt_status.place(x=520, y=180, width=200)
        self.txt_status.set("Select")


        #Buttons
        self.btn_add = Button(self.root, text="Save", font=("goudy old style", 15, "bold"),bg="#4e922d", fg="white", cursor="hand2",command=self.add)
        self.btn_add.place(x=170, y=340, width=110, height=40)
        self.btn_update = Button(self.root, text="Update", font=("goudy old style", 15, "bold"), bg="#dc6523", fg="white", cursor="hand2",command=self.update)
        self.btn_update.place(x=290, y=340, width=110, height=40)
        self.btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15, "bold"), bg="#d23b16", fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=410, y=340, width=110, height=40)
        self.btn_clear = Button(self.root, text=" Clear", font=("goudy old style", 15, "bold"), bg="#b4a19c",fg="white", cursor="hand2",command=self.clear)
        self.btn_clear.place(x=530, y=340, width=110, height=40)

        # search panel
        self.var_search = StringVar()
        lbl_search = Label(self.root, text="Roll number ", font=("goudy old style", 15, "bold"),bg="white").place(x=740,y=60)
        lbl_search_roll = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, "bold"),bg="white").place(x=870, y=60, width=180)
        btn_search = Button(self.root, text="search", font=("goudy old style", 15, "bold"), bg="#4e922d", fg="white", cursor="hand2",command=self.search).place(x=1070, y=60, width=120, height=28)

        # contents\

        self.C_Frame = Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=740,y=100,width=635,height=340)

        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        self.Coursetable = ttk.Treeview (self.C_Frame,columns=("roll","name","email","gender","dob","contact","course","account_status","address","state","city","zip"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.Coursetable.xview)
        scrolly.config(command=self.Coursetable.yview)
        self.Coursetable.heading("roll",text="Roll Number")
        self.Coursetable.heading("name",text="Name")
        self.Coursetable.heading("email",text="Email")
        self.Coursetable.heading("gender",text="Gender")
        self.Coursetable.heading("dob",text="DOB")
        self.Coursetable.heading("contact",text="Contact number")
        self.Coursetable.heading("course",text="course")
        self.Coursetable.heading("account_status",text="Account status")
        self.Coursetable.heading("address",text="Address")
        self.Coursetable.heading("state",text="State")
        self.Coursetable.heading("city",text="City")
        self.Coursetable.heading("zip",text="Zip")
        self.Coursetable["show"]='headings'
        self.Coursetable.column("roll", width=100)
        self.Coursetable.column("name", width=100)
        self.Coursetable.column("email", width=100)
        self.Coursetable.column("gender", width=100)
        self.Coursetable.column("dob",width=150)
        self.Coursetable.column("contact",width=150)
        self.Coursetable.column("course",width=150)
        self.Coursetable.column("account_status",width=150)
        self.Coursetable.column("address",width=150)
        self.Coursetable.column("state",width=150)
        self.Coursetable.column("city",width=150)
        self.Coursetable.column("zip",width=150)


        self.Coursetable.pack(fill=BOTH,expand=1)
        self.Coursetable.bind("<ButtonRelease-1>",self.get_data)
        self.show()



        #footer
        footer = Label(self.root, text="SRMS- Student Result management System \n For any quieries place contact number +1323xxxxx232",font=("goudy old style", 12), bg="#262626", fg="white").pack(side=BOTTOM, fill=X)
    #===================Functions ================================

    def Home(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = RMS(self.new_win)
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from student where roll=?", (self.var_search.get(),))
            rows = cur.fetchall()
            if rows != None:
                self.Coursetable.delete(*self.Coursetable.get_children())
                for row in rows:
                    self.Coursetable.insert('', END, values=row)
            else:
                messagebox.showerror("Error","No record found",parent=self.root)



        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll number is should be required", parent=self.root)
            else:
                cur.execute("select * from student where roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please select students from list first", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op== True:
                        cur.execute("Delete from student where roll=?", (self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","student  has deleted Successfully ")
                        self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    def clear(self):
        self.show()
        self.var_roll.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set(""),
        self.var_dob.set(""),
        self.var_status.set(""),
        self.var_course.set(""),
        self.txt_address.delete("1.0", END),
        self.txt_address.insert(END, ""),
        self.var_state.set(""),
        self.var_city.set(""),
        self.var_contact.set(""),
        self.var_zip.set(""),


        self.txt_roll.config(state=NORMAL)

    def get_data(self,ev):

        r = self.Coursetable.focus()
        content = self.Coursetable.item(r)
        row = content["values"]
        self.var_roll.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_dob.set(row[4]),
        self.var_contact.set(row[5]),
        self.var_status.set(row[7]),
        self.var_course.set(row[6]),
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END, row[8])

        self.var_state.set(row[9]),
        self.var_city.set(row[10]),
        self.var_zip.set(row[11]),




    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from student ")
            rows = cur.fetchall()
            self.Coursetable.delete(*self.Coursetable.get_children())
            for row in rows:
                self.Coursetable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    # def fetch_course(self):
    #     con = sqlite3.connect(database="rms.db")
    #     cur = con.cursor()
    #     try:
    #         cur.execute("select name from course")
    #         rows = cur.fetchall()
    #         if len(rows)>0:
    #             for row in rows:
    #                 self.course_list.append(row[0])
    #     except Exception as ex:
    #         messagebox.showerror("Error", f"Error due to {str(ex)}")

    def update(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error","Roll Number and Name should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "select student from the list", parent=self.root)
                else:
                    cur.execute("update student set name=?,email=?,gender=?,dob=?,contact=?,course=?,account_status=?,address=?,state=?,city=?,zip=? where roll=? ",(
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_course.get(),
                        self.var_status.get(),
                        self.txt_address.get("1.0", END),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_zip.get(),
                        self.var_roll.get(),

                    ))
                    con.commit()
                    messagebox.showinfo("Success","Details updated Sucessfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error","Roll number should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Student details are already present", parent=self.root)
                else:
                    cur.execute("insert into student (roll,name,email,gender,dob,contact,course,account_status,address,state,city,zip) values(?, ?, ?, ?,?, ?, ?, ?, ?,?,?,?) ",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_course.get(),
                        self.var_status.get(),
                        self.txt_address.get("1.0", END),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_zip.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student Added Sucessfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")




if __name__ == "__main__":
    root =Tk()
    Studentclass(root)
    root.mainloop()