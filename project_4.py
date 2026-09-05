import tkinter as tk
import time
from PIL import Image,ImageTk

#Main window

root=tk.Tk()
root.title("Photo Slidshow Album")
root.geometry("1000x800")

#list of image paths
image_paths=[r"C:\Users\omgal\OneDrive\Pictures\College_Account_Details.jpg",
    r"C:\Users\omgal\OneDrive\Pictures\Demand_Letter.jpg",
    r"C:\Users\omgal\OneDrive\Pictures\Last_Fees_Reciept.jpg",
    r"C:\Users\omgal\OneDrive\Pictures\Om_Gupta_1st_year_Result.jpg"
]                       #copying the image path by selecting image then use Ctrl + Shift +C

image_size=(600,600)
images=[]
for path in image_paths:
    img=Image.open(path)
    img=img.resize(image_size)
    images.append(img)  #adding each image in list

#Converting PIL image into Tkinter Compatible Image
final_image=[]
for img in images:
    photo=ImageTk.PhotoImage(img)
    final_image.append(photo)

image_label=tk.Label(root)     #label widget to keep photo
image_label.pack(pady=30)

#Slideshow Func
def slideshow():
    for photo in final_image:
        image_label.config(image=photo)
        image_label.image=photo
        root.update()
        time.sleep(2)

#Button
play_button=tk.Button(root,text="Play the slideshow",font=("Arial",18),command=slideshow)

play_button.pack(pady=40)


root.mainloop()