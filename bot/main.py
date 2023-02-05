from audioplayer import AudioPlayer
import PIL.Image
import pyautogui
import json
import win32gui
import win32con
import win32api
from time import sleep
import os
import psutil as ps
import sys
sys.path.insert(0, './TibiaBOT/bot')
from loc_imagem import *

def press_key_bk(key): # pressiona hotkey no background
    for t in range(1,4):
        hwndMain = win32gui.FindWindow(None,"Tibia")
        #hwndChild = win32gui.GetWindow(hwndMain, win32con.GW_CHILD)
        rn = get_command(key)
        temp = win32api.PostMessage(hwndMain, win32con.WM_CHAR, int(rn,0), 0);
        sleep(0.5)

def get_command(key): # buscar o alphanumérico de cada comando
    key="9"
    with open(r'keys.json', 'r') as read_file:
        ler = json.load(read_file)
    try:
        key=int(key)
    except:
        key = key.upper()
    v = list(ler['key'].values())
    newv = v.index(key)
    k = list(ler['func'].get(str(newv)))
    r = ''
    rn = r.join(k)
    return rn

def get_back(): # vefifica se o  modo backgound está ativo ou inativo
    with open(r'parametros_back.json ', 'r') as read_file:
        back = json.load(read_file)
    b = back['back']
    return b

def ativar_janela(janela): # ativa janela do Tibia no background
    toplist = []
    winlist = []

    def enum_callback(hwnd, results):
        winlist.append((hwnd, win32gui.GetWindowText(hwnd)))

    win32gui.EnumWindows(enum_callback, toplist)
    firefox = [(hwnd, title) for hwnd, title in winlist if 'tibia - ' in title.lower()]
    firefox = firefox[0]
    win32gui.SetForegroundWindow(firefox[0])

def check_img(imagem): # def para checar se determinada imagem existe
    start = pyautogui.locateCenterOnScreen(f'./imagens/game_screen/{imagem}.png',confidence=0.9)#If the file is not a png file it will not work
    return start

def get_img(imagem): # procura imagem na tela
    #imagem='battlelist_ini'
    b = get_back()
    if b == 0:
        start = pyautogui.locateCenterOnScreen(f'./imagens/game_screen/{imagem}.png',confidence=0.9)#If the file is not a png file it will not work
    else:
        start = loc_imagem(imagem,cod)
    return start


def image_click(imagem): # clica em imagem de acordo com o nome
    start = pyautogui.locateCenterOnScreen(f'./imagens/game_screen/{imagem}.png',confidence=0.9)#If the file is not a png file it will not work
    if start!=None :
        pyautogui.moveTo(start)#Moves the mouse to the coordinates of the image
        sleep(0.2)
        pyautogui.click(button='left',clicks=5,interval=0.5)
        sleep(0.2)
        pyautogui.moveTo(544, 315)


def get_size(imagem): # retorna o tamanho de uma imagem
    imm = PIL.Image.open(f'./imagens/game_screen/{imagem}.png')
    im=imm.size
    return im

def get_vida():
    x, y, w, h = get_lifebar()
    s=pyautogui.screenshot(region=(x+13,y,w-13,h-2))
    i=95
    j=0
    vida=100
    p=s.getpixel((i,10))
    try:
        while p[0] < 200:
            j+=1
            p = s.getpixel((i-j, 10))
        vida = (100-(100/94)*j)/100
    except:
        vida=0
    return vida

def get_mana():
    x, y, w, h = get_lifebar()
    s=pyautogui.screenshot(region=(x+13,y,w-13,h-2))
    i=95
    j=0
    mana=100
    p=s.getpixel((i,24))
    try:
        while p[2] < 200:
            j+=1
            p = s.getpixel((i-j, 24))
        mana=(100-(100/94)*j)/100
    except:
        mana=0
    return mana


def magia_vida_mana(perc, hotkey,vida_mana,MAI_MEI):
    while(True):
        try:
            if vida_mana == 'vida':

                root = r"parametros.json"
                with open(root, 'r') as read_file:
                    ler = json.load(read_file)
                cv_perc_sup = ler['cv_perc_sup']
                cv_ht_sup = ler['cv_ht_sup']

                vida = get_vida()
                b = get_back()
                if vida == None:
                    continue
                if MAI_MEI == 'MAI': #vida maior ou igual
                    if vida >= perc:
                        if b==0:
                            pyautogui.press(hotkey,presses=6,interval=0.5)
                        else:
                            press_key_bk(hotkey)
                else: #vida menor ou igual
                    if cv_perc_sup!='' and cv_ht_sup!='': #caso tenha setado magia de suporte
                        if vida <= cv_perc_sup:
                            if b==0:
                                pyautogui.press(cv_ht_sup,presses=6,interval=0.5)
                            else:
                                press_key_bk(hotkey)
                        elif vida <= float(perc):
                            if b==0:
                                pyautogui.press(hotkey,presses=6,interval=0.5)
                            else:
                                press_key_bk(hotkey)
                    else: #caso tenha apenas 1 magia de cura
                        if vida <= float(perc):
                            if b==0:
                                pyautogui.press(hotkey,presses=6,interval=0.5)
                            else:
                                press_key_bk(hotkey)
            else:
                mana = get_mana()
                if mana == None:
                    continue
                b = get_back()
                if MAI_MEI == 'MAI': #mana maior ou igual
                    if mana >= perc:
                        if b == 0:
                            pyautogui.press(hotkey, presses=2, interval=0.2)
                        else:
                            press_key_bk(hotkey)
                else: #mana menor ou igual
                    if mana <= perc:
                        if b == 0:
                            pyautogui.press(hotkey, presses=2, interval=0.2)
                        else:
                            press_key_bk(hotkey)
        except:
            continue

def check_status(status,cod):
    #status='haste'
    try:
        b = get_back()
        if b == 0:
            x,y,w,h = get_statusbar()
            strstatus = './imagens/game_screen/' + status + '.png'
            rstatus = pyautogui.locateOnScreen(strstatus,confidence=0.9,region=(int(x),int(y),int(w),int(h)))

        else:
            strstatus = status
            rstatus = loc_imagem(strstatus,cod)

    except:
        rstatus = None

    return rstatus
#check_status('fome','f')

def verifica_status(stat,hotkey,cod,tipo):
    #tipo: 1 = Encontrar ; 0 = Não Encontrar
    while(True):
        try:
            status = check_status(stat,cod)
            b = get_back()
            if tipo == 0:
                if b == 0:
                    #print('s',status)
                    if status == None:
                        pyautogui.press(hotkey, presses=1)
                else:
                    if status > 0.0002:
                        press_key_bk(hotkey)
            else:
                if b == 0:
                    if status != None:
                        #print('status',status)
                        pyautogui.press(hotkey, presses=1)
                else:
                    if status < 0.0002:
                        press_key_bk(hotkey)
        except:
            continue

def get_battlelist():

    img=get_img('battlelist_ini')
    x=img[0] - get_size('battlelist_ini')[0]/2
    x_mod = x + 155
    y=img[1] - get_size('battlelist_ini')[1]/2
    w = 20
    h = pyautogui.size()[1] - y + 5

    l = pyautogui.locateOnScreen(r'./imagens/game_screen/list_fim.png',confidence=0.9, region=(int(x_mod),int(y), int(w), int(h)))

    #w1=get_size('battlelist_inteira')[0]
    w1=171
    h1=l[1]- img[1] + get_size('list_fim')[1] + 8

    xbt=x
    ybt=y
    wbt=w1
    hbt=h1

    return xbt,ybt,wbt,hbt

def get_lifebar():
    img=get_img('icon_vida')
    icon_vida=get_size('icon_vida')
    if img != None and icon_vida != None:
        x=img[0] - icon_vida[0]/2
        y=img[1] - icon_vida[1]/2
        w = 110
        h = 30
    else:
        x=0
        y=0
        w=0
        h=0
    return x,y,w,h


def get_statusbar():
    img=get_img('stop')
    x=img[0] - get_size('stop')[0]/2 - 119
    y=img[1] - get_size('stop')[1]/2
    w = 109
    h = 14
    return x,y,w,h


def get_qtde_monstros():
    x,y,w,h = get_battlelist()
    qtde_monstros = (h-13)//22
    xl = x + 4
    yl = y + 13
    wl = w - 16
    hl = 22
    i = 0
    j = 0
    l = None
    for i in range(0,qtde_monstros):
        color = (0,0,0)
        la = pyautogui.screenshot(region=(int(xl)+24-2,int(yl) + 22 * i+18-2,132,5))
        l = la.getpixel((0,0))
        if l == color:
            #o = pyautogui.screenshot(region=(int(xl)+24-2, int(yl) + 22 * i, int(wl) - 22, int(hl)))
            #o.show()
            # região da barra de vida
            #m = pyautogui.screenshot(region=(int(xl)+24-2,int(yl) + 22 * i+18-2,132,5))
            #m.show()
            # região da figura do monstro
            #n = pyautogui.screenshot(region=(int(xl),int(yl) + 22 * i,20,22))
            #n.show()
            j += 1
    return j


def get_focus_atack():
    x,y,w,h = get_battlelist()
    qtde_monstros = (h-13)//22
    xl = x + 4
    yl = y + 13
    wl = w - 16
    hl = 22
    i = 0
    j = 0
    l = None
    focus = 0
    pos_monstro = 0
    vida_monstro = 0
    pos_pri_monstro_x = int(int(xl) + 20 / 2)
    pos_pri_monstro_y = int(int(yl) + 22 * i + 22 / 2)
    for i in range(0,qtde_monstros):
        color = (244,0,0)
        la = pyautogui.screenshot(region=(int(xl),int(yl) + 22 * i,20,22))
        l = la.getpixel((0,2))
        if l[0] >= color[0]-20:
            focus = 1 #0: não está atacando; 1: está atacando
            pos_monstro = i+1 #retorna a posição do monstro que está atacando dentro da lista
            m = pyautogui.screenshot(region=(int(xl)+24-2,int(yl) + 22 * i+18-2,132,5))
            n = m.getpixel((1,1))
            if n[0]==0 and n[1] >= 180 and n[2]==0:
                vida_monstro=3 #vida do monstro no verde
            elif n[0]==180 and n[1] >= 0 and n[2]==0:
                vida_monstro=1 #vida do monstro no vermelho
            elif n[0]>=200 and n[1] >= 200 and n[2]==0:
                vida_monstro=2 #vida do monstro no amarelo

    return focus,pos_monstro,vida_monstro,pos_pri_monstro_x,pos_pri_monstro_y

def cast_spell(magia,hotkey):
    caminho_magia = './imagens/magias/' + magia + '.png'
    j = pyautogui.locateCenterOnScreen(caminho_magia)
    if j != None:
        pyautogui.press(hotkey, presses=1)


def get_minimap():
    #Retorna a localização do char no minimapa
    # 0: chegou ao waypoint
    # 1: ainda está andando
    o = pyautogui.locateOnScreen(r'./imagens/game_screen/minimap.png')
    xc = o.left-13-106
    yc = o.top-92
    wc = 106
    hc = 109
    return xc,yc,wc,hc

def get_andar():
    o = pyautogui.locateOnScreen(r'./imagens/game_screen/minimap.png')
    while o==None:
        o = pyautogui.locateOnScreen('./imagens/game_screen/minimap.png')
    xc = o.left-13-106+108
    yc = o.top-92
    wc = 58
    hc = 109+8
    p = pyautogui.locateOnScreen(r'./imagens/game_screen/seta_mapa.png', region=(xc, yc, wc, hc), confidence=0.8)
    while p==None:
        p=pyautogui.locateOnScreen(r'./imagens/game_screen/seta_mapa.png',region=(xc,yc,wc,hc), confidence=0.8)
    andar = ((((p.top-74)/4)-7)*-1)-0.75
    return andar

def check_position():
    xc, yc, wc, hc = get_minimap()
    p = pyautogui.screenshot(region=(xc,yc,wc,hc))
    color = (255,255,255)
    posicao=0
    for x in range(p.width):
        for y in range(p.height):
            if p.getpixel((x,y)) == color:
                posicao += 1
    return posicao

def auto_loot():
    pyautogui.click(x=495, y=275, button='right', clicks=2)
    pyautogui.click(x=495, y=318, button='right', clicks=2)
    pyautogui.click(x=495, y=362, button='right', clicks=2)
    pyautogui.click(x=540, y=275, button='right', clicks=2)
    pyautogui.click(x=540, y=362, button='right', clicks=2)
    pyautogui.click(x=585, y=275, button='right', clicks=2)
    pyautogui.click(x=585, y=318, button='right', clicks=2)
    pyautogui.click(x=585, y=362, button='right', clicks=2)
    pyautogui.moveTo(544, 315)


def check_ammo():
    lst=['0','1','2','3','4','5','6','7','8','9']
    s = pyautogui.locateOnScreen(r'./imagens/game_screen/pvp.png')
    var1='0'
    var2='0'
    var3='0'
    var4='0'
    i=1
    while i <= 4:
        for j in lst:
            x=s.left - 11 -8*i
            y=s.top
            w=8
            h=10
            u = pyautogui.locateOnScreen(f'./imagens/numeros/ammo/{j}.png',region=(x,y,w,h),confidence=0.89)
            if u != None:
                if i==1:
                    var1 = j
                elif i==2:
                    var2 = j
                elif i==3:
                    var3 = j
                elif i==4:
                    var4 = j
        i+=1
    ammo_str = var4+var3+var2+var1
    ammo = int(ammo_str)
    return ammo

def check_supply(supply='great_mana_potion'):
    lst=['0','1','2','3','4','5','6','7','8','9']
    var1='0'
    var2='0'
    var3='0'
    var4='0'
    i=1
    while i <= 4:
        for j in lst:
            x=2
            y=98
            x_f=0
            y_f=0
            q=pyautogui.locateCenterOnScreen(f'./imagens/itens/{supply}.png',region=(0,96,70,430),confidence=0.9)
            #r = pyautogui.screenshot(region=(q.x, q.y, 31, 31))
            #r = pyautogui.screenshot(region=(0,96,70,430))
            #r.show()
            coluna=round((q.x-x)/31)
            linha=round((q.y-y)/31)
            #r = pyautogui.screenshot(region=(2, 205+36, 31, 31))
            #r.show()
            #i=3
            #j=7
            if coluna<=1:
                x_f=2
            else:
                x_f=38
            y_f=97+(linha-1)*36
            u = pyautogui.locateOnScreen(f'./imagens/numeros/supply/{j}.png', region=(x_f+31-6*i,y_f+31-8,6,8), confidence=0.85)
            #u = pyautogui.screenshot(region=(x_f+31-6*i,y_f+31-8,6,8))
            #u = pyautogui.screenshot(region=(x_f,y_f,31,31))
            #u.show()
            if u != None:
                if i==1:
                    var1 = j
                elif i==2:
                    var2 = j
                elif i==3:
                    var3 = j
                elif i==4:
                    var4 = j
        i+=1
    supply_str = var4+var3+var2+var1
    supply = int(supply_str)
    return supply

def andar(waypoint):
    #tenta localizar o waypoint 5 vezes e encerra caso não encontre
    #anda apenas se o battle list estiver vazio
    #fica clicando no waypoint até não localizar pixel branco ou até mudar de andar
    log_cavebot(f'andando para wp: {waypoint}')
    with open(r'parametros.json', 'r') as read_par:
        par = json.load(read_par)
    target = par['auto_atack']

    xc,yc,wc,hc = get_minimap()

    wp = './imagens/waypoints/' + waypoint + '.png'
    posicao = 1
    j = 1
    qtde_erro = 0
    qtde_zero = 0
    trap = 0
    while qtde_zero <= 2: #tentativas de localizar o wp
        posicao = check_position()
        if target==1: #verificação da battlelist caso auto_atack esteja ativo
            j = get_qtde_monstros() #verifica quantidade de monstros
            #t1 = datetime.now()
            while j > 0: #enquanto estiver com monstros, fica no sleep
                #from datetime import datetime
                sleep(0.2)
                j = get_qtde_monstros()
                #t2 = datetime.now()
                #t_delta=t2-t1
                #if t_delta.seconds>30: #não fica mais de 30 segundos no mesmo waypoint
                    #break
                if j==0:
                    auto_loot()

        l = pyautogui.locateCenterOnScreen(wp, region=(xc, yc, wc, hc)) #tenta localizar o wp

        if l!=None: #caso encontre o wp
            andar_antes=get_andar() #pega o andar atual
            l = pyautogui.locateCenterOnScreen(wp, region=(xc, yc, wc, hc))  # tenta localizar o wp
            pyautogui.click(l) #clica no wp
            no_way = pyautogui.locateOnScreen('./imagens/game_screen/no_way.png',confidence=0.8) #verifica se a mensagem de There is no way aparece na tela
            if no_way != None: #caso encontre o No Way
                trap+=1
                if trap >= 4: #encerra se não conseguir andar mais de 6 vezes
                    pyautogui.moveTo(544, 315)
                    break
            andar_depois=get_andar() #pega andar depois
            if andar_depois!=andar_antes: #encerra caso mude de andar
                pyautogui.moveTo(544, 315)
                break
            pyautogui.moveTo(544, 315)
            if posicao==0: #soma contador de zeros até 6 para encerrar o wp
                qtde_zero+=1

        else: #caso não encontre o wp
            qtde_erro+=1
            if qtde_erro>=5:
                break

def target_on():
    log_cavebot('target on')
    with open(r'parametros.json', 'r') as read_file:
        ler = json.load(read_file)
    ler['auto_atack'] = 1
    with open(r'parametros.json', 'w') as f:
        json.dump(ler, f)
    c=0
    for proc in ps.process_iter():
        info = proc.as_dict(attrs=['pid', 'name'])
        x = info['name'].find('auto_atack')
        if x != -1:
            c+=1
    if c==0:
        os.spawnl(os.P_DETACH, r'dist\auto_atack\auto_atack.exe', 'x')
    elif c>1:
        os.system("taskkill /im auto_atack.exe /F")
        sleep(0.5)
        os.spawnl(os.P_DETACH, r'dist\auto_atack\auto_atack.exe', 'x')

def target_off():
    with open(r'parametros.json', 'r') as read_file:
        ler = json.load(read_file)
    ler['auto_atack'] = 0
    with open(r'parametros.json', 'w') as f:
        json.dump(ler, f)
    os.system("taskkill /im auto_atack.exe /F")

def get_janela_compra():
    img=get_img('npc_trade')
    x=img[0] - get_size('npc_trade')[0]/2
    x_mod = x + 155
    y=img[1] - get_size('npc_trade')[1]/2
    w = 20
    h = pyautogui.size()[1] - y + 5

    l = pyautogui.locateOnScreen(r'./imagens/game_screen/list_fim.png',confidence=0.9, region=(int(x_mod),int(y), int(w), int(h)))

    #w1=get_size('battlelist_inteira')[0]
    w1=171
    h1=l[1]- img[1] + get_size('list_fim')[1] + 8

    x_1=int(x)
    y_1=int(y+57)
    w_1=int(w1)
    h_1=int(h1-57)

    x_2=int(x)
    y_2=int(y+64+100)
    w_2=int(w1)
    h_2=int(h1-73)

    #p1=pyautogui.screenshot(region=(x_1,y_1,w_1,h_1))
    #p1.show()
    #p2=pyautogui.screenshot(region=(x_2,y_2,w_2,h_2))
    #p2.show()

    return x_1,y_1,w_1,h_1,x_2,y_2,w_2,h_2

def vender_itens():
    log_cavebot('vendendo itens')
    verifica_aba_npc()

    verifica_chat('on')
    pyautogui.press('backspace',presses=10,interval=0.2)
    janela_trade = check_img('npc_trade')
    while janela_trade == None:
        pyautogui.write('hi trade')
        pyautogui.press('enter')
        janela_trade = check_img('npc_trade')
        sleep(1)
    verifica_chat('off')

    x_1, y_1, w_1, h_1, x_2, y_2, w_2, h_2 = get_janela_compra()

    janela_sell = check_img('sell_focus_off')

    while janela_sell != None:
        sell_btn = pyautogui.locateCenterOnScreen('./imagens/game_screen/sell_focus_off.png')
        pyautogui.click(sell_btn)
        sleep(0.2)
        pyautogui.moveTo(544, 315)
        janela_sell = check_img('sell_focus_off')

    i = 0
    janela_itens = pyautogui.screenshot(region=(x_1, y_1, w_1, h_1))
    while i < janela_itens.size[1]:
        janela_itens = pyautogui.screenshot(region=(x_1,y_1,w_1,h_1))
        i = 0
        p=janela_itens.getpixel((47,i))
        while p != (192,192,192) and i < janela_itens.size[1]:
            p = janela_itens.getpixel((47, i))
            i += 1
            if p == (192,192,192):
                pyautogui.click(int(x_1)+47,int(y_1)+i)
                sleep(0.2)
                pyautogui.moveTo(544, 315)
                seta_direita = pyautogui.locateOnScreen(r'./imagens/game_screen/npc_trade_seta_direita.png',region=(int(x_2),int(y_2),int(w_2),int(h_2)))
                pyautogui.click(seta_direita.left-7,seta_direita.top+3,clicks=3)
                sleep(0.2)
                pyautogui.moveTo(544, 315)
                ok_btn = pyautogui.locateCenterOnScreen(r'./imagens/game_screen/npc_trade_ok.png',region=(int(x_2),int(y_2),int(w_2),int(h_2)))
                pyautogui.click(ok_btn,clicks=3)
                sleep(0.2)
                pyautogui.moveTo(544, 315)
                continue

    verifica_chat('on')
    pyautogui.press('backspace',presses=10,interval=0.2)
    janela_trade = check_img('npc_trade')
    while janela_trade != None:
        pyautogui.write('bye')
        pyautogui.press('enter')
        janela_trade = check_img('npc_trade')
        sleep(1)
    verifica_chat('off')


def ajustar_zoom(nivel):
    log_cavebot(f'ajustando zoom para: {nivel}')
    p=pyautogui.locateCenterOnScreen(r'./imagens/game_screen/zoom_in.png')
    pyautogui.click(p,clicks=10)
    p = pyautogui.locateCenterOnScreen(r'./imagens/game_screen/zoom_out.png')
    pyautogui.click(p, clicks=nivel)
    sleep(0.2)
    pyautogui.moveTo(544,315)

def click_sqm(sqm,botao='left',qtd=1):
    if sqm==1:
        pyautogui.click(x=500, y=274,button=botao,clicks=qtd)
    elif sqm==2:
        pyautogui.click(x=530, y=266,button=botao, clicks=qtd)
    elif sqm == 3:
        pyautogui.click(x=585, y=275,button=botao, clicks=qtd)
    elif sqm == 4:
        pyautogui.click(x=498, y=318,button=botao, clicks=qtd)
    elif sqm == 5:
        pyautogui.click(x=544, y=315, button=botao, clicks=qtd)
    elif sqm == 6:
        pyautogui.click(x=582, y=317,button=botao, clicks=qtd)
    elif sqm == 7:
        pyautogui.click(x=500, y=361,button=botao, clicks=qtd)
    elif sqm == 8:
        pyautogui.click(x=539, y=359,button=botao, clicks=qtd)
    elif sqm==9:
        pyautogui.click(x=585, y=359,button=botao, clicks=qtd)

def say(texto):
    log_cavebot(f'say: {texto}')
    verifica_chat('on')
    pyautogui.write(texto)
    pyautogui.press('enter')
    verifica_chat('off')

def comprar_itens(item,texto,total):
    log_cavebot(f'comprando: {item}')
    verifica_aba_npc()

    verifica_chat('on')
    pyautogui.press('backspace', presses=10, interval=0.2)
    janela_trade = check_img('npc_trade')
    while janela_trade == None:
        pyautogui.write('hi trade')
        pyautogui.press('enter')
        janela_trade = check_img('npc_trade')
        sleep(1)
    verifica_chat('off')

    busca = pyautogui.locateOnScreen(r'./imagens/game_screen/type_search.png', confidence=0.9)
    pyautogui.click(busca)
    sleep(0.2)
    pyautogui.moveTo(544, 315)
    pyautogui.write(texto)
    pyautogui.press('esc',presses=3)

    sleep(1.5)

    item_txt = pyautogui.locateOnScreen(f'./imagens/game_screen/{item}.png', confidence=0.8)
    pyautogui.click(item_txt)

    quantidade = pyautogui.locateOnScreen(r'./imagens/game_screen/compra_selecionada.png', confidence=0.9)
    pyautogui.click(quantidade)
    pyautogui.press('backspace',presses=3,interval=0.2)
    pyautogui.press('del', presses=3, interval=0.2)
    pyautogui.write(total)
    sleep(0.2)
    pyautogui.moveTo(544, 315)
    sleep(1)
    ok_btn = pyautogui.locateOnScreen(r'./imagens/game_screen/npc_trade_ok.png', confidence=0.9)
    pyautogui.click(ok_btn,button='left',clicks=3)
    pyautogui.press('esc', presses=3)
    sleep(1)
    pyautogui.moveTo(544, 315)

    verifica_aba_npc()

    verifica_chat('on')
    pyautogui.press('backspace', presses=10, interval=0.2)
    janela_trade = check_img('npc_trade')
    while janela_trade != None:
        pyautogui.write('bye')
        pyautogui.press('enter')
        janela_trade = check_img('npc_trade')
        sleep(1)
    verifica_chat('off')

def chat_on():
    chat_off = pyautogui.locateOnScreen(r'./imagens/game_screen/chat_off.png')
    while chat_off != None:
        pyautogui.click(chat_off)
        chat_off = pyautogui.locateOnScreen(r'./imagens/game_screen/chat_off.png')
    sleep(0.2)
    pyautogui.moveTo(544, 315)


def chat_off():
    chat_on = pyautogui.locateOnScreen(r'./imagens/game_screen/chat_on.png')
    while chat_on != None:
        pyautogui.click(chat_on)
        chat_on = pyautogui.locateOnScreen(r'./imagens/game_screen/chat_on.png')
    sleep(0.2)
    pyautogui.moveTo(544, 315)

def chat_npc_active():
    chat_npc = pyautogui.locateOnScreen(r'./imagens/game_screen/chat_npc_off.png')
    while chat_npc != None:
        pyautogui.click(chat_npc)
        chat_npc = pyautogui.locateOnScreen(r'./imagens/game_screen/chat_npc_off.png')
    sleep(0.2)
    pyautogui.moveTo(544, 315)

def verifica_chat(desejo):
    c=pyautogui.locateOnScreen(r'./imagens/game_screen/chat_on.png')
    if c==None:
        c=pyautogui.locateOnScreen(r'./imagens/game_screen/chat_off.png')
        estado='off'
    else:
        estado='on'
    if desejo!=estado:
        p=pyautogui.locateCenterOnScreen(r'./imagens/game_screen/chat.png')
        pyautogui.click(p)
    sleep(0.2)
    pyautogui.moveTo(544, 315)

def press_tecla(tecla,i=1):
    log_cavebot(f'pressionando tecla: {tecla}')
    verifica_chat('off')
    pyautogui.press(tecla,presses=i,interval=0.2)

def verifica_aba_npc():
    c=pyautogui.locateCenterOnScreen(r'./imagens/game_screen/aba_npc_off.png')
    if c==None:
        c=pyautogui.locateOnScreen(r'./imagens/game_screen/aba_npc_on.png')
        if c==None:
            d=pyautogui.locateCenterOnScreen(r'./imagens/game_screen/pastas.png')
            pyautogui.click(d)
            sleep(0.1)
            e=pyautogui.locateCenterOnScreen(r'./imagens/game_screen/aba_npc.png')
            pyautogui.click(e)
            sleep(0.1)
            f=pyautogui.locateCenterOnScreen(r'./imagens/game_screen/aba_open.png')
            pyautogui.click(f)
    pyautogui.click(c)

def auto_ring(hotkey='u'):
    while(True):
        try:
            p=pyautogui.locateCenterOnScreen(r'./imagens/game_screen/ring_off.png')
            if p!=None:
                pyautogui.press(hotkey)
        except:
            continue

def get_game_window():
    x=pyautogui.locateOnScreen(r'./imagens/game_screen/abas_hotkey_cima.png')
    for i in range(1,430):
        p=pyautogui.screenshot()
        pixels=p.getpixel((x.left+i,x.top+220))
        n1=pixels[0]-pixels[1]
        n2=pixels[1]-pixels[2]
        n3=pixels[2]-pixels[0]
        a1=abs(n1)>20
        a2=abs(n1)>20
        a3=abs(n1)>20
        a1+a2+a3
        if (a1+a2+a3)>=2 or ((abs(n1)+abs(n2)+abs(n3))/3)>10:
            xc=x.left+i
            break

    y=pyautogui.locateOnScreen(r'./imagens/game_screen/xp_icon.png')
    yc=y.top+37

    wc=647,
    hc=474

    return xc,yc,wc,hc

def private_msg():
    xc, yc, wc, hc = get_game_window()
    while(True):
        try:
            parar = 0
            scr=pyautogui.screenshot(region=(xc,yc,647,474))
            for i in range(1,scr.size[0]):
                for j in range(1,scr.size[1]):
                    pixel=scr.getpixel((i,j))
                    if pixel==(96,248,248):
                        AudioPlayer("./audio/alerta_mensagem.mp3").play(block=True)
                        parar=1
                        break
                    if parar==1:
                        break
        except:
            continue


def player_on_screen():
    while(True):
        try:
            p=pyautogui.locateOnScreen(r'./imagens/game_screen/battlelist_ini_player.png')
            size=pyautogui.size()
            f=pyautogui.locateOnScreen(r'./imagens/game_screen/list_fim_2.png',region=(p.left,p.top,size.width-p.left,size.height-p.top),confidence=0.6)
            ptr=pyautogui.screenshot(region=(p.left,p.top,size.width-p.left,f.top-f.height-p.top))
            for i in range(1,ptr.size[1]):
                pixel=ptr.getpixel((50,i))
                if pixel==(0,0,0):
                    AudioPlayer(r"./audio/player_na_tela.mp3").play(block=True)
                    break
        except:
            continue


def log_cavebot(txt):
    f = open(r"cavebot.txt", "a")
    f.writelines([f"{txt}\n"])
    f.close()

def anti_bot():
    while(True):
        try:
            f=pyautogui.locateOnScreen(r'./imagens/game_screen/anti_bot.png')
            if f==None:
                AudioPlayer(r"./audio/player_na_tela.mp3").play(block=True)
        except:
            continue

def follow_on():
    while(True):
        try:
            f=pyautogui.locateCenterOnScreen(r'./imagens/game_screen/follow_off.png')
            if f!= None:
                pyautogui.click(f)
                sleep(0.2)
                pyautogui.moveTo(544, 315)
        except:
            continue

def follow_off():
    while(True):
        try:
            f=pyautogui.locateCenterOnScreen(r'./imagens/game_screen/follow_on.png')
            if f!= None:
                pyautogui.click(f)
                sleep(0.2)
                pyautogui.moveTo(544, 315)
        except:
            continue


def deposit_dp():
    #anda para spot do DP
    #dp_spot=pyautogui.locateCenterOnScreen('dp_spot.png',confidence=0.7)
    #pyautogui.moveTo(dp_spot)
    #pyautogui.click(button='left')

    #verifica se chegou no spot
    t=0
    while t==0:
        dp_spot = pyautogui.locateCenterOnScreen(r'./imagens/game_screen/dp_spot.png', confidence=0.7)
        pyautogui.moveTo(dp_spot)
        pyautogui.click(button='left')
        sleep(3)
        for w in range(0,99):
                dp_pixel=pyautogui.pixelMatchesColor(502+99-w, 280+99-w,(174,60,15),tolerance=10)
                if dp_pixel==True:
                    t=1
                    break

    sleep(0.2)
    #verifica se há uma caixa do DP em volta
    x=544-39
    y=315-80
    w=69
    h=132

    #clica no box do dp
    locker=pyautogui.locateCenterOnScreen(r'./imagens/game_screen/locker.png',confidence=0.8)
    while locker==None:
        locker = pyautogui.locateCenterOnScreen(r'./imagens/game_screen/locker.png',confidence=0.8)
        if locker != None:
            break
        else:
            k = pyautogui.locateCenterOnScreen(r'./imagens/game_screen/dp_box.png', region=(x, y, w, h), confidence=0.9)
            pyautogui.moveTo(k)
            pyautogui.click(button='right')

    #fecha bp aberta
    backpack_open=pyautogui.locateOnScreen(r'./imagens/game_screen/backpack.png',confidence=0.8)
    while backpack_open != None:
        backpack_open=pyautogui.locateOnScreen(r'./imagens/game_screen/backpack.png',confidence=0.8)
        if backpack_open == None:
            break
            sleep(0.2)
        else:
            fechar = pyautogui.locateCenterOnScreen(r'./imagens/game_screen/fechar.png',region=(backpack_open.left, backpack_open.top, 170, 15),confidence=0.8)
            pyautogui.moveTo(fechar)
            pyautogui.click(button='left')
        sleep(0.2)
    del backpack_open
    sleep(0.5)

    #reabre janela da bp
    backpack_open = pyautogui.locateCenterOnScreen(r'./imagens/game_screen/backpack.png')
    while backpack_open == None:
        backpack_open = pyautogui.locateCenterOnScreen(r'./imagens/game_screen/backpack.png')
        if backpack_open != None:
            break
            sleep(0.2)
        else:
            storage = pyautogui.locateOnScreen(r'./imagens/game_screen/storage_inbox.png')
            pyautogui.moveTo(storage.left + 18, storage.top + 32)
            pyautogui.click(button='right')
        sleep(0.2)
    del backpack_open

    #encontra o fim da BP
    backpack_open_2 = pyautogui.locateOnScreen(r'./imagens/game_screen/backpack.png')
    fim_bp=pyautogui.locateOnScreen(r'./imagens/game_screen/list_fim.png',region=(backpack_open_2.left-20+158,backpack_open_2.top,20,400),confidence=0.8)
    pyautogui.moveTo(fim_bp.left-30,fim_bp.top+14)
    pyautogui.drag(0, 100, button='left')

    #mapeia variaveis para stockar
    backpack_open_2 = pyautogui.locateOnScreen(r'./imagens/game_screen/backpack.png')
    fim_bp = pyautogui.locateOnScreen(r'./imagens/game_screen/list_fim.png',region=(backpack_open_2.left - 20 + 158, backpack_open_2.top, 20, 400),confidence=0.8)
    item_valuables = os.listdir('./imagens/valuables')
    backpacks = os.listdir('./imagens/containers')

    # primeira ve se tem algum item valioso na bp principal
    m=0
    while m==0:
        o=0
        for l in item_valuables:
            item=pyautogui.locateCenterOnScreen(f'./imagens/valuables/'+l,region=(-10+backpack_open_2.left,backpack_open_2.top,fim_bp.left- backpack_open_2.left+10,fim_bp.top- backpack_open_2.top+10),confidence=0.8)
            if item != None:
                stash=pyautogui.locateCenterOnScreen(r'./imagens/game_screen/stash.png',confidence=0.8)
                pyautogui.moveTo(item)
                pyautogui.dragTo(stash.x,stash.y,button='left')
            else:
                o+=1
        if o==len(item_valuables):
            break

    # abre todas as bps e procura item valioso
    j=0
    while j==0:
        k=0
        for i in backpacks:
            bp=pyautogui.locateCenterOnScreen(f'./imagens/containers/'+i,region=(-10+backpack_open_2.left,backpack_open_2.top,fim_bp.left- backpack_open_2.left+10,fim_bp.top- backpack_open_2.top+10),confidence=0.8)
            if bp != None:
                pyautogui.moveTo(bp)
                pyautogui.click(button='right')
                #verifica itens valiosos
                m = 0
                while m == 0:
                    o = 0
                    for l in item_valuables:
                        item = pyautogui.locateCenterOnScreen(f'./imagens/valuables/' + l, region=(
                        -10 + backpack_open_2.left, backpack_open_2.top, fim_bp.left - backpack_open_2.left + 10,
                        fim_bp.top - backpack_open_2.top + 10), confidence=0.8)
                        if item != None:
                            stash = pyautogui.locateCenterOnScreen(r'./imagens/game_screen/stash.png', confidence=0.8)
                            pyautogui.moveTo(item)
                            pyautogui.dragTo(stash.x, stash.y, button='left')
                        else:
                            o += 1
                    if o == len(item_valuables):
                        break
            else:
                k+=1
        if k==len(backpacks):
            break

    # fecha bp aberta
    backpack_open = pyautogui.locateOnScreen(r'./imagens/game_screen/backpack.png',confidence=0.8)
    while backpack_open != None:
        backpack_open = pyautogui.locateOnScreen(r'./imagens/game_screen/backpack.png',confidence=0.8)
        if backpack_open==None:
            break
            sleep(0.2)
        else:
            fechar = pyautogui.locateCenterOnScreen(r'./imagens/game_screen/fechar.png',region=(backpack_open.left, backpack_open.top, 170, 15),confidence=0.8)
            pyautogui.moveTo(fechar)
            pyautogui.click(button='left')
        sleep(0.2)
    del backpack_open
    sleep(0.5)

    # reabre janela da bp
    backpack_open = pyautogui.locateCenterOnScreen(r'./imagens/game_screen/backpack.png',confidence=0.8)
    while backpack_open == None:
        backpack_open = pyautogui.locateCenterOnScreen(r'./imagens/game_screen/backpack.png',confidence=0.8)
        if backpack_open!=None:
            break
            sleep(0.2)
        else:
            storage = pyautogui.locateOnScreen(r'./imagens/game_screen/storage_inbox.png')
            pyautogui.moveTo(storage.left + 18, storage.top + 32)
            pyautogui.click(button='right')
        sleep(0.2)
    del backpack_open

def haste_on():
    log_cavebot('haste on')
    c=0
    for proc in ps.process_iter():
        info = proc.as_dict(attrs=['pid', 'name'])
        x = info['name'].find('auto_haste')
        if x != -1:
            c+=1
    if c==0:
        os.spawnl(os.P_DETACH, r"dist\auto_haste\auto_haste.exe", 'x')
    elif c>1:
        os.system("taskkill /im auto_haste.exe /F")
        sleep(0.5)
        os.spawnl(os.P_DETACH, r"dist\auto_haste\auto_haste.exe", 'x')

def haste_off():
    log_cavebot('hast off')
    os.system("taskkill /im auto_haste.exe /F")

######################################################################################
#SUPORTE
######################################################################################
#sleep(3)
#x,y,w,h = get_battlelist()
#x,y,w,h = get_lifebar()
#x,y,w,h = get_statusbar()
#im = pyautogui.screenshot(region=(int(x),int(y),int(w),int(h)))
#l = pyautogui.locateOnScreen('haste.png',confidence=.9 ,region=(int(x),int(y),int(w),int(h)))
#im.show()
#status = check_status('haste','h')
#print('l:',l,' status: ',status)
#x=pyautogui.position()
#y=pyautogui.screenshot()
#y.getpixel((x.x,x.y))
#print(x)

