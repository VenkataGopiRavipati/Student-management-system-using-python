from tkinter import*
from course import *
from student import *
from results import  *
from report import *
from login import  *
class RMS:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Result management System")
        self.root.geometry("1340x700+0+0")  # width x height + x -axis + y- axis
        self.root.config(bg="white")
        title = Label(self.root, text="Student Result management System", font=("goudy old style", 20, "bold"),bg="#033054", fg="white").place(x=0,y=0,relwidth=1,height=50)
        # menu
        m_frame = LabelFrame(self.root, text="menu", font=("times new roman", 15), bg="white")
        m_frame.place(x=10, y=70, width=1340, height=80)
        # Buttons on menu
        btn_course = Button(m_frame, text="Course", font=("goudy old style", 15, "bold"), command=self.add_course,bg="#0b5377", fg="white", cursor="hand2").place(x=20, y=5, width=200, height=40)
        btn_student = Button(m_frame, text="Student", font=("goudy old style", 15, "bold"),command=self.add_student, bg="#0b5377", fg="white",cursor="hand2").place(x=240, y=5, width=200, height=40)
        btn_results = Button(m_frame, text="Student Results", font=("goudy old style", 15, "bold"), bg="#0b5377",fg="white", cursor="hand2",command=self.add_results).place(x=460, y=5, width=200, height=40)
        btn_view = Button(m_frame, text="View Student Results", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2",command=self.view_results).place(x=680, y=5, width=200, height=40)
        btn_logout = Button(m_frame, text="Logout", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2",command=self.logout).place(x=900, y=5, width=200, height=40)

        # UDPATE Details
        lbl_course = Label(self.root, text="Total courses \n [0]", font=("goudy old style", 20, "bold"), bd=10,relief=RIDGE, bg="#033054", fg="white")
        lbl_course.place(x=200, y=530, width=300, height=100)
        lbl_student = Label(self.root, text="Total Students \n [0]", font=("goudy old style", 20, "bold"), bd=10, relief=RIDGE, bg="#033054", fg="white")
        lbl_student.place(x=510, y=530, width=300, height=100)
        lbl_results =Label(self.root, text="Total Results \n [0]", font=("goudy old style", 20, "bold"), bd=10, relief=RIDGE, bg="#033054", fg="white")
        lbl_results.place(x=820, y=530, width=300, height=100)

        # Create a footer
        footer = Label(self.root, text="SRMS- Student Result management System \n For any quieries place contact number +1323xxxxx232",font=("goudy old style", 12), bg="#262626", fg="white").pack(side=BOTTOM, fill=X)
    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Courseclass(self.new_win)
    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Studentclass(self.new_win)

    def add_results(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Resultclass(self.new_win)
    def view_results(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Reportclass(self.new_win)

    def logout(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Login(self.new_win)
        # root.destroy()


if __name__ == "__main__":
    root =Tk()
    RMS(root)
    root.mainloop()