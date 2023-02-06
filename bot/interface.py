from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter import filedialog
from tkinter.messagebox import showinfo
from goto import with_goto
import shutil
import csv
import json
import os
from pathlib import Path
from main import *

def food():
    if (var1.get() == 1):
        os.spawnl(os.P_DETACH, r"./dist/eat_food/eat_food.exe",'x')
    else:
        os.system("taskkill /im eat_food.exe /F")

def ring():
    if (var11.get() == 1):
        os.spawnl(os.P_DETACH, r"dist\auto_ring\auto_ring.exe",'x')
    else:
        os.system("taskkill /im auto_ring.exe /F")

def player_on_screen():
    if (var12.get() == 1):
        os.spawnl(os.P_DETACH, r"dist\player_on_screen\player_on_screen.exe", 'a')
    else:
        os.system("taskkill /IM player_on_screen.exe /F")


def private_mensage():
    if (var13.get() == 1):
        os.spawnl(os.P_DETACH, r"dist\private_mensage\private_mensage.exe", 'a')
    else:
        os.system("taskkill /IM private_mensage.exe /F")

def anti_bot():
    if (var15.get() == 1):
        os.spawnl(os.P_DETACH, r"dist\anti_bot\anti_bot.exe", 'a')
    else:
        os.system("taskkill /IM anti_bot.exe /F")

def haste():
    if (var2.get() == 1):
        os.spawnl(os.P_DETACH, r"./dist/auto_haste/auto_haste.exe", 'x')
    else:
        os.system("taskkill /im auto_haste.exe /F")

def cura_vida():
    if (var3.get() == 1):
        os.spawnl(os.P_DETACH, r"dist\cura_vida\cura_vida.exe", 'x')
    else:
        os.system("taskkill /im cura_vida.exe /F")
    with open(r'parametros.json', 'r') as read_file:
        ler = json.load(read_file)
    ler['cv'] = var3.get()
    with open(r'parametros.json', 'w') as f:
        json.dump(ler, f)

def mana_train():
    if (var4.get() == 1):
        os.spawnl(os.P_DETACH, r"dist\mana_train\mana_train.exe", 'a')
    else:
        os.system("taskkill /IM mana_train.exe /F")

def paralyze():
    if (var6.get() == 1):
        os.spawnl(os.P_DETACH, r"dist\auto_anti_paralyze\auto_anti_paralyze.exe", 'x')
    else:
        os.system("taskkill /im auto_anti_paralyze.exe /F ")

def utamo():
    if (var7.get() == 1):
        os.spawnl(os.P_DETACH, r"dist\auto_utamo\auto_utamo.exe", 'x')
        #ativar_janela('tibia')
    else:
        os.system("taskkill /im auto_utamo.exe /F")

def cura_mana():
    with open(r'parametros.json', 'r') as read_file:
        ler = json.load(read_file)
    if (var8.get() == 1):
        os.spawnl(os.P_DETACH, r"dist\cura_mana\cura_mana.exe", 'x')
    else:
        os.system("taskkill /im cura_mana.exe /F")
    ler['cm'] = var8.get()
    with open(r'parametros.json', 'w') as f:
        json.dump(ler, f)

def ler_var(col):
    with open(r'parametros.json', 'r') as read_file:
        ler = json.load(read_file)
        val = ler[col]
    return val

def auto_atack():
    if (var9.get() == 1):
        os.spawnl(os.P_DETACH, r"dist\auto_atack\auto_atack.exe", 'x')
    else:
        os.system("taskkill /im auto_atack.exe /F")
    with open(r'parametros.json', 'r') as read_file:
        ler = json.load(read_file)
    ler['auto_atack'] = var9.get()
    with open(r'parametros.json', 'w') as f:
        json.dump(ler, f)

def auto_loot():
    if (var14.get() == 1):
        os.spawnl(os.P_DETACH, r"dist\auto_loot\auto_loot.exe", 'x')
    else:
        os.system("taskkill /im auto_loot.exe /F")

def follow_on():
    if (var16.get() == 1):
        os.spawnl(os.P_DETACH, r"dist\follow_on\follow_on.exe", 'x')
    else:
        os.system("taskkill /im follow_on.exe /F")

def cavebot():
    if (var10.get() == 1):
        #os.spawnl(os.P_DETACH, r"dist\cavebot\cavebot.exe", 'x')
        os.spawnl(os.P_DETACH, r"dist\script_reader\script_reader.exe", 'x')
    else:
        #os.system("taskkill /im cavebot.exe /F")
        os.system("taskkill /im script_reader.exe /F")

def atualizar():
    with open(r'parametros.json', 'r') as read_file:
        ler = json.load(read_file)
    ler['ef_ht']=ef_ht.get()
    ler['cv_perc']=float(cv_perc.get())
    ler['cv_ht']=cv_ht.get()
    ler['cv_perc_sup']=float(cv_perc_sup.get())
    ler['cv_ht_sup']=cv_ht_sup.get()
    ler['mt_perc']=float(mt_perc.get())
    ler['mt_ht']=mt_ht.get()
    ler['ah_ht']=ah_ht.get()
    ler['ap_ht']=ap_ht.get()
    ler['au_ht']=au_ht.get()
    ler['cm_perc']=float(cm_perc.get())
    ler['cm_ht']=cm_ht.get()
    ler['ar_ht'] = ar_ht.get()
    ler['spell_um_nm'] = spell_um_nm.get()
    ler['spell_dois_nm'] = spell_dois_nm.get()
    ler['spell_tres_nm'] = spell_tres_nm.get()
    ler['spell_um_ht'] = spell_um_ht.get()
    ler['spell_dois_ht'] = spell_dois_ht.get()
    ler['spell_tres_ht'] = spell_tres_ht.get()
    ler['min_mana_atack'] = float(min_mana_atack.get())
    with open(r'parametros.json', 'w') as f:
        json.dump(ler, f)
    tkinter.messagebox.showinfo('Tibia BOT','Hotkeys atualizadas')
    frame1.focus_set()

def background():

    with open('parametros_back.json', 'r') as read_file:
        ler = json.load(read_file)

    if (var5.get() == 1):
        ler['back'] = 1
    else:
        ler['back'] = 0

    with open('parametros_back.json', 'w') as f:
        json.dump(ler, f)

def selecionar_script():
    pasta = ''
    folder_selected = filedialog.askdirectory()
    for i in range(1,len(folder_selected)):
        x = folder_selected[-i]
        y = x.find('/')
        if y==-1:
            pasta = x+pasta
        else:
            break

    with open(r'parametros.json', 'r') as read_file:
        ler = json.load(read_file)
    ler['script'] = pasta
    with open(r'parametros.json', 'w') as f:
        json.dump(ler, f)

    btn_txt.set(f'script: {pasta}')

    return pasta

def limpar_script():
    entry10.delete(0, END)
    frame11.delete(CURRENT, END)

@with_goto
def delete_script():
    pasta=script_name.get()
    if pasta=='' or pasta == None:
        goto .fim
    limpar_script()
    path = "./scripts/"+pasta
    isExist = os.path.exists(path)
    if isExist:
        shutil.rmtree(path)
    showinfo(title='Informação', message='Script deletado')
    goto .encerrar
    label .fim
    showinfo(title='Informação', message='Selecione script a ser deletado')
    label .encerrar

@with_goto
def salvar_script():
    pasta=script_name.get()
    if pasta=='' or pasta == None:
        goto .fim
    path = "./scripts/"+pasta
    r=frame11.get('1.0','end')
    if len(r)<5:
        goto .fim
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)

    f = open(path+f'/{pasta}.csv', 'w+')
    writer = csv.writer(f)
    if r[0:1]==f'\n':
        r=r[1:len(r)]
    if r[(len(r)-2):len(r)]==f'\n\n':
        r=r[0:(len(r)-2)]
    writer.writerow([r.replace(f'\n\n','\n')])
    f.close()

    frame11.delete(CURRENT, END)
    ficheiro = open(f'./scripts/{pasta}/{pasta}.csv', 'r')
    ler = csv.reader(ficheiro, delimiter=';')
    lista = list(ler)
    for i in range(0, len(lista) - 1):
        c = lista[i][0]
        if c != '' and c != r'\n':
            frame11.insert(END, c)
            if i < len(lista) - 2:
                frame11.insert(END, '\n')

    showinfo(title='Informação', message='Script salvo')
    goto .encerrar
    label .fim
    showinfo(title='Informação', message='Script vazio')
    label .encerrar

def abrir_script():
    root = Toplevel(window)
    root.title('Listbox')
    rootdir = 'scripts'
    langs = ()
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d):
            if d.replace("scripts\\", "") != "__pycache__":
                langs = langs + (d.replace("scripts\\", ""),)
    var = Variable(value=langs)
    listbox = Listbox(
        root,
        listvariable=var,
        height=6,
        selectmode=EXTENDED)
    listbox.pack(expand=True, fill=BOTH, side=LEFT)
    # link a scrollbar to a list
    scrollbar = ttk.Scrollbar(
        root,
        orient=VERTICAL,
        command=listbox.yview
    )
    listbox['yscrollcommand'] = scrollbar.set
    scrollbar.pack(side=LEFT, expand=True, fill=Y)

    def items_selected(event):
        # get selected indices
        selected_indices = listbox.curselection()
        # get selected items
        selected_langs = ",".join([listbox.get(i) for i in selected_indices])
        msg = f'You selected: {selected_langs}'

        entry10.delete(0,END)
        entry10.insert(0,selected_langs)
        frame11.delete(CURRENT, END)
        ficheiro = open(f'./scripts/{selected_langs}/{selected_langs}.csv', 'r')
        ler = csv.reader(ficheiro, delimiter=';')
        lista = list(ler)
        for i in range(0, len(lista)-1):
            c = lista[i][0]
            if c!='' and c!=r'\n':
                frame11.insert(END,c)
                if i<len(lista)-2:
                    frame11.insert(END, '\n')

        showinfo(title='Information', message=msg)
        root.destroy()

    listbox.bind('<<ListboxSelect>>', items_selected)

    #Preenche Codigo

def limpa_programa():
    os.system("taskkill /im cura_vida.exe /F")
    os.system("taskkill /im cura_mana.exe /F")
    os.system("taskkill /im mana_train.exe /F")
    os.system("taskkill /im auto_haste.exe /F")
    os.system("taskkill /im eat_food.exe /F")
    os.system("taskkill /im auto_atack.exe /F")
    os.system("taskkill /im cavebot.exe /F")
    os.system("taskkill /im auto_ring.exe /F")
    os.system("taskkill /im player_on_screen.exe /F")
    os.system("taskkill /im private_mensage.exe /F")
    os.system("taskkill /im anti_bot.exe /F")
    os.system("taskkill /im follow_on.exe /F")
    os.system("taskkill /im script_reader.exe /F")

def kill_programa():
    os.system("taskkill /im cura_vida.exe /F")
    os.system("taskkill /im cura_mana.exe /F")
    os.system("taskkill /im mana_train.exe /F")
    os.system("taskkill /im auto_haste.exe /F")
    os.system("taskkill /im eat_food.exe /F")
    os.system("taskkill /im auto_atack.exe /F")
    os.system("taskkill /im cavebot.exe /F")
    os.system("taskkill /im auto_ring.exe /F")
    os.system("taskkill /im player_on_screen.exe /F")
    os.system("taskkill /im private_mensage.exe /F")
    os.system("taskkill /im anti_bot.exe /F")
    os.system("taskkill /im follow_on.exe /F")
    os.system("taskkill /im script_reader.exe /F")
    os.system("taskkill /im python.exe /F")

def stop_script():
    os.system("taskkill /im auto_atack.exe /F")
    os.system("taskkill /im cavebot.exe /F")
    os.system("taskkill /im follow_on.exe /F")
    os.system("taskkill /im script_reader.exe /F")

##################################################
# Window de Scripts
##################################################

def abrir_lista_scripts():
    # create the root window
    root = Toplevel(window)

    root.title('Listbox')

    # create a list box
    # langs = ('Java', 'C#', 'C', 'C++', 'Python',
    #         'Go', 'JavaScript', 'PHP', 'Swift')
    rootdir = 'scripts'
    langs = ()
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d):
            if d.replace("scripts\\", "") != "__pycache__":
                langs = langs + (d.replace("scripts\\", ""),)

    var = Variable(value=langs)

    listbox = Listbox(
        root,
        listvariable=var,
        height=6,
        selectmode=EXTENDED)

    listbox.pack(expand=True, fill=BOTH, side=LEFT)

    # link a scrollbar to a list
    scrollbar = ttk.Scrollbar(
        root,
        orient=VERTICAL,
        command=listbox.yview
    )

    listbox['yscrollcommand'] = scrollbar.set

    scrollbar.pack(side=LEFT, expand=True, fill=Y)

    def items_selected(event):
        # get selected indices
        selected_indices = listbox.curselection()
        # get selected items
        selected_langs = ",".join([listbox.get(i) for i in selected_indices])
        msg = f'Script {selected_langs} selecionado'

        with open(r'parametros.json', 'r') as read_file:
            ler = json.load(read_file)
        ler['script'] = str(selected_langs)
        with open(r'parametros.json', 'w') as f:
            json.dump(ler, f)
        btn_txt.set(f'script: {str(selected_langs)}')

        showinfo(title='Information', message=msg)
        root.destroy()

    listbox.bind('<<ListboxSelect>>', items_selected)

##################################################
# Configurações da janela
##################################################

limpa_programa()

window = Tk()
window.title('Tibia BOT')
window.geometry('580x380')
window.configure(bg='#dddddd')

menubar = Menu(window)
window.config(menu=menubar)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Atualizar Hotkeys", command=atualizar)
#filemenu.add_command(label="Open", command=atualizar)
#filemenu.add_command(label="Save", command=atualizar)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=kill_programa)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=atualizar)
helpmenu.add_command(label="About...", command=atualizar)
menubar.add_cascade(label="Help", menu=helpmenu)

tabControl = ttk.Notebook (window)
tab1 = ttk.Frame (tabControl)
tab2 = ttk.Frame (tabControl)
tab3 = ttk.Frame (tabControl)
tab4 = ttk.Frame (tabControl)
tabControl.add (tab1, text = 'Main')
tabControl.add (tab2, text = 'Target')
tabControl.add (tab3, text = 'Cavebot')
tabControl.add (tab4, text = 'Editor Cavebot')
tabControl.pack(expand = 1, fill ="both")


##################################################
# Frame comandos principais
##################################################
frame1 = Label(tab1)
frame1.pack()
frame2 = LabelFrame(frame1, text='On/Off')

ef_ht = StringVar(value=ler_var('ef_ht'))
cv_perc = StringVar(value=ler_var('cv_perc'))
cv_ht = StringVar(value=ler_var('cv_ht'))
cv_perc_sup = StringVar(value=ler_var('cv_perc_sup'))
cv_ht_sup = StringVar(value=ler_var('cv_ht_sup'))
mt_perc = StringVar(value=ler_var('mt_perc'))
mt_ht = StringVar(value=ler_var('mt_ht'))
ah_ht = StringVar(value=ler_var('ah_ht'))
ap_ht = StringVar(value=ler_var('ap_ht'))
au_ht = StringVar(value=ler_var('au_ht'))
cm_perc = StringVar(value=ler_var('cm_perc'))
cm_ht = StringVar(value=ler_var('cm_ht'))
ar_ht = StringVar(value=ler_var('ar_ht'))
spell_um_nm = StringVar(value=ler_var('spell_um_nm'))
spell_dois_nm = StringVar(value=ler_var('spell_dois_nm'))
spell_tres_nm = StringVar(value=ler_var('spell_tres_nm'))
spell_um_ht = StringVar(value=ler_var('spell_um_ht'))
spell_dois_ht = StringVar(value=ler_var('spell_dois_ht'))
spell_tres_ht = StringVar(value=ler_var('spell_tres_ht'))
min_mana_atack = StringVar(value=ler_var('min_mana_atack'))
back = IntVar


##Labels

label = Label(frame1, text="Food").grid(row=0, column=0)
entry = Entry(frame1 ,textvariable=ef_ht).grid(row=0, column=1)

label = Label(frame1, text="Auto Haste").grid(row=1, column=0)
entry = Entry(frame1, textvariable=ah_ht).grid(row=1, column=1)

label = Label(frame1, text="Anti Paralyze").grid(row=2, column=0)
entry = Entry(frame1, textvariable=ap_ht).grid(row=2, column=1)

label = Label(frame1, text="Auto Utamo").grid(row=3, column=0)
entry = Entry(frame1, textvariable=au_ht).grid(row=3, column=1)

label = Label(frame1, text="Cura Vida").grid(row=4, column=0)
entry = Entry(frame1, textvariable=cv_perc).grid(row=4, column=1)
entry = Entry(frame1, textvariable=cv_ht).grid(row=4, column=2)
entry = Entry(frame1, textvariable=cv_perc_sup).grid(row=5, column=1)
entry = Entry(frame1, textvariable=cv_ht_sup).grid(row=5, column=2)

label = Label(frame1, text="Mana Train").grid(row=6, column=0)
entry = Entry(frame1, textvariable=mt_perc).grid(row=6, column=1)
entry = Entry(frame1, textvariable=mt_ht).grid(row=6, column=2)

label = Label(frame1, text="Cura Mana").grid(row=7, column=0)
entry = Entry(frame1, textvariable=cm_perc).grid(row=7, column=1)
entry = Entry(frame1, textvariable=cm_ht).grid(row=7, column=2)

label = Label(frame1, text="Auto Ring").grid(row=8, column=0)
entry = Entry(frame1, textvariable=ar_ht).grid(row=8, column=1)


#Butões
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var15 = IntVar()
Checkbutton(frame2, text='Food', variable=var1, onvalue=1, offvalue=0,command=food).pack(anchor=W)
Checkbutton(frame2, text='Haste', variable=var2, onvalue=1, offvalue=0,command=haste).pack(anchor=W)
Checkbutton(frame2, text='Anti Paralyze', variable=var6, onvalue=1, offvalue=0,command=paralyze).pack(anchor=W)
Checkbutton(frame2, text='Utamo', variable=var7, onvalue=1, offvalue=0,command=utamo).pack(anchor=W)
Checkbutton(frame2, text='Cura Vida', variable=var3, onvalue=1, offvalue=0,command=cura_vida).pack(anchor=W)
Checkbutton(frame2, text='Cura Mana', variable=var8, onvalue=1, offvalue=0,command=cura_mana).pack(anchor=W)
Checkbutton(frame2, text='Mana Train', variable=var4, onvalue=1, offvalue=0,command=mana_train).pack(anchor=W)
Checkbutton(frame2, text='Background', variable=var5, onvalue=1, offvalue=0,command=background).pack(anchor=W)
Checkbutton(frame2, text='Auto Ring', variable=var11, onvalue=1, offvalue=0,command=ring).pack(anchor=W)
Checkbutton(frame2, text='Player Alert', variable=var12, onvalue=1, offvalue=0,command=player_on_screen).pack(anchor=W)
Checkbutton(frame2, text='Private Mensage', variable=var13, onvalue=1, offvalue=0,command=private_mensage).pack(anchor=W)
Checkbutton(frame2, text='Anti Bot', variable=var15, onvalue=1, offvalue=0,command=anti_bot).pack(anchor=W)

frame2.grid(row=0, column=3, rowspan=8, padx=30)

Button1 = Button(frame1, text="Atualizar HotKeys", command=atualizar).grid(row=0, column=2,rowspan=2,ipadx=5,ipady=5)


##################################################
# Frame Target
##################################################
frame3 = Label(tab2, bg='#dddddd')
frame3.pack()
frame4 = LabelFrame(frame3, text='On/Off')

label = Label(frame3, text="Mana Min.").grid(row=0, column=0)
entry = Entry(frame3, textvariable=min_mana_atack).grid(row=0, column=1)

label = Label(frame3, text="Magia 1").grid(row=1, column=0)
entry = Entry(frame3, textvariable=spell_um_nm).grid(row=1, column=1)
entry = Entry(frame3, textvariable=spell_um_ht).grid(row=1, column=2)

label = Label(frame3, text="Magia 2").grid(row=2, column=0)
entry = Entry(frame3, textvariable=spell_dois_nm).grid(row=2, column=1)
entry = Entry(frame3, textvariable=spell_dois_ht).grid(row=2, column=2)

label = Label(frame3, text="Magia 3").grid(row=3, column=0)
entry = Entry(frame3, textvariable=spell_tres_nm).grid(row=3, column=1)
entry = Entry(frame3, textvariable=spell_tres_ht).grid(row=3, column=2)

var9 = IntVar()
Checkbutton(frame4, text='target', variable=var9, onvalue=1, offvalue=0,command=auto_atack).pack(anchor=W)
var14 = IntVar()
Checkbutton(frame4, text='auto loot', variable=var14, onvalue=1, offvalue=0,command=auto_loot).pack(anchor=W)
var16 = IntVar()
Checkbutton(frame4, text='follow on', variable=var16, onvalue=1, offvalue=0,command=follow_on).pack(anchor=W)
frame4.grid(row=0, column=3, rowspan=8, padx=30)

##################################################
# Frame Cavebot
##################################################

open('cavebot.txt', 'w').close()

frame5 = Label(tab3, bg='#dddddd')
frame5.pack()
Button2 = Button(frame5, text="Encerrar", command=kill_programa).grid(row=0, column=2,rowspan=2,ipadx=5,ipady=5)

frame8 = Label(tab3)
frame8.pack()

frame7 = LabelFrame(tab3, text='')
frame7.pack()
btn_txt=StringVar()
Button3 = Button(frame7, textvariable=btn_txt, command=abrir_lista_scripts).grid(row=0, column=3,rowspan=3,ipadx=5,ipady=5)
btn_txt.set("selecionar script")

frame6 = LabelFrame(frame5, text='On/Off')
var10 = IntVar()
Checkbutton(frame6, text='cavebot', variable=var10, onvalue=1, offvalue=0,command=cavebot).pack(anchor=W)
frame6.grid(row=0, column=3, rowspan=8, padx=30)

frame9 = Label(tab3)
frame9.pack()

st = Label(tab3,justify=LEFT)
st.pack()
def atualizar():
    f = open("cavebot.txt").readlines()
    st.config(text=f)
    st.after(1000,atualizar)
atualizar()


##################################################
# Frame Editor de Cavebot
##################################################

frame10 = Label(tab4, bg='#dddddd')
frame10.pack()
script_name=StringVar()
label10= Label(frame10, text="Nome do Script")
label10.grid(row=0, column=0)
entry10 = Entry(frame10,text='' ,textvariable=script_name)
entry10.grid(row=0, column=1)
text10 = Label(frame10,text='     ',bg='#dddddd')
text10.grid(row=0, column=2)
Button10 = Button(frame10,text='Salvar',command=salvar_script)
Button10.grid(row=0, column=3)
Button11 = Button(frame10,text='Abrir',command=abrir_script)
Button11.grid(row=0, column=4)
Button12 = Button(frame10,text='Novo',command=limpar_script)
Button12.grid(row=0, column=5)
Button13 = Button(frame10,text='Delete',command=delete_script)
Button13.grid(row=0, column=6)

frame11 = Label(tab4)
frame11.pack()

langs = ('goto_label','ajustar_zoom','andar_waypoint','click_sqm','press_tecla','say','comprar_item','vender_itens','label','verifica_andar','verifica_supply','verifica_ammo','target_on','target_off','sleep','check_supply_vai','check_ammo_vai','stop_script','depositar_dp','haste_on','haste_off')
dct = {'goto_label':'goto(<nome da label>)','ajustar_zoom':'ajustar_zoom(<nivel do zoom>)','andar_waypoint':'andar("<nome do waypoint>")','click_sqm':'click_sqm(<sqm>,<botao>,<vezes>)','press_tecla':'press_tecla("<tecla>",<vezes>)','say':'say("<texto>")','comprar_item':'comprar_item(<"nome da img">,<"abreviacao">,<"qtde">)','vender_itens':'vender_itens()','label':'label_<nome da label>','verifica_andar':'andar_get()','verifica_supply':'check_supply("<nome do supply>")','verifica_ammo':'check_ammo()','target_on':'target_on()','target_off':'target_off()','sleep':'sleep(<segundos>)','check_supply_vai':'check_supply_vai(<supply>,<valor>,<label>)','check_ammo_vai':'check_ammo_vai(<ammo>,<valor>,<label>)','stop_script':'stop_script()','depositar_dp':'deposit_dp()','haste_on':'haste_on()','haste_off':'haste_off()'}

var = Variable(value=langs)

listbox = Listbox(
    tab4,
    listvariable=var,
    height=6,
    selectmode=EXTENDED)

listbox.pack(expand=True, fill=BOTH, side=LEFT,anchor='center')

# link a scrollbar to a list
scrollbar = ttk.Scrollbar(
    tab4,
    orient=VERTICAL,
    command=listbox.yview
)

listbox['yscrollcommand'] = scrollbar.set

scrollbar.pack(side=LEFT, expand=True, fill=Y)

@with_goto
def items_selected(event):
    # get selected indices
    selected_indices = listbox.curselection()
    # get selected items
    selected_langs = ",".join([listbox.get(i) for i in selected_indices])
    key_lst=list(dct.keys())
    values_lst=list(dct.values())
    if selected_langs!='' and selected_langs!=f'n':
        key_value=key_lst.index(selected_langs)
        index_value=values_lst[key_value]

        frame11.insert(END,index_value+';\n')


listbox.bind('<<ListboxSelect>>', items_selected)

frame11 = Text(tab4)
frame11.pack()

##################################################

window.mainloop()

######################################################################
#Comandos antes de fechar
######################################################################

kill_programa()