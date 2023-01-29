def salvar_barras():
    while h >= 10:
        y = 0
        x = 0
        h = 94
        w = 11
        image = cv2.imread('barra_mana_100.png')
        barra_vida = image[x:w, y:h]
        cv2.imwrite('barra_mana_' + str(h) + '.png',barra_vida)
        print(h)
        h-=1


import os




import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# create the root window
root = Toplevel(window)

root.title('Listbox')


# create a list box
#langs = ('Java', 'C#', 'C', 'C++', 'Python',
#         'Go', 'JavaScript', 'PHP', 'Swift')
rootdir = 'scripts'
langs=()
for file in os.listdir(rootdir):
    d = os.path.join(rootdir, file)
    if os.path.isdir(d):
        if d.replace("scripts\\","") != "__pycache__":
            langs=langs+(d.replace("scripts\\",""),)

var = tk.Variable(value=langs)

listbox = tk.Listbox(
    root,
    listvariable=var,
    height=6,
    selectmode=tk.EXTENDED)

listbox.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

# link a scrollbar to a list
scrollbar = ttk.Scrollbar(
    root,
    orient=tk.VERTICAL,
    command=listbox.yview
)

listbox['yscrollcommand'] = scrollbar.set

scrollbar.pack(side=tk.LEFT, expand=True, fill=tk.Y)


def items_selected(event):
    # get selected indices
    selected_indices = listbox.curselection()
    # get selected items
    selected_langs = ",".join([listbox.get(i) for i in selected_indices])
    msg = f'You selected: {selected_langs}'

    showinfo(title='Information', message=msg)


listbox.bind('<<ListboxSelect>>', items_selected)

root.mainloop()
