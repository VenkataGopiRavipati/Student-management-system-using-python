import sqlite3
from tkinter import*
from tkinter import ttk,messagebox

class Reportclass:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Result management System")
        self.root.geometry("1640x700+0+0")  # width x height + x -axis + y- axis
        self.root.config(bg="white")
        self.root.focus_force()
        #Title
        title = Label(self.root, text=" View Student Results", font=("goudy old style", 20, "bold"),bg="#009698", fg="white").place(x=10,y=15,width=1640,height=35)

        #search ================================================================================================================================================================

        self.var_search = StringVar()
        lbl_search = Label(self.root, text="Search by| Roll number ", font=("goudy old style", 16, "bold"), bg="white").place( x=300, y=140,width = 250,height=35)
        lbl_search_roll = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 16, "bold"),bg="white").place(x=550, y=140, width = 250,height=35)
        btn_search = Button(self.root, text="search", font=("goudy old style", 16, "bold"), bg="#4e922d", fg="white",cursor="hand2",command=self.search).place(x=810, y=140,width = 100,height=35)
        btn_clear = Button(self.root, text="clear", font=("goudy old style", 16, "bold"), bg="grey", fg="white",cursor="hand2",command=self.clear).place(x=920, y=140, width = 150,height=35)

        #labels ############################################################=================================
        lbl_roll = Label(self.root, text="Roll number ", font=("goudy old style", 16, "bold"), bg="white",bd=2,relief=GROOVE).place( x=250, y=230,width = 150,height=50)
        lbl_name = Label(self.root, text="Name ", font=("goudy old style", 16, "bold"), bg="white",bd=2,relief=GROOVE).place( x=400, y=230,width = 250,height=50)
        lbl_course = Label(self.root, text="Course ", font=("goudy old style", 16, "bold"), bg="white",bd=2,relief=GROOVE).place( x=650, y=230,width = 250,height=50)
        lbl_marks = Label(self.root, text="Marks ", font=("goudy old style", 16, "bold"), bg="white",bd=2,relief=GROOVE).place( x=900, y=230,width = 150,height=50)
        lbl_total_marks = Label(self.root, text="Total Marks ", font=("goudy old style", 16, "bold"), bg="white",bd=2,relief=GROOVE).place(x=1050, y=230,width = 150,height=50)


        self.roll = Label(self.root, font=("goudy old style", 16, "bold"), bg="white",bd=2,relief=GROOVE)
        self.roll .place( x=250, y=280,width = 150,height=50)
        self.name = Label(self.root,  font=("goudy old style", 16, "bold"), bg="white",bd=2,relief=GROOVE)
        self.name.place( x=400, y=280,width = 250,height=50)
        self.course = Label(self.root, font=("goudy old style", 16, "bold"), bg="white",bd=2,relief=GROOVE)
        self.course.place( x=650, y=280,width = 250,height=50)
        self.marks = Label(self.root,  font=("goudy old style", 16, "bold"), bg="white",bd=2,relief=GROOVE)
        self.marks.place( x=900, y=280,width = 150,height=50)
        self.total_marks = Label(self.root, font=("goudy old style", 16, "bold"), bg="white",bd=2,relief=GROOVE)
        self.total_marks.place(x=1050, y=280,width = 150,height=50)

        #delete btn
        btn_delete = Button(self.root, text="Delete", font=("goudy old style", 16, "bold"), bg="red", fg="white",cursor="hand2").place(x=600, y=360, width=120, height=40)

    def clear(self):
        self.var_search.set("")
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.total_marks.config(text="")

    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from result where roll=?", (self.var_search.get(),))
            row = cur.fetchone()
            if row != None:
                self.roll.config(text=row[1])
                self.name.config(text=row[2])
                self.course.config(text=row[3])
                self.marks.config(text=row[4])
                self.total_marks.config(text=row[5])
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Roll number is should be required", parent=self.root)
            else:
                cur.execute("select * from result where roll=?", (self.var_search.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Result", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("Delete from result where roll=?", (self.var_search.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Result has deleted Successfully ")
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")




if __name__ == "__main__":
    root =Tk()
    Reportclass(root)
    root.mainloop()