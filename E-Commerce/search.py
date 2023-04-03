from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk

class Search:
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
        frame1 = Frame(self.root, bg = None)
        frame1.place(x = 350, y = 200, width = 800, height = 60)
        
        # create a label widget
        label = Label(frame1, text="Type here", width = 10, font=("Arial", 15), bg= None)
        label.pack(side=LEFT)

        # create an entry widget
        entry = Entry(frame1, width = 95, font=("Arial", 25),bg= None)
        entry.pack(side=LEFT)

        def on_enter_pressed(event):
            name = entry.get()
            print("Hello,", name)

        # bind the Return key to the on_enter_pressed function
        entry.bind("<Return>", on_enter_pressed)

        
        self.search_img = ImageTk.PhotoImage(file = 'Images/search_new_small.png')
        btn = Button(frame1, command=self.search, border = NO, bg = '#f0f0f0', image = self.search_img).place(relx = 1.0, anchor="ne", relwidth = 0.08, relheight=1)

    def search(self):
        self.root.destroy()
        import product
        
root = Tk()
obj = Search(root)
root.mainloop()