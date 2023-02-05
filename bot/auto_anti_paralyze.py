from main import verifica_status
import json

root = r"parametros.json"

with open(root,'r') as read_file:
    ler = json.load(read_file)

ap = ler['ap_ht']

verifica_status('paralyze',ap,'p',1)