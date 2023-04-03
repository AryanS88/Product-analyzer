from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk

class Home:
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
        
        # For changing the background color
        self.root.config(bg='white')
        
        #Header section code starts below
        header = Frame(self.root,bg="grey",borderwidth=30)
        header.pack(side=TOP,fill="x")

        self.Profile_image = ImageTk.PhotoImage(file="Images/profileimg.png",width=(100),height=(100))
        label1 = Label(header,image=self.Profile_image,background="grey")
        label1.pack(side=LEFT,anchor="ne")

        label2 = Label(header,text="Product Analyser",background="grey",font="bold")
        label2.pack()

        LoginButton = Button(header,width=(10),height=(2),fg="black",text="Logout",relief=SUNKEN,cursor="hand2",command=self.LogoutButton)
        LoginButton.pack(side=RIGHT,anchor="se")
        #Header section code ends here

        #Footer section code starts here

        footer = Frame(root,bg="grey",borderwidth=30)
        footer.pack(side=BOTTOM,fill="x")

        label3 = Label(footer,text="About Us",background="grey")
        label3.pack(side=LEFT)

        #Footer section code ends here
        
        #Main Body section code starts here

        body = Frame(root,bg="black",borderwidth=63)
        body.pack(side="left",fill="both")

        self.recentimg1 = ImageTk.PhotoImage(file="Images/recentimg1.png",width=(300),height=(300))
        label4 = Label(body,image=self.recentimg1)
        label4.pack(side=LEFT,anchor="ne",padx="10")

        self.recentimg2 = PhotoImage(file="Images/recentimg1.png",width=(300),height=(300))
        label5 = Label(body,image=self.recentimg2)
        label5.pack(side=LEFT,anchor="ne",padx="10")

        self.recentimg3 = ImageTk.PhotoImage(file="Images/recentimg1.png",width=(300),height=(300))
        label6 = Label(body,image=self.recentimg3)
        label6.pack(side=LEFT,anchor="ne",padx="10")

        self.recentimg4 = ImageTk.PhotoImage(file="Images/recentimg1.png",width=(300),height=(300))
        label7 = Label(body,image=self.recentimg4)
        label7.pack(side=LEFT,anchor="ne",padx="10")

        Continuebutton = Button(body,width=(15),height=(2),fg="black",text="Continue to search",relief=SUNKEN,cursor="hand2",command=self.search)
        Continuebutton.pack(side=BOTTOM,anchor="se")
        #Main body section code ends here
    def search(self):
        self.root.destroy()
        import search
    def LogoutButton(self):
        self.root.destroy()
        import login

root = Tk()
obj = Home(root)
root.mainloop()