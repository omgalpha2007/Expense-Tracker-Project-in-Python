import time
import tkinter as tk

root=tk.Tk()
root.title("Standard Digital Clock")

def currentTime():     #find curent time
    string=time.strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(100,currentTime)     #every 100 milisecond time will be updated

label=tk.Label(root,font=("Calibri",60,"bold"),background="black",foreground="white")
label.pack(anchor="center")

currentTime()

root.mainloop()