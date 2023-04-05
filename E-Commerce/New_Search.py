from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import webbrowser

class PlaceholderEntry(Entry):
    def __init__(self, master=None, placeholder="Enter query", color='#777777', **kwargs):
        super().__init__(master, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']
        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)
        self.delete(0, END)
        self.insert(0, self.placeholder)
        self.configure(fg=self.placeholder_color, bd = 0)

    def on_focus_in(self, event):
        if self['fg'] == self.placeholder_color:
            self.delete(0, END)
            self.configure(fg=self.default_fg_color)

    def on_focus_out(self, event):
        if not self.get():
            self.delete(0, END)
            self.insert(0, self.placeholder)
            self.configure(fg=self.placeholder_color)

class Search:
    def __init__(self,root):

        self.root = root
        # create the main window
        self.root.title("Search")
        self.root.configure(bg='#CAF0F8')

        # For creating the Background Image
        self.bg = ImageTk.PhotoImage(file='Images/Search_BG.png')
        bg = Label(self.root,image=self.bg).place(x = 0, y = 0, relwidth=1,relheight=1)

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
        frame1 = Frame(self.root, bg = '#93e5f6')
        frame1.place(x = 350, y = 200, width = 850, height = 70)

        # create an entry widget
        self.entry = PlaceholderEntry(frame1,width = 95, font=("Helvetica", 20), bg= '#CAF0F8')
        self.entry.pack(side=LEFT)

        def on_enter_pressed(event):
            name = self.entry.get()
            print("Hello,", name)

        # bind the Return key to the on_enter_pressed function
        self.entry.bind("<Return>", on_enter_pressed)
        
        self.search_img = ImageTk.PhotoImage(file = 'Images/search_new_new.png')
        btn = Button(frame1, command=self.search, border = NO, bg = '#93e5f6', image = self.search_img).place(relx = 1.0, anchor="ne", relwidth = 0.08, relheight=1)

        # # # Creating a back button
        self.back_image = ImageTk.PhotoImage(file = 'Images/back.png')
        btn = Button(command=self.back_func, image = self.back_image,bg='#CAF0F8',bd=0).place(x=20,y=20)
        
    def search(self):
        self.name = self.entry.get()
        url = 'http://amazon.com/search?q={}'.format(self.name)
        webbrowser.open(url)
        print('Searching...',self.name)
        self.root.destroy()
        import product
        
    def back_func(self):
        self.root.destroy()
        import dashboard    
root = Tk()
obj = Search(root)
root.mainloop()