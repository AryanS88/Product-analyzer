from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import mysql.connector,pymysql
class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1500x800+0+0")
        self.root.resizable(False,False)
        # Setting Background Image
        self.bg = ImageTk.PhotoImage(file="Images/background.png")
        bg = Label(self.root, image = self.bg).place(x = 0, y = 0, relwidth=1,relheight=1)
        
        frame1 = Frame(self.root,bg="#CAF0F8")
        frame1.place(x = 375, y = 200, width=750, height=400)

        # calculate the center coordinates of the screen
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (1500 // 2)  # 300 is the width of the window
        y = (screen_height // 2) - (800 // 2)  # 150 is the height of the window
        
        # set the window position to the center of the screen
        root.geometry("1500x800+{}+{}".format(x, y))
        

        title = Label(frame1, text = "Welcome Back!", font=("Montserrat",20,"bold"),bg="#CAF0F8",fg="#1d3557").place(x= 150,y=30)
        
        # email Field in row 1
        
        email_id = Label(frame1, text = "Email :",font=("Montserrat",15,"bold"),bg="#CAF0F8",fg="gray").place(x= 250,y=100)
        self.txt_email_id = Entry( frame1, font=("Montserrat",15),bg="#90e0ef")
        self.txt_email_id.place(x= 250,y=130, width=250)
        
        # password Field in row 2
                
        password = Label( frame1, text = "Password :",font=("Montserrat",15,"bold"),bg="#CAF0F8",fg="gray").place(x= 250,y=160)
        self.txt_password = Entry( frame1, font=("Montserrat",15),bg="#90e0ef")
        self.txt_password.place(x= 250,y=190, width=250)
        
        # Registered Account Field
        btn_register = Button( frame1, cursor='hand2', text='Registered Account ?',command=self.register_window,font=("Montserrat",14),bg='#CAF0F8',bd=0,fg='#B00857').place(x =280,y =220)
        
        # Login Button
        
        # T & C 
        # self.var_chk = IntVar()
        # chk = Checkbutton(  text="I Agree to the Terms and Conditions of your WebApp", variable=self.var_chk,onvalue=1, offvalue=0 ,bg="white", font=("Montserrat",10)).place(x=216,y=260)
    
        self.btn_image = ImageTk.PhotoImage(file="Images/login.png",width="50",height="30")
        btn =Button(frame1,  image = self.btn_image,bd=0,cursor="hand2",command=self.login,bg="#CAF0F8").place(x=320,y=300,width=80,height=30)
        
    def register_window(self):
        self.root.destroy()
        import signup
    
    def login(self):
        if self.txt_email_id.get()=='' or self.txt_password.get()=='':
            messagebox.showerror('Error',"Please enter valid credentials",parent = self.root)
        else:
            try:
                con = pymysql.connect(host='localhost',user='root',password='toor',database='mypro')
                cur = con.cursor()
                cur.execute('select * from register where email=%s and password=%s',(self.txt_email_id.get(),self.txt_password.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror('Error',"Please enter valid username and password if not create one",parent = self.root)
                else:
                    messagebox.showinfo('Success','Welcome!',parent = self.root)
                    self.root.destroy()
                    import practice
                    
                con.close()
                   
            except Exception as es:
                messagebox.showerror('Error',f'Error due to {str(es)}',parent = self.root)
root = Tk()
obj = Login_window(root)
root.mainloop()