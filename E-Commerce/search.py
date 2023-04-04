from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk

class TextEntryWithPlaceholder(Frame):
    def __init__(self, parent, placeholder, width=600, height = 1.4, font=("Helvetica", 18)):
        super().__init__(parent)
        
        # create a Text widget
        self.text = Text(self, height=height, width=width, font=font)
        self.text.pack(side=LEFT)

        # add placeholder text
        self.placeholder = placeholder
        self.text.insert(1.0, self.placeholder)
        self.text.tag_configure("placeholder", font=font, foreground="#d1d1d1")
        self.text.tag_add("placeholder", 1.0, "end")

        # bind events
        self.text.bind("<FocusIn>", self.on_focus_in)
        self.text.bind("<FocusOut>", self.on_focus_out)

    def on_focus_in(self, event):
        if self.text.get("1.0", "end-1c") == self.placeholder:
            self.text.delete("1.0", "end")
            self.text.tag_configure("placeholder", foreground="black")

    def on_focus_out(self, event):
        if not self.text.get("1.0", "end-1c"):
            self.text.insert(1.0, self.placeholder)
            self.text.tag_configure("placeholder", foreground="#d1d1d1")

# class PlaceholderEntry(Entry):
#     def __init__(self, master=None, placeholder="Enter text", color='#d1d1d1', **kwargs):
#         super().__init__(master, **kwargs)
#         self.placeholder = placeholder
#         self.placeholder_color = color
#         self.default_fg_color = self['fg']
#         self.bind("<FocusIn>", self.on_focus_in)
#         self.bind("<FocusOut>", self.on_focus_out)
#         self.delete(0, END)
#         self.insert(0, self.placeholder)
#         self.configure(fg=self.placeholder_color)

#     def on_focus_in(self, event):
#         if self['fg'] == self.placeholder_color:
#             self.delete(0, END)
#             self.configure(fg=self.default_fg_color)

#     def on_focus_out(self, event):
#         if not self.get():
#             self.delete(0, END)
#             self.insert(0, self.placeholder)
#             self.configure(fg=self.placeholder_color)

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
        
        # # create a label widget
        # label = Label(frame1, text="Type here", width = 10, font=("Arial", 15), bg= None)
        # label.pack(side=LEFT)

        # # create an entry widget
        # entry = PlaceholderEntry(frame1, width = 95, font=("Arial", 18),bg= None)
        # entry.pack(side=LEFT)

        # Text Entry Widget
        entry = TextEntryWithPlaceholder(frame1, "Enter your name:")
        entry.pack()

        # def on_enter_pressed(event):
        #     name = entry.get()
        #     print("Hello,", name)

        # # bind the Return key to the on_enter_pressed function
        # entry.bind("<Return>", on_enter_pressed)

        
        self.search_img = ImageTk.PhotoImage(file = 'Images/search_new_small.png')
        btn = Button(frame1, command=self.search, border = NO, bg = '#f0f0f0', image = self.search_img).place(relx = 1.0, anchor="ne", relwidth = 0.08, relheight=0.6)

    def search(self):
        self.root.destroy()
        import product
        
root = Tk()
obj = Search(root)
root.mainloop()