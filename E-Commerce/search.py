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
        
        # Create Base Frame
        frame1 = Frame(self.root, bg = "#fff")
        frame1.place(x = 350, y = 200, width = 800, height = 60)
        
        # title = Label(frame1, text = "Welcome to Our Family",font=("Times New Roman",20,"bold"),bg="white",fg="green").place(x= 50,y=30)
        self.search_img = ImageTk.PhotoImage(file = 'Images/search_new_small.png')
        btn = Button(frame1, bd = 0, bg = 'black', image = self.search_img).place(relx = 1.0, anchor="ne", relwidth = 0.08, relheight=1)








    def search(self):
        self.root.destroy()
        import search
root = Tk()
obj = Seach(root)
root.mainloop()