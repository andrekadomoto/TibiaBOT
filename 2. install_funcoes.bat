@echo off
call venv\Scripts\activate.bat
echo ---------------------------
echo ----- instalando 1/17 -----
echo ---------------------------
pyinstaller .\bot\anti_bot.py --noconfirm

echo ---------------------------
echo ----- instalando 2/17 -----
echo ---------------------------
pyinstaller .\bot\auto_anti_paralyze.py --noconfirm

echo ---------------------------
echo ----- instalando 3/17 -----
echo ---------------------------
pyinstaller .\bot\auto_atack.py --noconfirm

echo ---------------------------
echo ----- instalando 4/17 -----
echo ---------------------------
pyinstaller .\bot\auto_haste.py --noconfirm

echo ---------------------------
echo ----- instalando 5/17 -----
echo ---------------------------
pyinstaller .\bot\auto_loot.py --noconfirm

echo ---------------------------
echo ----- instalando 6/17 -----
echo ---------------------------
pyinstaller .\bot\auto_ring.py --noconfirm

echo ---------------------------
echo ----- instalando 7/17 -----
echo ---------------------------
pyinstaller .\bot\auto_utamo.py --noconfirm

echo ---------------------------
echo ----- instalando 8/17 -----
echo ---------------------------
pyinstaller .\bot\cavebot.py --noconfirm

echo ---------------------------
echo ----- instalando 9/17 -----
echo ---------------------------
pyinstaller .\bot\cura_mana.py --noconfirm

echo ---------------------------
echo ----- instalando 10/17 -----
echo ---------------------------
pyinstaller .\bot\cura_vida.py --noconfirm

echo ---------------------------
echo ----- instalando 11/17 -----
echo ---------------------------
pyinstaller .\bot\eat_food.py --noconfirm

echo ---------------------------
echo ----- instalando 12/17 -----
echo ---------------------------
pyinstaller .\bot\follow_on.py --noconfirm

echo ---------------------------
echo ----- instalando 13/17 -----
echo ---------------------------
pyinstaller .\bot\interface.py --noconfirm

echo ---------------------------
echo ----- instalando 14/17 -----
echo ---------------------------
pyinstaller .\bot\mana_train.py --noconfirm

echo ---------------------------
echo ----- instalando 15/17 -----
echo ---------------------------
pyinstaller .\bot\player_on_screen.py --noconfirm

echo ---------------------------
echo ----- instalando 16/17 -----
echo ---------------------------
pyinstaller .\bot\private_mensage.py --noconfirm

echo ---------------------------
echo ----- instalando 17/17 -----
echo ---------------------------
pyinstaller .\bot\script_reader.py --noconfirm


pause