import csv
from main import *
from goto import with_goto

@with_goto
def read_script():
    with open('parametros.json', 'r') as read_file:
        ler = json.load(read_file)
    script=ler['script']
    open('cavebot.txt', 'w').close()
    ficheiro = open(f'./scripts/{script}/{script}.csv', 'r')
    ler = csv.reader(ficheiro,delimiter=';')
    lista_ant = list(ler)
    lista=lista_ant[0][0].split(sep='\n')
    while(True):
        k = 0
        label .inicio
        for i in range(k,len(lista)):
            c=lista[i]

            if c.find('label')>-1 and c.find('goto')==-1: #se for apenas label, ele continua normalmente
                continue

            elif c.find('goto')>-1: #se for goto label, ele identifica para onde deve direcionar com base no index no wp dentro da lista
                goto_var=c.replace('goto(','').replace(')','')
                for j in range(0, len(lista)):
                    d = lista[j]
                    if d.find(goto_var)>-1 and d.find('goto')==-1:
                        k=j
                        goto .inicio

            elif c.find('check_supply_vai')>-1: #se for check supply, ele faz a verificação e direciona ao wp caso atenda aos critérios
                l = []
                for i in range(0, len(c)):
                    x = c[i].find(',')
                    if x != -1:
                        l.append(i)
                supply = c[17:l[0]]
                qtde = int(c[l[0] + 1:l[1]])
                goto_var = c[l[1] + 1:len(c) - 2]
                while True:
                    try:
                        supply_check=eval(supply)
                    except:
                        continue
                    break
                if supply_check <= qtde:
                    for j in range(0, len(lista)):
                        d = lista[j]
                        if d.find('label_'+goto_var)>-1 and d.find('goto')==-1:
                            k=j
                            goto .inicio

            else:
                exec(c)

read_script()