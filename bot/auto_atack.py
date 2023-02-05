from main import get_qtde_monstros,get_focus_atack,cast_spell,get_mana,auto_loot
import pyautogui
import json
from time import sleep

root = r"parametros.json"

with open(root,'r') as read_file:
    ler = json.load(read_file)

ah = ler['ah_ht']
spell_um_nm = ler['spell_um_nm']
spell_dois_nm = ler['spell_dois_nm']
spell_tres_nm = ler['spell_tres_nm']
spell_um_ht = ler['spell_um_ht']
spell_dois_ht = ler['spell_dois_ht']
spell_tres_ht = ler['spell_tres_ht']
min_mana_atack = ler['min_mana_atack']

while(True):
    try:
        j = get_qtde_monstros()
        if j > 0:
            focus, pos_monstro, vida_monstro, pos_pri_monstro_x, pos_pri_monstro_y = get_focus_atack()
            if focus==0:
                pyautogui.click(x=pos_pri_monstro_x,y=pos_pri_monstro_y)
                sleep(0.1)
                pyautogui.moveTo(534,310)
            mana = get_mana()
            if mana >= min_mana_atack:
                if spell_um_nm!= '':
                    while (True):
                        j1 = pyautogui.locateOnScreen('./imagens/magias/'+spell_um_nm+'.png')
                        if j1 != None:
                            cast_spell(spell_um_nm,spell_um_ht)
                            break
                    if spell_dois_nm != '':
                        while (True):
                            j2 = pyautogui.locateOnScreen('./imagens/magias/'+spell_dois_nm+'.png')
                            if j2 != None:
                                cast_spell(spell_dois_nm, spell_dois_ht)
                                break
                        if spell_tres_nm != '':
                            while (True):
                                j3 = pyautogui.locateOnScreen('./imagens/magias/'+spell_tres_nm+'.png')
                                if j3 != None:
                                    cast_spell(spell_tres_nm, spell_tres_ht)
                                    break
                if spell_dois_nm != '':
                    cast_spell(spell_dois_nm, spell_dois_ht)
                    if spell_tres_nm != '':
                        cast_spell(spell_tres_nm, spell_tres_ht)
                if spell_tres_nm != '':
                    cast_spell(spell_tres_nm, spell_tres_ht)
            j = get_qtde_monstros()
    except:
        continue

