import tkinter as tk

def autoscroll():
    large_textbox.yview(tk.END)

def on_enter(event):
    text = small_textbox.get()
    large_textbox.config(state=tk.NORMAL)
    large_textbox.insert(tk.END, "\nYou entered: " + text)
    large_textbox.config(state=tk.DISABLED)
    small_textbox.delete(0, tk.END)
    autoscroll()

root = tk.Tk()
root.title("Text Boxes Example")

large_textbox = tk.Text(root, height=10, width=40)
large_textbox.insert(tk.END, "This is a large uneditable text box.")
large_textbox.config(state=tk.DISABLED)
large_textbox.pack(pady=10)

small_textbox = tk.Entry(root, width=40)
small_textbox.pack(pady=10)

scrollbar = tk.Scrollbar(root, command=large_textbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
large_textbox.config(yscrollcommand=scrollbar.set)

small_textbox.bind("<Return>", on_enter)

root.mainloop()
