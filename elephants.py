import tkinter as tk
from tkinter import X
from tkinter.constants import RIGHT

# window setup
window = tk.Tk(className='how many elephants?')
window.geometry('400x600')
window.configure(bg='#BFDCDE')

# functions

# title
title_frame = tk.Frame(
    master=window,
    width=400,
    padx=30,
    bg='#BFDCDE'
)
title_label = tk.Label(
    master=title_frame,
    text='How many\n elephants?',
    bg='#BFDCDE',
    fg='black',
    font=('Courier', 40, 'bold')
)
title_frame.pack(pady=(40,20))
title_label.pack()

# image
image_frame = tk.Frame(
    master=window,
    width=130,
    height=133
)
img = tk.PhotoImage(file='elephant.png')
image_label = tk.Label(
    master=image_frame,
    image=img,
    bg='#BFDCDE'
)
image_frame.pack()
image_label.pack()

# 'subtitle'
subtitle_frame = tk.Frame(
    master=window,
    width=400,
    pady=20,
    bg='#BFDCDE'
)
subtitle_label = tk.Label(
    master=subtitle_frame,
    text='1 elephant = 15000lbs',
    bg='#BFDCDE',
    fg='black',
    font=('Courier', 20, 'bold')
)
subtitle_frame.pack()
subtitle_label.pack()

# user input
input_frame = tk.Frame(
    master=window,
    bg='#BFDCDE'
)
input_entry = tk.Entry(
    master=input_frame,
    bg='white',
    fg='black',
    font=('Courier', 30)
)
input_label = tk.Label(
    master=input_frame,
    text='lbs',
    font=('Courier', 30, 'bold'),
    bg='#BFDCDE',
    fg='black'
)
input_entry.insert(0, '0')
input_frame.pack(fill=X, pady=(0,20), padx=(50,50))
input_label.pack(side=RIGHT, padx=5)
input_entry.pack(fill=X, padx=5, expand=True)

# button

# result

# making sure the window opens
window.mainloop()

