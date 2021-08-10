import tkinter as tk
from tkinter import X
from tkinter import font
from tkinter.constants import RIGHT

# window setup
window = tk.Tk(className='how many elephants?')
window.geometry('400x600')
window.configure(bg='#BFDCDE')

# functions
def count_elephants():
    try:
        lbs_value = int(input_entry.get())
        elephants = round(lbs_value/15000, 2)
        result_label['text'] = '{} is equal to\n {} elephants!'.format(lbs_value, elephants)
        result_label.config(fg='black')
    except ValueError:
        result_label['text'] = 'Make sure to input\n number as weight!'
        result_label.config(fg='red')

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
button_frame = tk.Frame(
    master=window,
    width=250,
    height=100,
    bg='black'
)
button = tk.Button(
    master=button_frame,
    bg='#127278',
    fg='white',
    text='Calculate',
    font=('Courier', 25),
    padx=20,
    pady=10,
    command=count_elephants
)
button_frame.pack()
button.pack()

# result
result_frame = tk.Frame(
    master=window,
    width=400,
    pady=20,
    bg='#BFDCDE'
)
result_label = tk.Label(
    master=result_frame,
    text='0 lbs is equal to\n 0 elephants!',
    font=('Courier', 25, 'bold'),
    bg='#BFDCDE',
    fg='black'
)
result_frame.pack()
result_label.pack()

# making sure the window opens
window.mainloop()

