import tkinter as tk
from tkinter import ttk
from menu_bar import MenuBar
from navigation_panel import NavPanel
from view_panel import ViewPanel
from control_panel import ControlPanel
from view import MyView



if __name__=="__main__":
	root = tk.Tk()
	root.title('MenuBar Widget')
	root.geometry('600x400')
	
	#Menu bar
	menuBar1 = MenuBar(root)
	root.config(menu=menuBar1)
	
	#Navigation panel
	navPanel1 = NavPanel(root)
	navPanel1.pack(side='left', fill='y', expand=False)
	
	#View panel
	viewPanel1= ViewPanel(root)
	viewPanel1.pack(fill='both', expand=True)
	
	view1 = MyView(viewPanel1)
	view2 = MyView(viewPanel1)
	
	view1.pack(fill = 'both', expand = True)
	view2.pack(fill = 'both', expand = True)
	
	viewPanel1.add(view1, text= 'View 1')
	viewPanel1.add(view2, text= 'View 2')
	
	#Control Panel
	controlPanel1= ViewPanel(root)
	controlPanel1.pack(fill='both', expand=True)
	
	view3 = MyView(viewPanel1)
	view4 = MyView(viewPanel1)
	
	view3.pack(fill = 'both', expand = True)
	view4.pack(fill = 'both', expand = True)
	
	controlPanel1.add(view3, text= 'View 3')
	controlPanel1.add(view4, text= 'View 4')
	
	
	root.mainloop()
