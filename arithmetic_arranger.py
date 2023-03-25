import re

def arithmetic_arranger(lista, results=False):
    new_list = [item.split() for item in lista]
    error = False
    for item in new_list:
        if len(item[0]) > 4:
            print("\nERRO: Não posso processar números maiores do que quatro dígitos")
            error = True
        elif len(item[2]) > 4:
            print("\nERRO: Não posso processar números maiores do que quatro dígitos")
            error = True
        elif '/' in item or '*' in item:
            print("\nERRO: Somente aceito soma e subtração")
            error = True
    if len(lista) < 5 and error == False:
        print('\n')
        new_list = [item.split() for item in lista]
        for lista in new_list:
            for i in range(4):
                if(len(lista[0])) == i + 1:
                    lista[0] = ' ' * (5 - i) + lista[0]
            for i in range(4):
                if(len(lista[2])) == i + 1:
                    lista[2] = ' ' * (3 - i) + lista[2] 
            print(lista[0], end='    ')
        print()
        for lista in new_list:
            print( lista[1] + ' ' + lista[2], end='    ')
        print()
        for lista in new_list:
            print('------', end='    ')
        if results:
            print()
            for item in new_list:
                if '+' in item:
                    item.remove('+')
                    apenas_numeros = re.sub(r"[^0-9]", "", item[0])
                    apenas_numeros_2 = re.sub(r"[^0-9]", "", item[1])
                    soma = int(apenas_numeros) + int(apenas_numeros_2)
                    print(' ', soma, end='     ')
                if '-' in item:
                    item.remove('-')
                    apenas_numeros = re.sub(r"[^0-9]", "", item[0])
                    apenas_numeros_2 = re.sub(r"[^0-9]", "", item[1])
                    sub = int(apenas_numeros) - int(apenas_numeros_2)
                    print(' ', sub, end='     ')
        print('\n')
    elif len(lista) >= 5:
        print("\nERRO: Não posso processar mais de 4 cálculos\n")
        
arithmetic_arranger(["45 + 445", "5 - 44", "67 + 30", "7890 - 8"], results=True)

