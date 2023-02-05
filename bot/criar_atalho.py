import os, winshell, win32com.client

print('-- escolha seu ícone --')
print('-- 1. Ferumbras Hat --')
print('-- 2. Tibia Old School --')
print('-- 3. Exercise Sword --')
print('-- 4. Fire Sword --')
num_icone = int(input('>>  '))

if num_icone >=1 or num_icone<=4:
    if num_icone == 1:
        icone = 'ferumbras_hat'
    elif num_icone == 2:
        icone = 'tibia_old_school'
    elif num_icone == 3:
        icone = 'exercise_sword'
    elif num_icone == 4:
        icone = 'fire_sword'
    else:
        print('-- falha ao selecionar ícone --')
        print('-- tente reiniciar o programa --')
        input('Pressione qualquer tecla para continuar..')
        exit()
else:
    print('-- falha ao selecionar ícone --')
    print('-- tente reiniciar o programa --')
    input('Pressione qualquer tecla para continuar..')
    exit()

desktop = winshell.desktop()
#desktop = r"path to where you wanna put your .lnk file"
path = os.path.join(desktop, 'Tibia_BOT.lnk')
target = rf"{os.getcwd()}\4. run_script.bat" 
icon = rf"{os.getcwd()}\imagens\icones\{icone}.ico"
wDir = os.getcwd()
shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.IconLocation = icon
shortcut.WorkingDirectory = wDir
shortcut.save()