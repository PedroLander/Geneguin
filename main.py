import tkinter as tk
from tkinter import ttk
from navigation_panel import NavPanel
from view_panel import ViewPanel
from control_panel import ControlPanel
from canvas import MapCanvas, SeqCanvas
from view import MyView
import tools
import global_variables

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
	root.title('Geneguin 🐧')
	root.geometry('800x500')
	
	#Menu bar
	menuBar1 = MenuBar(root)
	root.config(menu=menuBar1)
	
	
	#PanedWindow
	pw = tk.PanedWindow()
	pw.pack(fill='both', expand='true')
	
	#Navigation panel
	navPanel1= NavPanel(root)
	navPanel1.pack(side='left', fill='y', expand=False)
	
	pw.add(navPanel1)
	
	#View panel
	global_variables.viewPanel1= ViewPanel(root)
	global_variables.viewPanel1.pack(fill='both', expand=True)
	
	global_variables.mapCanvas = MapCanvas(global_variables.viewPanel1)
	global_variables.mapCanvas.pack(side = 'top', fill = 'both', expand = True)
	
	global_variables.seqCanvas = SeqCanvas(global_variables.viewPanel1)
	global_variables.seqCanvas.pack(side = 'top', fill = 'both', expand = True)
	
	global_variables.viewPanel1.add(global_variables.seqCanvas, text= 'Sequence View')
	global_variables.viewPanel1.add(global_variables.mapCanvas, text= 'Map View')
	
	#Control Panel
	controlPanel1= ViewPanel(root)
	controlPanel1.pack(fill='both', expand=True)
	
	canvas3= MyView(global_variables.viewPanel1)
	canvas3.pack(fill = 'both', expand = True)
	canvas4 = MyView(global_variables.viewPanel1)
	canvas4.pack(fill = 'both', expand = True)
	
	controlPanel1.add(canvas3, text= 'Canvas 3')
	controlPanel1.add(canvas4, text= 'Canvas 4')
	
	
	root.mainloop()
