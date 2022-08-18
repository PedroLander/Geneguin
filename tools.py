import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfile

def plot_rectangle(canvas):
	canvas.create_rectangle(50, 50, 180, 120, outline = 'white', fill  = 'orange')

def plot_arrow(canvas):
	canvas.create_polygon([
	0,0,
	100,0,
	110,5,
	100,10,
	0,10], outline='white', fill='yellow', width=2)


def open_file(navPanel):
	file = askopenfile(mode ='r', filetypes =[('Fasta Files', '*.fa')])
	if file is not None:
		content = file.read()
		print(file.name.split('/')[-1], content)
		
		navPanel.add_data(file.name.split('/')[-1])
