import tkinter as tk
from tkinter import ttk
from tkinter import *
import os
import sys
import binary_tree

# root window
root = tk.Tk()
root.geometry("1000x1000")
root.title('Program pre návrh efektívného kódu')
root.resizable(0, 0)

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
'------------'
'import binarneho stromu'
def run():
    os.system('binary_tree.py')

btn = Button(root, text="Binary Tree", bg="black", fg="white",command=run)
btn.grid(column=0, row=0)


'-----------'
# username
username_label = ttk.Label(root, text="PK kody:")
username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

pk_entry = ttk.Entry(root)
pk_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)


pk_entry = ttk.Entry(root)
pk_entry.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)

pk_entry = ttk.Entry(root)
pk_entry.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)

pk_entry = ttk.Entry(root)
pk_entry.grid(column=0, row=3, sticky=tk.E, padx=5, pady=5)

pk_entry = ttk.Entry(root)
pk_entry.grid(column=0, row=4, sticky=tk.E, padx=5, pady=5)

pk_entry = ttk.Entry(root)
pk_entry.grid(column=0, row=5, sticky=tk.E, padx=5, pady=5)

pk_entry = ttk.Entry(root)
pk_entry.grid(column=0, row=6, sticky=tk.E, padx=5, pady=5)

pk_entry = ttk.Entry(root)
pk_entry.grid(column=0, row=7, sticky=tk.E, padx=5, pady=5)

pk_entry = ttk.Entry(root)
pk_entry.grid(column=0, row=8, sticky=tk.E, padx=5, pady=5)

pk_entry = ttk.Entry(root)
pk_entry.grid(column=0, row=9, sticky=tk.E, padx=5, pady=5)

pk_entry = ttk.Entry(root)
pk_entry.grid(column=0, row=10, sticky=tk.E, padx=5, pady=5)

pk_entry = ttk.Entry(root)
pk_entry.grid(column=0, row=11, sticky=tk.E, padx=5, pady=5)

pk_entry = ttk.Entry(root)
pk_entry.grid(column=0, row=12, sticky=tk.E, padx=5, pady=5)

pk_entry = ttk.Entry(root)
pk_entry.grid(column=0, row=13, sticky=tk.E, padx=5, pady=5)

pk_entry = ttk.Entry(root)
pk_entry.grid(column=0, row=14, sticky=tk.E, padx=5, pady=5)

pk_entry = ttk.Entry(root)
pk_entry.grid(column=0, row=15, sticky=tk.E, padx=5, pady=5)

pk_entry = ttk.Entry(root)
pk_entry.grid(column=0, row=16, sticky=tk.E, padx=5, pady=5)

pk_entry = ttk.Entry(root)
pk_entry.grid(column=0, row=17, sticky=tk.E, padx=5, pady=5)

pk_entry = ttk.Entry(root)
pk_entry.grid(column=0, row=18, sticky=tk.E, padx=5, pady=5)

pk_entry = ttk.Entry(root)
pk_entry.grid(column=0, row=19, sticky=tk.E, padx=5, pady=5)

pk_entry = ttk.Entry(root)
pk_entry.grid(column=0, row=20, sticky=tk.E, padx=5, pady=5)




window = root
'''output window'''
txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)

frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Vyberte variantu:')

agreement = tk.StringVar()


def agreement_changed():
    tk.messagebox.showinfo(title='Result',
                        message=agreement.get())


ttk.Checkbutton(root,
                text='shanon-fan',
                command=agreement_changed,
                variable=agreement,
                onvalue='agree',
                offvalue='disagree').pack()

ttk.Checkbutton(root,
                text='Huffman',
                command=agreement_changed,
                variable=agreement,
                onvalue='agree',
                offvalue='disagree').pack()

''''jjjj'''
# password


root.mainloop()

# exit button
exit_button = ttk.Button(
    root,
    text='Huffman coding',
    command=lambda: root.quit()
)

exit_button = ttk.Button(
    root,
    text='Huffman coding',
    command=lambda: root.quit()
)


exit_button.pack(
    ipadx=10,
    ipady=10,
    expand=True
)

exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)



root.mainloop()
