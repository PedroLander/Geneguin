import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfile
import parsers
import global_variables


def load_sequence(seqName):
	#takes the name of the sequence, and gets the seq from the dictionar
	#plot each nucleotide in the seq canvas
	
	seq=global_variables.sequences[seqName[0]],
	seq = seq[0]
	
	global_variables.seqCanvas.delete("all")
	width = global_variables.viewNotebook.winfo_width(),
	height = global_variables.viewNotebook.winfo_height(),
	x=width[0]
	y=height[0]/2
	lenght = len(seq)
	print (seq)
	pos = 15
	
	#plot bar wrapping sequence
	global_variables.seqCanvas.create_polygon([
	pos,y-10,
	pos*lenght+pos*2,y-10,
	pos*lenght+pos*2.5,y,
	pos*lenght+pos*2,y+10,
	pos,y+10], outline='white', fill='yellow', width=2)
	
	#plot overlaying sequence
	for nt in seq:
		pos += 15
		global_variables.seqCanvas.create_text(
		pos, 
		y,
		text = nt,
		fill="black", 
		font=('Helvetica 15 bold'))
	print (lenght)




def zoom_in():
	x = global_variables.seqCanvas.winfo_width()
	y = global_variables.seqCanvas.winfo_height()
	factor = 1.3 
	print (x, y, x/2, y/2)
	global_variables.seqCanvas.scale('all', x/2, y/2, factor, factor)

def zoom_out():
	x = global_variables.seqCanvas.winfo_width()
	y = global_variables.seqCanvas.winfo_height()
	factor = .7
	global_variables.seqCanvas.scale('all', x/2, y/2, factor, factor)


def open_file():
	file = askopenfile(mode ='r', filetypes =[('Fasta Files', '*.fa')])
	if file is not None:
		global_variables.navPanel.add_data(
		file.name.split('/')[-1], 
		parsers.parse_fasta(file.read()))
	file.close()
