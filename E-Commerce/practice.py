from tkinter import *
from PIL import Image,ImageTk


class dashboard:
    def __init__(self,root):
        self.root = root
        self.root.title('Dashboard')
        self.root.resizable(False,False)
        
        # For creating the Background Image
        self.bg = ImageTk.PhotoImage(file='Python_Mini_Project/Images/Dashboard.png')
        bg = Label(self.root,image=self.bg).place(x = 0, y = 0, relwidth=1,relheight=1)
        
        # calculate the x and y coordinates for the Tk root window
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        print(screen_height,' ',screen_width)
        x = int((screen_width/2) - (1500/2))
        y = int((screen_height/2) - (800/2))

        # To set center of the screen
        self.root.geometry('1500x800+{}+{}'.format(x, y))
        
        
        # Creating the Frame for Header
        frame1 = Frame(self.root,bg='grey')
        frame1.place(x = 5, y = 5, width=1490, height=80)
        
        self.user_image = ImageTk.PhotoImage(file='Python_Mini_Project/Images/Profileimg1.png',width='50',height='50')
        btn = Button(frame1,image=self.user_image,bd=0,command=self.user_clicked,bg='grey').place(x=10,y=10)
        # Ending the Frame for Header
        
        # Creating About US Frame
        frame3 = Frame(self.root,bg='grey')
        frame3.place(x = 200, y = 200, width=1100, height=400)

        # To create a function for Button
        # LogoutButton = Button(frame1,text='Logout').place(x =1400,y = 5)
        self.btn1_image = ImageTk.PhotoImage(file="Python_Mini_Project/Images/Logout.png",width="50",height="30")
        btn =Button(frame1,image = self.btn1_image,bd=0,cursor="hand2",bg="grey",command=self.Logout).place(x=1400,y=5)

        # Creating the Frame for Footer
        frame2 = Frame(self.root,bg='grey')
        frame2.place(x = 5, y = 720, width=1490, height=74)
        
        # Adding an image in frame2
        self.img = ImageTk.PhotoImage(file='Python_Mini_Project/Images/Footer_Section.png')
        img_label = Label(frame2, image=self.img,bg='grey')
        img_label.place(x = 0, y = 0)

        
    # Creating Logout button
    def Logout(self):
        self.root.destroy()
        import login
    
    def user_clicked(self):
        print('User clicked!!')
    
    
if __name__ == '__main__':
    root = Tk()
    obj = dashboard(root)
    root.mainloop()
