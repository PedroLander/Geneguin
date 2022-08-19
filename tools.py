import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfile
import parsers
import global_variables

def plot_rectangle(canvas):
	canvas.create_rectangle(50, 50, 180, 120, outline = 'white', fill  = 'orange')

def plot_sequence(canvas, lenght):
	
	x = canvas.winfo_width()/2,
	y = canvas.winfo_height()*2/3,
	
	canvas.create_polygon([
	0,y,
	lenght-10,y,
	lenght,y+5,
	lenght-10,y+10,
	0,y+10], outline='white', fill='yellow', width=2)


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

def load_nuc_sequence(seqName):
	global_variables.mapCanvas.delete("all")
	global_variables.seqCanvas.delete("all")
	width = global_variables.viewPanel1.winfo_width(),
	height = global_variables.viewPanel1.winfo_height(),
	x=width[0]
	y=height[0]
	print (x/2)
	print (y*2/3)
	global_variables.seqCanvas.create_text(
	x/2,
	y*2/3, 
	text=global_variables.sequences[seqName[0]],
	fill="white", 
	font=('Helvetica 15 bold'))


def load_map_sequence(seqName):
	global_variables.mapCanvas.delete("all")
	global_variables.seqCanvas.delete("all")
	width = global_variables.viewPanel1.winfo_width(),
	height = global_variables.viewPanel1.winfo_height(),
	x=width[0]
	y=height[0]/2
	print (x)
	print (height)
	lenght = len(global_variables.sequences[seqName[0]])
	
	global_variables.mapCanvas.create_polygon([
	50,y,
	50+lenght-10,y,
	50+lenght,y+5,
	50+lenght-10,y+10,
	50,y+10], outline='white', fill='yellow', width=2)

