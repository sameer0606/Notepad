from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import webbrowser

def newfile():
    global file
    root.title("Untitled-Notepad")
    file = None
    TextArea.delete(1.0, END)


def openfile():
    global file
    file = askopenfilename(defaultextension = ".txt", filetypes = [("All Files", "*.*"),
    ("Text Documents", "*.txt")])

    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "-Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()
        
def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = "Untitiled.txt",defaultextension = ".txt", filetypes = [("All Files", "*.*"),
        ("Text Documents", "*.txt")] )
        if file == "":
            file = None
        else:
            # save file as new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + "-Notepad")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
def quitapp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepade", "Notepad by Sam")

def openweb():
    webbrowser.open(url,new=new)

# cut,copy and paste shortcut
def cut1():
    TextArea.event_generate(("<<Ctrl+x>>"))
def copy1():
    TextArea.event_generate(("<<Ctrl+c>>"))
def paste1():
    TextArea.event_generate(("<<Ctrl+v>>"))






if __name__ == "__main__":
    # Basic tkinter setup
    root = Tk()
    root.geometry("400x500")
    root.title("Untitled-Notepad")
    root.wm_iconbitmap("2.ico")

    # how to use notepad web link
    new = 1
    url = "https://support.microsoft.com/en-us/topic/how-to-use-notepad-to-create-a-log-file-dd228763-76de-a7a7-952b-d5ae203c4e12#:~:text=Click%20Start%2C%20point%20to%20Programs,box%2C%20and%20then%20click%20OK."

    # Adding text area
    TextArea = Text(root, font = "lucida 16")
    file = None
    TextArea.pack(expand = True, fill = BOTH)

    # Adding menubars
    Menubar = Menu(root)
    # filemenu starts 
    filemenu = Menu(Menubar, tearoff = 0)
    # To open a new file
    filemenu.add_command(label = "New", command = newfile)
    # To open an already existing file
    filemenu.add_command(label = "Open", command = openfile)
    # to save the file
    filemenu.add_command(label = "Save", command = savefile)
    # to quit
    filemenu.add_separator()
    filemenu.add_command(label = "Exit", command = quitapp)
    Menubar.add_cascade(label ="File", menu = filemenu)
    # filemenu ends

    # Edit menu starts
    Editmenu = Menu(Menubar, tearoff = 0)
    # to give the feature of cut,copy and paste
    Editmenu.add_command(label = "Cut", command = cut)
    Editmenu.add_command(label = "Copy", command = copy)
    Editmenu.add_command(label = "Paste", command = paste)
    Menubar.add_cascade(label = "Edit", menu = Editmenu)
    # Edit menu ends

    # Help menu stars 
    Helpmenu = Menu(Menubar, tearoff = 0)
    Helpmenu.add_command(label = "About-Notepad", command = about)
    Helpmenu.add_command(label = "How to use Notepad", command = openweb)
    Menubar.add_cascade(label = "Help", menu = Helpmenu)
    # Help menu ends
    root.config(menu=Menubar)

    # Adding scroollbar 
    scroll = Scrollbar(TextArea)
    scroll.pack(side = RIGHT, fill = Y)
    scroll.config(command = TextArea.yview)
    TextArea.config(yscrollcommand = scroll.set)

    root.mainloop()
