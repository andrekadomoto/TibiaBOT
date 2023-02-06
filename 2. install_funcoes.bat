@echo off
call venv\Scripts\activate.bat
echo ---------------------------
echo ----- instalando 1/17 -----
echo ---------------------------
pyinstaller .\bot\anti_bot.py -y --clean --specpath ./bot

echo ---------------------------
echo ----- instalando 2/17 -----
echo ---------------------------
pyinstaller .\bot\auto_anti_paralyze.py -y --clean --specpath ./bot

echo ---------------------------
echo ----- instalando 3/17 -----
echo ---------------------------
pyinstaller .\bot\auto_atack.py -y --clean --specpath ./bot

echo ---------------------------
echo ----- instalando 4/17 -----
echo ---------------------------
pyinstaller .\bot\auto_haste.py -y --clean --specpath ./bot

echo ---------------------------
echo ----- instalando 5/17 -----
echo ---------------------------
pyinstaller .\bot\auto_loot.py -y --clean --specpath ./bot

echo ---------------------------
echo ----- instalando 6/17 -----
echo ---------------------------
pyinstaller .\bot\auto_ring.py -y --clean --specpath ./bot

echo ---------------------------
echo ----- instalando 7/17 -----
echo ---------------------------
pyinstaller .\bot\auto_utamo.py -y --clean --specpath ./bot

echo ---------------------------
echo ----- instalando 8/17 -----
echo ---------------------------
pyinstaller .\bot\cavebot.py -y --clean --specpath ./bot

echo ---------------------------
echo ----- instalando 9/17 -----
echo ---------------------------
pyinstaller .\bot\cura_mana.py -y --clean --specpath ./bot

echo ---------------------------
echo ----- instalando 10/17 -----
echo ---------------------------
pyinstaller .\bot\cura_vida.py -y --clean --specpath ./bot

echo ---------------------------
echo ----- instalando 11/17 -----
echo ---------------------------
pyinstaller .\bot\eat_food.py -y --clean --specpath ./bot

echo ---------------------------
echo ----- instalando 12/17 -----
echo ---------------------------
pyinstaller .\bot\follow_on.py -y --clean --specpath ./bot

echo ---------------------------
echo ----- instalando 13/17 -----
echo ---------------------------
pyinstaller .\bot\interface.py -y --clean --specpath ./bot

echo ---------------------------
echo ----- instalando 14/17 -----
echo ---------------------------
pyinstaller .\bot\mana_train.py -y --clean --specpath ./bot

echo ---------------------------
echo ----- instalando 15/17 -----
echo ---------------------------
pyinstaller .\bot\player_on_screen.py -y --clean --specpath ./bot

echo ---------------------------
echo ----- instalando 16/17 -----
echo ---------------------------
pyinstaller .\bot\private_mensage.py -y --clean --specpath ./bot

echo ---------------------------
echo ----- instalando 17/17 -----
echo ---------------------------
pyinstaller .\bot\script_reader.py -y --clean --specpath ./bot


pause