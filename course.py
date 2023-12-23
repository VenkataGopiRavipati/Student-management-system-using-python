import sqlite3
from tkinter import*
from tkinter import ttk,messagebox

class Courseclass:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Result management System")
        self.root.geometry("1340x700+0+0")  # width x height + x -axis + y- axis
        self.root.config(bg="white")
        self.root.focus_force()
        #Title
        title = Label(self.root, text="Course Management Details", font=("goudy old style", 20, "bold"),bg="#033054", fg="white").place(x=10,y=15,width=1340,height=35)

        #variables
        self.var_course = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()

        # widgets
        lbl_course = Label(self.root, text="Course Name", font=("goudy old style", 15, "bold"),bg="white").place(x=10,y=60)
        lbl_duration = Label(self.root, text="Course Duration", font=("goudy old style", 15, "bold"),bg="white").place(x=10,y=100)
        lbl_charges = Label(self.root, text="Course Charges", font=("goudy old style", 15, "bold"),bg="white").place(x=10,y=140)
        lbl_description = Label(self.root, text="Description", font=("goudy old style", 15, "bold"),bg="white").place(x=10,y=180)

        self.txt_course = Entry(self.root,textvariable=self.var_course,font=("goudy old style", 15, "bold"),bg="white")
        self.txt_course.place(x=170,y=60, width=200)
        txt_duration = Entry(self.root,textvariable=self.var_duration,  font=("goudy old style", 15, "bold"),bg="white").place(x=170,y=100)
        txt_charges = Entry(self.root, textvariable=self.var_charges, font=("goudy old style", 15, "bold"),bg="white").place(x=170,y=140)
        self.txt_description = Text(self.root,font=("goudy old style", 15, "bold"),bg="white")
        self.txt_description.place(x=170,y=180,width=500,height=100)

        #Buttons
        self.btn_add = Button(self.root, text="Save", font=("goudy old style", 15, "bold"),bg="#4e922d", fg="white", cursor="hand2",command=self.add)
        self.btn_add.place(x=170, y=300, width=110, height=40)
        self.btn_update = Button(self.root, text="Update", font=("goudy old style", 15, "bold"), bg="#dc6523", fg="white", cursor="hand2",command=self.update)
        self.btn_update.place(x=290, y=300, width=110, height=40)
        self.btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15, "bold"), bg="#d23b16", fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=410, y=300, width=110, height=40)
        self.btn_clear = Button(self.root, text=" Clear", font=("goudy old style", 15, "bold"), bg="#b4a19c",fg="white", cursor="hand2",command=self.clear)
        self.btn_clear.place(x=530, y=300, width=110, height=40)

        # search panel
        self.var_search = StringVar()
        lbl_search = Label(self.root, text="Course Name ", font=("goudy old style", 15, "bold"),bg="white").place(x=720,y=60)
        lbl_search_course = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, "bold"),bg="white").place(x=870, y=60, width=180)
        btn_search = Button(self.root, text="search", font=("goudy old style", 15, "bold"), bg="#4e922d", fg="white", cursor="hand2").place(x=1070, y=60, width=120, height=28)

        # contents
        self.C_Frame = Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=515,height=340)

        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        self.Coursetable = ttk.Treeview (self.C_Frame,columns=("cid","name","duration","charges","description"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.Coursetable.xview)
        scrolly.config(command=self.Coursetable.yview)
        self.Coursetable.heading("cid",text="Course ID")
        self.Coursetable.heading("name",text="Name")
        self.Coursetable.heading("duration",text="Duration")
        self.Coursetable.heading("charges",text="Charges")
        self.Coursetable.heading("description",text="Description")
        self.Coursetable["show"]='headings'
        self.Coursetable.column("cid", width=100)
        self.Coursetable.column("name", width=100)
        self.Coursetable.column("duration", width=100)
        self.Coursetable.column("charges", width=100)
        self.Coursetable.column("description",width=150)


        self.Coursetable.pack(fill=BOTH,expand=1)
        self.Coursetable.bind("<ButtonRelease-1>",self.get_data)
        self.show()



        #footer
        footer = Label(self.root, text="SRMS- Student Result management System \n For any quieries place contact number +1323xxxxx232",font=("goudy old style", 12), bg="#262626", fg="white").pack(side=BOTTOM, fill=X)
    #===================Functions ================================
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute(f"select * from course where name like '%{self.var_course.get()}%'")
            rows = cur.fetchall()
            self.Coursetable.delete(*self.Coursetable.get_children())
            for row in rows:
                self.Coursetable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course Name should be required", parent=self.root)
            else:
                cur.execute("select * from course where name=?", (self.var_course.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please select course from list first", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op== True:
                        cur.execute("Delete from course where name=?", (self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Course has deleted Successfully ")
                        self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_description.delete('1.0', END)
        self.txt_courseName.config(state=NORMAL)

    def get_data(self,ev):

        r = self.Coursetable.focus()
        content = self.Coursetable.item(r)
        row = content["values"]
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[4])

    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from course ")
            rows = cur.fetchall()
            self.Coursetable.delete(*self.Coursetable.get_children())
            for row in rows:
                self.Coursetable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def update(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error","Course Name should be required",parent=self.root)
            else:
                cur.execute("select * from course where name=?", (self.var_course.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "select course from the list", parent=self.root)
                else:
                    cur.execute("update course set duration=?, charges=?, description=? where name=? ",(
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0", END),
                        self.var_course.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course updated Sucessfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error","Course Name should be required",parent=self.root)
            else:
                cur.execute("select * from course where name=?", (self.var_course.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Course Name already present", parent=self.root)
                else:
                    cur.execute("insert into course (name, duration, charges, description) values(?, ?, ?, ?) ",(
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0", END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course Added Sucessfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")




if __name__ == "__main__":
    root =Tk()
    Courseclass(root)
    root.mainloop()