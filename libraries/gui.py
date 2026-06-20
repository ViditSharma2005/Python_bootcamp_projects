import tkinter as tk
w=tk.Tk()
l1=tk.Label(text="Name")
k1=tk.Entry(width="30")
l1.grid(row=1,column=1,padx=10,pady=10)
k1.grid(row=1,column=2,padx=10)
w.minsize(400,400)
w.mainloop()