import tkinter as tk


TEXT_SIZE = 44

def _quit(event):
    root.destroy()

    
root = tk.Tk()
root.wm_attributes('-fullscreen', 'True')
root.ISBN = tk.Entry(root)
root.ISBN.grid(row = 0, column = 0, sticky = "ns")
root.ISBN.config(font=("Courier", TEXT_SIZE))
root.search_button = tk.Button(root, text = "Søk", font=("Arial", TEXT_SIZE))
root.search_button.grid(row = 0, column = 1, sticky = "ns")
root.bind("<Control-x>", _quit)

root.mainloop()
