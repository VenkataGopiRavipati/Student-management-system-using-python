from tkinter import *
import sys

from course import *
from Dashboard import *



class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Result management System")
        self.root.geometry("1340x700+0+0")  # width x height + x -axis + y- axis
        self.root.config(bg="white")
        title = Label(self.root, text="Student Result Management System Login Screen", font=("goudy old style", 20, "bold"),bg="#033054", fg="white").place(x=0,y=0,relwidth=1,height=50)

        # variables
        self.var_username = StringVar()
        self.var_password = StringVar()

        # labels
        lbl_login = Label(self.root, text="Login", font=("goudy old style", 18, "bold"), bg="white").place(x=957,y=120)
        lbl_course = Label(self.root, text="User Name", font=("goudy old style", 15, "bold"), bg="white").place(x=757,y=180)
        lbl_duration = Label(self.root, text="Password", font=("goudy old style", 15, "bold"), bg="white").place( x=757, y=240)
        self.btn_login = Button(self.root, text="Forget password", font=("goudy old style", 15, "bold"), bg="white", fg="red", cursor="hand2", command=self.forget_password).place( x=757, y=300)

        # edit text
        txt_username = Entry(self.root, textvariable=self.var_username, font=("goudy old style", 15, "bold"),bg="white").place(x=870, y=180,width=300, height=40)
        txt_password = Entry(self.root, textvariable=self.var_password, font=("goudy old style", 15, "bold"),bg="white",show="*").place(x=870, y=230,width=300, height=40)

        #buttons
        self.btn_login = Button(self.root, text="Login", font=("goudy old style", 15, "bold"), bg="#4e922d", fg="white",cursor="hand2", command= self.command1)
        self.btn_login.place(x=953, y=300, width=210, height=35)
        # txt_password.bind('<Return>', self.command1)

        #footer
        footer = Label(self.root, text="SRMS- Student Result management System \n For any quieries place contact number +1323xxxxx232",font=("goudy old style", 12), bg="#262626", fg="white").pack(side=BOTTOM, fill=X)


    def forget_password(self):
        self.root2 = Toplevel( )
        self.root2.title("Forget Password")
        self.root2.geometry("500x300+450+200")
        self.root2.config(bg="white")
        self.root2.focus_force()
        self.root2.grab_set()

        lbl_login = Label(self.root2, text="Forget Password", font=("goudy old style", 18, "bold"), bg="#033054", fg="white").place(x=0,y=15,relwidth=1,height=50)
        lbl_dob = Label(self.root2, text="D.O.B", font=("goudy old style", 16, "bold"), bg="white").place(x=5,y=85)
        lbl_password = Label(self.root2, text="New Password", font=("goudy old style", 16, "bold"), bg="white").place(x=5,y=115)
        lbl_re_password = Label(self.root2, text="ReType New Password", font=("goudy old style", 16, "bold"), bg="white").place(x=5,y=145)

        txt_username = Entry(self.root2, textvariable=self.var_username, font=("goudy old style", 15, "bold"),bg="white").place(x=270, y=85, width=200, height=25)
        txt_password = Entry(self.root2, textvariable=self.var_password, font=("goudy old style", 15, "bold"),bg="white", show="*").place(x=270, y=115, width=200, height=25)
        txt_password2 = Entry(self.root2, textvariable=self.var_password, font=("goudy old style", 15, "bold"),bg="white", show="*").place(x=270, y=145, width=200, height=25)

        self.btn_login = Button(self.root2, text="Submit", font=("goudy old style", 15, "bold"), bg="#4e922d", fg="white",cursor="hand2", command=self.command1)
        self.btn_login.place(x=350, y=180, width=120, height=30)




    def command1(self):
        if self.var_username.get() == 'admin' and self.var_password.get() == 'password' or self.var_username.get() == 'Login' and self.var_password.get() == 'pass':
                # root.deiconify() #"unhide" a window that was previously hidden using the iconify() method
                # top.destroy()   # close a window and destroy its contents
            self.new_win = Toplevel(self.root)
            self.new_obj = RMS(self.new_win)
        else:
            self.new_win = Toplevel(self.root)
            self.new_obj = Courseclass(self.new_win)









if __name__ == "__main__":
    root =Tk()
    Login(root)
    root.mainloop()