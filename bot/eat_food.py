from main import verifica_status
import json

root = r"parametros.json"

with open(root,'r') as read_file:
    ler = json.load(read_file)

ef_ht = ler['ef_ht']

verifica_status('fome',ef_ht,'f',1)

