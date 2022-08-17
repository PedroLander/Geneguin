import tkinter as tk
from tools import plot_rectangle

class MenuBar(tk.Menu):
	def __init__(self, parent):
		super().__init__()
		
		# create a menu
		file_menu = tk.Menu(self)
		edit_menu = tk.Menu(self)
		tools_menu = tk.Menu(self)

		# add a menu item to the menu
		file_menu.add_command(label='Exit', command=parent.destroy)
		edit_menu.add_command(label='Plot', command= lambda : plot_rectangle(canvas1))
		tools_menu.add_command(label='About')



		# add the File menu to the menubar
		self.add_cascade(label="File", menu=file_menu)
		self.add_cascade(label="Edit", menu=edit_menu)
		self.add_cascade(label="Tools", menu=tools_menu)



if __name__=="__main__":
	root = tk.Tk()
	root.title('MenuBar Widget')
	root.geometry('600x400')

	menuBar1 = MenuBar(root)
	root.config(menu=menuBar1)

	root.mainloop()
