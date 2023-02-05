from main import *
import json

root = r"parametros.json"

with open('parametros.json', 'r') as read_file:
    ler = json.load(read_file)
hotkey = ler['ar_ht']

auto_ring(hotkey)