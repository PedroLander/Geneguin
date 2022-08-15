import tkinter as tk
from application import MainApplication, Menubar

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('600x400')
    root.title('Geneguin')
    
    menubar = Menubar(root)
    root.config (menu=menubar)
    
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
