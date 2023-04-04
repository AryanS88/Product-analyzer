from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk

class Product:
    def __init__(self,root):
        # Driver Code 
        self.root = root
        self.root.title("DashBoard")
        self.root.resizable(False,False)
        # calculate the center coordinates of the screen
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (1500 // 2)  # 300 is the width of the window
        y = (screen_height // 2) - (800 // 2)  # 150 is the height of the window
        
        # set the window position to the center of the screen
        root.geometry("1500x800+{}+{}".format(x, y))
        
        # Creating button for Search Screen
        self.search_image = ImageTk.PhotoImage(file='Images/search_new_small.png')
        btn = Button(image=self.search_image,bd=0,command=self.search,bg='#f6f6f6').place(x=1320,y=12)
        
        # For creating the Background Image
        self.bg = ImageTk.PhotoImage(file='Images/Dashboard.png')
        bg = Label(self.root,image=self.bg).place(x = 0, y = 0, relwidth=1,relheight=1)
        
        # --------Starting of the Header--------

        # For Opening Search Window
        self.user_image = ImageTk.PhotoImage(file='Images/Profile_img.png',width='50',height='50')
        btn = Button(image=self.user_image,command=self.user_clicked,bg="#f6f6f6", highlightthickness=0, bd=0).place(x=10,y=10)

        # To create a function for Button
        self.btn1_image = ImageTk.PhotoImage(file="Images/Logout (Blue).png")
        btn = Button(image = self.btn1_image,bd=0,cursor="hand2",bg=None,command=self.LogoutButton).place(x=1400,y = 20)
        
        # --------Ending of the Header--------
    
    
        # --------Starting of the Content--------
        
        self.recentimg1 = ImageTk.PhotoImage(file="Images/recentimg1.png",width=(400),height=(400))
        label_1 = Label(image=self.recentimg1,bg='#f6f6f6').place(x=75,y = 200)
        
        self.recentimg2 = ImageTk.PhotoImage(file="Images/recentimg1.png",width=(400),height=(400))
        label_1 = Label(image=self.recentimg1,bg='#f6f6f6').place(x=590,y = 200)
        
        self.recentimg3 = ImageTk.PhotoImage(file="Images/recentimg1.png",width=(400),height=(400))
        label_1 = Label(image=self.recentimg1,bg='#f6f6f6').place(x=1125,y = 200)
        
        # --------Ending of the Content-----------
    
    
        # --------Starting of the Footer--------
        frame2 = Frame(self.root,bg='#f6f6f6')
        frame2.place(x = 5, y = 720, width=1490, height=74)
        
        # Adding an image in frame2
        self.img = ImageTk.PhotoImage(file='Images/Footer_Section.png')
        img_label = Label(frame2, image=self.img,bg='#f6f6f6')
        img_label.place(x = 0, y = 0)

        # --------Ending of the Header--------
        
    def user_clicked(self):
        print('User clicked!!')
        
    def search(self):
        self.root.destroy()
        import search
    def LogoutButton(self):
        self.root.destroy()
        import login

root = Tk()
obj = Product(root)
root.mainloop()