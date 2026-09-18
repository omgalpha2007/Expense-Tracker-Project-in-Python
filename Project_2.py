#Notepad Clown Project
#tkinter module and library
import tkinter as tk
from tkinter import filedialog,messagebox

#Main Window code
root=tk.Tk()
root.title("simple Text Editor")
root.geometry("800x600")

#creating text area
text =tk.Text(root,wrap=tk.WORD,font=("Helvetica",16))

text.pack(expand=True,fill=tk.BOTH)

#Main logic

#func 1-"too create new file"
def new_file():
    text.delete(1.0,tk.END)

#func 2- "to open a file"
def open_file():
    file_path=filedialog.askopenfilename(defaultextentions=".txt",filetypes=[("Text Files","*.txt")])
    if file_path:  # opening the file
        with open(file_path,"r") as files:
            text.delete(1.0,tk.END)
            text.insert(tk.END,files.read())

#func 3- "saving the file"
def save_file():
    file_path=filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files","*.txt")]
    )

    if file_path:
        with open(file_path,"w") as file:
            file.write(text.get(1.0,tk.END))
    messagebox.showinfo("Info","FIle saved successfully")

#Menu
menu=tk.Menu(root)
root.config(menu=menu)
file_menu=tk.Menu(menu)

#New file,Open,Save,Exit
menu.add_cascade(label="File",menu=file_menu)

file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

root.mainloop()     #starts & keep the window open
