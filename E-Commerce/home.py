# from tkinter import *
# from PIL import Image,ImageTk


# class dashboard:
#     def __init__(self,root):
#         self.root = root
#         self.root.title('Dashboard')
#         self.root.resizable(False,False)
        
#         # For creating the Background Image
#         self.bg = ImageTk.PhotoImage(file='Images/Dashboard.png')
#         bg = Label(self.root,image=self.bg).place(x = 0, y = 0, relwidth=1,relheight=1)
        

#         # calculate the x and y coordinates for the Tk root window
#         screen_width = root.winfo_screenwidth()
#         screen_height = root.winfo_screenheight()
#         print(screen_height,' ',screen_width)
#         x = int((screen_width/2) - (1500/2))
#         y = int((screen_height/2) - (800/2))

#         # To set center of the screen
#         self.root.geometry('1500x800+{}+{}'.format(x, y))
        
#         # Creating button for Search Screen
#         self.search_image = ImageTk.PhotoImage(file='Images/search_new_small.png')
#         btn = Button(image=self.search_image,bd=0,command=self.go_to_search,bg='#f6f6f6').place(x=1320,y=12)
        

#         # For Opening Search Window
#         self.user_image = ImageTk.PhotoImage(file='Images/Profile_img.png',width='50',height='50')
#         btn = Button(image=self.user_image,command=self.user_clicked,bg="#4db0f4", highlightthickness=0, bd=0).place(x=10,y=10)

#         # Ending the Frame for Header


#         # About Us Image
#         self.about_us_img = ImageTk.PhotoImage(file='Images/About_Us_Section.png')
#         about_us_img = Label(image=self.about_us_img,bg='#f6f6f6')
#         about_us_img.place(x = 200, y = 200)
        

#         # To create a function for Button
#         self.btn1_image = ImageTk.PhotoImage(file="Images/Logout (Blue).png")
#         btn = Button(image = self.btn1_image,bd=0,cursor="hand2",bg=None,command=self.Logout).place(x=1400,y = 20)

#         # Creating the Frame for Footer
#         frame2 = Frame(self.root,bg='#f6f6f6')
#         frame2.place(x = 5, y = 720, width=1490, height=74)
        
#         # Adding an image in frame2
#         self.img = ImageTk.PhotoImage(file='Images/Footer_Section.png')
#         img_label = Label(frame2, image=self.img,bg='#f6f6f6')
#         img_label.place(x = 0, y = 0)

        
#     # Creating Logout button
#     def Logout(self):
#         self.root.destroy()
#         import login
    
#     def user_clicked(self):
#         print('User clicked!!')

#     def go_to_search(self):
#         self.root.destroy()
#         import search
    

# root = Tk()
# obj = dashboard(root)
# root.mainloop()