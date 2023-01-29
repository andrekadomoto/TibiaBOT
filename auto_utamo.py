from main import verifica_status
import json

root = r"parametros.json"

with open(root,'r') as read_file:
    ler = json.load(read_file)

au = ler['au_ht']

verifica_status('utamo',au,'u',0)