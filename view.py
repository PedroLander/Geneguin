from tkinter import ttk
import tkinter as tk

class MyView(tk.Frame): 
	def __init__(self,parent):
		super().__init__()
		self.configure(bg='blue')

if __name__=="__main__":
	root = tk.Tk()
	root.title('View1 Widget')
	root.geometry('400x200')

	myView1= MyView(root)
	myView1.pack(fill='both', expand=True)

	root.mainloop()
