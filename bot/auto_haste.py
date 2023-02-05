from main import verifica_status
import json

root = r"parametros.json"

with open(root,'r') as read_file:
    ler = json.load(read_file)

ah = ler['ah_ht']

verifica_status('haste',ah,'h',0)