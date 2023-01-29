from main import get_qtde_monstros,get_focus_atack,cast_spell,get_mana,auto_loot
import pyautogui
from time import sleep


while(True):
    try:
        j = get_qtde_monstros()
        while j > 0:
            sleep(1)
            j = get_qtde_monstros()
            if j==0:
                auto_loot()
    except:
        continue

