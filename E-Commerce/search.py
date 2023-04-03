from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk

class Seach:
    def __init__(self,root):

        self.root = root
        # create the main window
        self.root.title("Search")

        # disable the maximize button
        root.resizable(False, False)

        # calculate the center coordinates of the screen
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (1500 // 2)  # 300 is the width of the window
        y = (screen_height // 2) - (800 // 2)  # 150 is the height of the window

        # set the window position to the center of the screen
        root.geometry("1500x800+{}+{}".format(x, y))
        
        # Creation of Registration Frame 
        frame1 = Frame(self.root,bg="black")
        frame1.place(x = 200, y = 150, width=800, height=60)
        
        # title = Label(frame1, text = "Welcome to Our Family",font=("Times New Roman",20,"bold"),bg="white",fg="green").place(x= 50,y=30)
        








    def search(self):
        self.root.destroy()
        import search
root = Tk()
obj = Seach(root)
root.mainloop()