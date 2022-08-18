import tkinter as tk
from tkinter import ttk
from navigation_panel import NavPanel
from view_panel import ViewPanel
from control_panel import ControlPanel
from canvas import MapCanvas, SeqCanvas
from view import MyView
import tools

class MenuBar(tk.Menu):
	def __init__(self, parent):
		super().__init__()
		
		# create a menu
		file_menu = tk.Menu(self)
		edit_menu = tk.Menu(self)
		tools_menu = tk.Menu(self)

		# add a menu item to the menu
		file_menu.add_command(label='Exit', command=parent.destroy)
		file_menu.add_command(label='Open', command= lambda : tools.open_file(navPanel1))
		edit_menu.add_command(label='Plot arrow', command= lambda : tools.plot_arrow(mapCanvas))
		edit_menu.add_command(label='Plot text', command= lambda : tools.plot_text(seqCanvas))
		tools_menu.add_command(label='About')

		# add the File menu to the menubar
		self.add_cascade(label="File", menu=file_menu)
		self.add_cascade(label="Edit", menu=edit_menu)
		self.add_cascade(label="Tools", menu=tools_menu)


if __name__=="__main__":
	root = tk.Tk()
	root.title('MenuBar Widget')
	root.geometry('800x500')
	
	#Menu bar
	menuBar1 = MenuBar(root)
	root.config(menu=menuBar1)
	
	#Navigation panel
	navPanel1= NavPanel(root)
	navPanel1.pack(side='left', fill='y', expand=False)
	
	#View panel
	viewPanel1= ViewPanel(root)
	viewPanel1.pack(fill='both', expand=True)
	
	mapCanvas = MapCanvas(viewPanel1)
	mapCanvas.pack(side = 'top', fill = 'both', expand = True)
	
	seqCanvas = SeqCanvas(viewPanel1)
	seqCanvas.pack(side = 'top', fill = 'both', expand = True)
	
	viewPanel1.add(mapCanvas, text= 'Map View')
	viewPanel1.add(seqCanvas, text= 'Sequence View')
	
	#Control Panel
	controlPanel1= ViewPanel(root)
	controlPanel1.pack(fill='both', expand=True)
	
	canvas3= MyView(viewPanel1)
	canvas3.pack(fill = 'both', expand = True)
	canvas4 = MyView(viewPanel1)
	canvas4.pack(fill = 'both', expand = True)
	
	controlPanel1.add(canvas3, text= 'Canvas 3')
	controlPanel1.add(canvas4, text= 'Canvas 4')
	
	
	root.mainloop()
