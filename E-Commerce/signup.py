from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import mysql.connector,pymysql
class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1500x800+0+0")
        self.root.resizable(False,False)
        # Setting Background Image
        self.bg = ImageTk.PhotoImage(file="Images/background.png")
        bg = Label(self.root, image = self.bg).place(x = 0, y = 0, relwidth=1,relheight=1)
        
        # calculate the center coordinates of the screen
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (1500 // 2)  # 300 is the width of the window
        y = (screen_height // 2) - (800 // 2)  # 150 is the height of the window
        
        # set the window position to the center of the screen
        root.geometry("1500x800+{}+{}".format(x, y))
       
        # Creation of Registration Frame
        frame1 = Frame(self.root,bg="white")
        frame1.place(x = 375, y = 200, width=750, height=400)
        
        title = Label(frame1, text = "Welcome to Our Family",font=("Times New Roman",20,"bold"),bg="white",fg="green").place(x= 50,y=30)
        
        # Row 1
        
        first_Name = Label(frame1, text = "First Name :",font=("Times New Roman",15,"bold"),bg="white",fg="gray").place(x= 50,y=100)
        self.txt_first_Name = Entry(frame1, font=("times new roman",15),bg="lightgray")
        self.txt_first_Name.place(x= 50,y=130, width=250)
        
        last_Name = Label(frame1, text = "Last Name :",font=("Times New Roman",15,"bold"),bg="white",fg="gray").place(x= 450,y=100)
        self.txt_last_Name = Entry(frame1, font=("times new roman",15),bg="lightgray")
        self.txt_last_Name.place(x= 450,y=130, width=250)
        
        # Row 2
        
        contact_num = Label(frame1, text = "Phone Number :",font=("Times New Roman",15,"bold"),bg="white",fg="gray").place(x= 50,y=160)
        self.txt_contact_num = Entry(frame1, font=("times new roman",15),bg="lightgray")
        self.txt_contact_num.place(x= 50,y=190, width=250)
        
        email_id = Label(frame1, text = "Email :",font=("Times New Roman",15,"bold"),bg="white",fg="gray").place(x= 450,y=160)
        self.txt_email_id = Entry(frame1, font=("times new roman",15),bg="lightgray")
        self.txt_email_id.place(x= 450,y=190, width=250)
        
        # Row 3
        
        question = Label(frame1, text = "Security Question :",font=("Times New Roman",15,"bold"),bg="white",fg="gray").place(x= 50,y=220)
        
        self.cmb_question = ttk.Combobox(frame1, font=("times new roman",13),state="readonly",justify="center")
        self.cmb_question['values'] =("Select","Your Pet Name","Your first Crush","Your Best Friends","Your Birth Place")
        self.cmb_question.place(x= 50,y=250, width=250)
        self.cmb_question.current(0)
        
        answer = Label(frame1, text = "Answer :",font=("Times New Roman",15,"bold"),bg="white",fg="gray").place(x= 450,y=220)
        self.txt_answer = Entry(frame1, font=("times new roman",15),bg="lightgray")
        self.txt_answer.place(x= 450,y=250, width=250)
        
        # Row 4
        
        password = Label(frame1, text = "Password :",font=("Times New Roman",15,"bold"),bg="white",fg="gray").place(x= 50,y=280)
        self.txt_password = Entry(frame1, font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x= 50,y=310, width=250)
        
        c_password = Label(frame1, text = "Confirm Password :",font=("Times New Roman",15,"bold"),bg="white",fg="gray").place(x= 450,y=280)
        self.txt_c_password = Entry(frame1, font=("times new roman",15),bg="lightgray")
        self.txt_c_password.place(x= 450,y=310, width=250)
        
        # T & C 
        self.var_chk = IntVar()
        chk = Checkbutton(frame1,text="I Agree to the Terms and Conditions of your WebApp", variable=self.var_chk,onvalue=1, offvalue=0 ,bg="white", font=("Times New Roman",10)).place(x=50,y=340)
        
        self.btn_image = ImageTk.PhotoImage(file="Images/signup.png",width="50",height="30")
        btn =Button(frame1,image = self.btn_image,bd=0,cursor="hand2",bg="white",command=self.register_data).place(x=490,y=340)
        
        self.btn1_image = ImageTk.PhotoImage(file="Images/login.png",width="50",height="30")
        btn =Button(frame1,image = self.btn1_image,bd=0,cursor="hand2",bg="white",command=self.login_window).place(x=570,y=340)
    
    def login_window(self):
        self.root.destroy()
        import login
    
    def clear(self):
        self.txt_first_Name.delete(0,END)
        self.txt_last_Name.delete(0,END)
        self.txt_contact_num.delete(0,END)
        self.txt_email_id.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_c_password.delete(0,END)
        self.cmb_question.current(0)
    
    def register_data(self):
        if self.txt_first_Name.get() == "" or self.txt_last_Name.get() == "" or self.txt_contact_num.get() == "" or self.txt_email_id.get()== "" or self.txt_answer.get() == "" or self.txt_c_password == "":
            messagebox.showerror("Error","Please enter valid credentials",parent=self.root)
        elif self.txt_password.get() != self.txt_c_password.get():
            messagebox.showerror("Error","Please enter correct password",parent=self.root)
        
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error","Please agree to our Policies",parent=self.root)
        
        else:
            try:
                con = pymysql.connect(host='localhost',user='root',password='toor',database='mypro')
                cur = con.cursor()
                cur.execute('select * from register where email=%s',self.txt_email_id.get())
                row = cur.fetchone()
                print(row)
                if row!= None:
                    messagebox.showerror("Error","Someone maybe You are already have registered previously!",parent=self.root)
                else:
                    cur.execute('insert into register (f_name,l_name,number,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)',
                                (self.txt_first_Name.get(),
                                 self.txt_last_Name.get(),
                                 self.txt_contact_num.get(),
                                 self.txt_email_id.get(),
                                 self.cmb_question.get(),
                                 self.txt_answer.get(),
                                 self.txt_password.get()                                
                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo('Success','Registration Successful')
                    self.clear()
            except Exception as es:
                messagebox.showinfo('Error',f'Error dure to {str(es)}',parent=self.root)      
            
root = Tk()
obj = Register(root)
root.mainloop()