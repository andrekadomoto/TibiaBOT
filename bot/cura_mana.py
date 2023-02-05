from main import magia_vida_mana,get_mana
import json

root = r"parametros.json"

with open(root, 'r') as read_file:
    ler = json.load(read_file)

cm_perc = ler['cm_perc']
cm_ht = ler['cm_ht']
cm = ler['cm']

magia_vida_mana(cm_perc,cm_ht,'mana','MEI')

