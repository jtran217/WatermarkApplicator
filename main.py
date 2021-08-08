# IMPORTS
import tkinter
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

# Functions
def browseimage():
    background_image = filedialog.askopenfilename(title='Select an Image',
                                            filetypes=(("Image files",
                                                     "*.png* *.jpeg*"),))
    watermark = filedialog.askopenfilename(title='Select a watermark',
                                           filetypes=(("Image files",
                                                       "*.png* *.jpeg*"),))

    if background_image and watermark:
        #Open File
        image1 = Image.open(background_image)
        image2 = Image.open(watermark)
        image2 = image2.resize((40,40))
        image1.paste(image2,(0,0))

        canvas.image_tk = ImageTk.PhotoImage(image1)

        canvas.itemconfigure(image_id, image=canvas.image_tk)


def save_image():
    mask = [
        ("Image Files", "*.png*"),
        ("JPEG", "*.jpg*")
    ]
    merged_image = ImageTk.getimage(canvas.image_tk)
    name = filedialog.asksaveasfilename(filetypes=mask, defaultextension='.png')
    merged_image.save(name)







# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Watermark Applier")
window.geometry("1200x850")
window.configure(bg='#DEBA9D')

canvas = Canvas(height=600,width=800,)
canvas.grid(row=3,column=1)

# Labels
title_label = Label(text="Watermark Applicator V1", bg='#DEBA9D', fg='#6F4C5B',font=("Arial", 60, 'bold'))
title_label.grid(row=0,column=0, columnspan=3)
title_label.config(padx=100,pady=10)


# FileDialog
image_explore = Button(text='Select Image and Watermark', command=browseimage)
image_explore.grid(row=1, column=1, pady=10)
image_id = canvas.create_image(400,300)
save_image = Button(text='Save New Image', command=save_image)
save_image.grid(row=4,column=1, pady=10)


window.mainloop()