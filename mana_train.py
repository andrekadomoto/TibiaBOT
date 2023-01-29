from main import magia_vida_mana
import json

root = r"parametros.json"

with open(root, 'r') as read_file:
    ler = json.load(read_file)

mt_perc = ler['mt_perc']
mt_ht = ler['mt_ht']

magia_vida_mana(mt_perc,mt_ht,'mt','MAI')

