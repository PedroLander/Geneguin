import tkinter as tk
from tkinter import ttk

def plot_rectangle(canvas):
	canvas.create_rectangle(50, 50, 180, 120, outline = 'white', fill  = 'orange')

def plot_arrow(canvas):
	canvas.create_polygon([
	0,0,
	100,0,
	110,5,
	100,10,
	0,10], outline='white', fill='yellow', width=2)

