import sqlite3
from tkinter import*
from tkinter import ttk,messagebox

class Resultclass:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Result management System")
        self.root.geometry("1640x700+0+0")  # width x height + x -axis + y- axis
        self.root.config(bg="white")
        self.root.focus_force()
        #Title
        title = Label(self.root, text=" Manage Student Results", font=("goudy old style", 20, "bold"),bg="#009698", fg="white").place(x=10,y=15,width=1640,height=35)
        #variables
        self.roll_list=[]
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_full_marks = StringVar()
        self.fetch_roll()

        #labels
        lbl_roll = Label(self.root, text="Roll Number", font=("goudy old style", 15, "bold"), bg="white").place(x=10,y=60)
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=100)
        lbl_Course = Label(self.root, text="Course", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=140)
        lbl_marks = Label(self.root, text="Marks", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=180)
        lbl_fullmarks = Label(self.root, text="Full Marks", font=("goudy old style", 15, "bold"), bg="white").place(x=10,y=220)

        #edit box

        self.txt_roll = ttk.Combobox(self.root, textvariable=self.var_roll, values=self.roll_list,font=("goudy old style", 15, "bold"), state="readonly")
        self.txt_roll.place(x=240, y=60, width=200)
        self.txt_roll.set("Select")
        btn_search = Button(self.root, text="search", font=("goudy old style", 15, "bold"), bg="#4e922d", fg="white", cursor="hand2",command=self.search).place(x=470, y=60, width=120, height=28)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15, "bold"),bg="white",state='readonly').place(x=240, y=100, width=400)
        txt_course= Entry(self.root, textvariable=self.var_course, font=("goudy old style", 15, "bold"),bg="white").place(x=240, y=140, width=400)
        txt_marks = Entry(self.root, textvariable=self.var_marks, font=("goudy old style", 15, "bold"),bg="white").place(x=240, y=180, width=400)
        txt_full_marks = Entry(self.root, textvariable=self.var_full_marks, font=("goudy old style", 15, "bold"),bg="white").place(x=240, y=220, width=400)






        # Buttons
        self.btn_submit = Button(self.root, text="Submit ", font=("goudy old style", 15, "bold"), bg="grey", fg="white",cursor="hand2", command=self.submit)
        self.btn_submit.place(x=170, y=280, width=110, height=40)
        self.btn_clear = Button(self.root, text="Update", font=("goudy old style", 15, "bold"), bg="#dc6523",fg="white", cursor="hand2",command=self.clear)
        self.btn_clear.place(x=290, y=280, width=110, height=40)

    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select name,course from student where roll=?", (self.var_roll.get(),))
            row = cur.fetchone()
            if row != None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def fetch_roll(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select roll from student")
            rows = cur.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.roll_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def clear(self):
        self.var_roll.set("Select"),
        self.var_name.set(""),
        self.var_course.set(""),
        self.var_marks.set(""),
        self.var_full_marks.set(""),

    def submit(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll number should be required", parent=self.root)
            else:
                cur.execute("select * from result where roll=? and course=?", (self.var_roll.get(),self.var_course.get()))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Results was  already present", parent=self.root)
                else:
                    per = (int(self.var_marks.get())*100)/int(self.var_full_marks.get())
                    cur.execute(
                        "insert into result (roll,name,course,marks,full_marks) values(?, ?, ?, ?,?) ",
                        (
                            self.var_roll.get(),
                            self.var_name.get(),
                            self.var_course.get(),
                            self.var_marks.get(),
                            self.var_full_marks.get(),
                            # str(per)
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Result Added Sucessfully", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")




if __name__ == "__main__":
    root =Tk()
    Resultclass(root)
    root.mainloop()