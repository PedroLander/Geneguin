import tkinter as tk
import tkinter as tk
from tkinter import ttk
from menu_bar import MenuBar
from navigation_panel import NavPanel
from control_panel import ControlPanel
from canvas import  SeqCanvas
from view import MyView
import tools
import global_variables



if __name__=="__main__":


	root = tk.Tk()
	root.geometry('800x500')

	menuBar= MenuBar(root)
	root.config(menu=menuBar)
	
	toolBar=tk.Frame(root)
	toolBar.pack(fill='x', expand=False)
	
	zoomIn = tk.Button(toolBar, text="Zoom in", command = tools.zoom_in)
	zoomIn.pack(side='left')
	zoomOut= tk.Button(toolBar, text="Zoom out", command = tools.zoom_out)
	zoomOut.pack(side='left')
	loadRect= tk.Button(toolBar, text="Load Rectangle", command = lambda: tools.plot_text(global_variables.seqCanvas))
	loadRect.pack(side='left')
	
#---------left paned window----------
	left = tk.PanedWindow()
	left.pack(fill='both', expand=1)

	global_variables.navPanel =NavPanel(left)
	left.add(global_variables.navPanel )

#-------right paned window----------
	right = tk.PanedWindow(left, orient='vertical')
	left.add(right)

#--------view panel--------------------
##-------view Frame---------------------
	global_variables.viewFrame= tk.Frame(right, bg='red')
	global_variables.viewFrame.pack(fill='both', expand=True)
	right.add(global_variables.viewFrame)

###------view scrollbar---------------
	map_scroll = tk.Scrollbar(global_variables.viewFrame, orient = 'horizontal')
	map_scroll.pack(side='bottom', fill='x')
	
###-------view notebook-----------
	global_variables.viewNotebook = ttk.Notebook(global_variables.viewFrame)
	global_variables.viewNotebook.pack(side='top', fill='both', expand=True)


####-----view canvases---------
	global_variables.seqCanvas = SeqCanvas(global_variables.viewNotebook)
	global_variables.seqCanvas.pack(fill = 'both', expand = True)
	
	global_variables.viewNotebook.add(global_variables.seqCanvas, text= 'Sequence View')



#------------------- control panel-----------------------
	global_variables.controlPanel = ttk.Notebook()
	right.add(global_variables.controlPanel)

	canvas3= MyView(global_variables.controlPanel)
	canvas3.pack(fill = 'both', expand = True)
	canvas4 = MyView(global_variables.controlPanel)
	canvas4.pack(fill = 'both', expand = True)

	global_variables.controlPanel.add(canvas3, text= 'Canvas 3')
	global_variables.controlPanel.add(canvas4, text= 'Canvas 4')

	root.mainloop()
