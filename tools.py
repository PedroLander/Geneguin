import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfile
import parsers
import global_variables

def plot_rectangle(canvas):
	canvas.create_rectangle(50, 50, 180, 120, outline = 'white', fill  = 'orange')

def plot_arrow(canvas):
	canvas.create_polygon([
	0,0,
	100,0,
	110,5,
	100,10,
	0,10], outline='white', fill='yellow', width=2)


def plot_text(canvas):
	global sequences
	canvas.create_text(
	canvas.winfo_width()/2,
	canvas.winfo_height()*2/3, 
	text="HELLO WORLD", 
	fill="white", 
	font=('Helvetica 15 bold'))


def open_file(navPanel):
	file = askopenfile(mode ='r', filetypes =[('Fasta Files', '*.fa')])
	if file is not None:
		navPanel.add_data(
		file.name.split('/')[-1], 
		parsers.parse_fasta(file.read()))
	file.close()

def load_sequence(seqName):
	print ('enter')
	global_variables.mapCanvas.create_text(
	global_variables.mapCanvas.winfo_width()/2,
	global_variables.mapCanvas.winfo_height()*2/3, 
	text=global_variables.sequences[seqName[0]],
	fill="white", 
	font=('Helvetica 15 bold'))
