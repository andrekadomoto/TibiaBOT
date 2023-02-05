from main import magia_vida_mana
import json

root = r"parametros.json"

with open(root, 'r') as read_file:
    ler = json.load(read_file)

cv_perc = ler['cv_perc']
cv_ht = ler['cv_ht']
cv = ler['cv']

magia_vida_mana(cv_perc,cv_ht,'vida','MEI')



