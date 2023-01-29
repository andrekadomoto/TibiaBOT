@echo off
call venv\Scripts\activate.bat
echo ---------------------------
echo ----- instalando 1/17 -----
echo ---------------------------
pyinstaller anti_bot.py --noconfirm

echo ---------------------------
echo ----- instalando 2/17 -----
echo ---------------------------
pyinstaller auto_anti_paralyze.py --noconfirm

echo ---------------------------
echo ----- instalando 3/17 -----
echo ---------------------------
pyinstaller auto_atack.py --noconfirm

echo ---------------------------
echo ----- instalando 4/17 -----
echo ---------------------------
pyinstaller auto_haste.py --noconfirm

echo ---------------------------
echo ----- instalando 5/17 -----
echo ---------------------------
pyinstaller auto_loot.py --noconfirm

echo ---------------------------
echo ----- instalando 6/17 -----
echo ---------------------------
pyinstaller auto_ring.py --noconfirm

echo ---------------------------
echo ----- instalando 7/17 -----
echo ---------------------------
pyinstaller auto_utamo.py --noconfirm

echo ---------------------------
echo ----- instalando 8/17 -----
echo ---------------------------
pyinstaller cavebot.py --noconfirm

echo ---------------------------
echo ----- instalando 9/17 -----
echo ---------------------------
pyinstaller cura_mana.py --noconfirm

echo ---------------------------
echo ----- instalando 10/17 -----
echo ---------------------------
pyinstaller cura_vida.py --noconfirm

echo ---------------------------
echo ----- instalando 11/17 -----
echo ---------------------------
pyinstaller eat_food.py --noconfirm

echo ---------------------------
echo ----- instalando 12/17 -----
echo ---------------------------
pyinstaller follow_on.py --noconfirm

echo ---------------------------
echo ----- instalando 13/17 -----
echo ---------------------------
pyinstaller interface.py --noconfirm

echo ---------------------------
echo ----- instalando 14/17 -----
echo ---------------------------
pyinstaller mana_train.py --noconfirm

echo ---------------------------
echo ----- instalando 15/17 -----
echo ---------------------------
pyinstaller player_on_screen.py --noconfirm

echo ---------------------------
echo ----- instalando 16/17 -----
echo ---------------------------
pyinstaller private_mensage.py --noconfirm

echo ---------------------------
echo ----- instalando 17/17 -----
echo ---------------------------
pyinstaller script_reader.py --noconfirm


pause