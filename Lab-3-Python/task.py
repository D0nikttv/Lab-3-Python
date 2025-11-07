from tkinter import * 
from PIL import Image, ImageTk
from key_generate import key_generate
import itertools

root = Tk()
root.title('Name')
root.geometry('500x350+500+300')


icon = PhotoImage(file='am.png')
root.iconphoto(False, icon)


def resize_image(event=None):

    new_width = root.winfo_width()
    new_height = root.winfo_height()
    
    new_image = original_photo.resize((new_width,new_height), Image.LANCZOS) 
    photo = ImageTk.PhotoImage(new_image)

    canvas.delete('all')
    canvas.create_image(0, 0, image=photo, anchor=NW)
    canvas.create_rectangle(new_width//3, new_height//6.6, new_width//1.5, new_height//4)
    canvas.image = photo

    canvas.create_window(new_width/2, new_height/2, window=btn)
    
def key_gen():
        canvas.delete('dynamic_text')
        canvas.create_text(root.winfo_width()//2, root.winfo_height()//5, text=f'{key_generate()}', anchor= 'center', tags='dynamic_text')
    

    
original_photo = Image.open('dota2_image.png')
canvas = Canvas(root)
canvas.pack(fill='both', expand= YES)


btn = Button(canvas, text='Генерация ключа', command=key_gen)


root.bind('<Configure>', resize_image)
root.mainloop()

