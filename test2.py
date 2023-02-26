import random


def add(n1, n2):
    return float(n1) + float(n2)


def subs(n1, n2):
    return float(n1) - float(n2)


def mult(n1, n2):
    return float(n1) * float(n2)


def divide(n1, n2):
    return float(n1) / float(n2)


def la_putere(n1, n2):
    return float(n1) ** float(n2)


PLUS = '+'
MINUS = '-'
IMPARTIT = '/'
INMULTIT = '*'
# PUTERE = '**'

data_dict = {
    PLUS: add,
    MINUS: subs,
    INMULTIT: mult,
    IMPARTIT: divide,
    # PUTERE: la_putere,
}

# user_input = input('Zii ecuatia: ')
# user_input = user_input.replace(" ", '')
#
# user_list = [item for item in user_input]
list_semne = [PLUS, MINUS, IMPARTIT, INMULTIT]
ran_num = random.randint(2, 10)
calculator_ecuatie = []
for _ in range(ran_num):
    numar = random.randint(1, 1000)
    calculator_ecuatie.append(numar)
    semn = random.choice(list_semne)
    calculator_ecuatie.append(semn)

calculator_ecuatie.pop(-1)
lista_proba = [str(item) for item in calculator_ecuatie]
string_proba = ''.join(lista_proba)
print(string_proba)
input('Apasa pt a continua')


def curatire(lista, indexul):
    indexul = indexul + 1
    for _ in range(3):
        lista.pop(indexul)
        indexul = indexul - 1

    return lista


def calculate(lista):
    while INMULTIT or IMPARTIT in lista:
        if INMULTIT not in lista and IMPARTIT not in lista:
            break
        for semnul in lista:
            if semnul == INMULTIT or semnul == IMPARTIT:
                if semnul == INMULTIT:
                    indexul = lista.index(INMULTIT)
                    ecuatia = data_dict[INMULTIT]
                    suma = ecuatia(lista[indexul - 1], lista[indexul + 1])
                    curatire(lista=lista, indexul=indexul)
                    lista.insert(indexul - 1, suma)
                    break

                elif semnul == IMPARTIT:
                    indexul = lista.index(IMPARTIT)
                    ecuatia = data_dict[IMPARTIT]
                    suma = ecuatia(lista[indexul - 1], lista[indexul + 1])
                    curatire(lista=lista, indexul=indexul)
                    lista.insert(indexul - 1, suma)
                    break
    while PLUS or MINUS in lista:
        if PLUS not in lista and MINUS not in lista:
            break
        if PLUS in lista:
            indexul = lista.index(PLUS)
            ecuatia = data_dict[PLUS]
            suma = ecuatia(lista[indexul - 1], lista[indexul + 1])
            curatire(lista=lista, indexul=indexul)
            lista.insert(indexul - 1, suma)

        if MINUS in lista:
            indexul = lista.index(MINUS)
            ecuatia = data_dict[MINUS]
            suma = ecuatia(lista[indexul - 1], lista[indexul + 1])
            curatire(lista=lista, indexul=indexul)
            lista.insert(indexul - 1, suma)

    return lista


rezultat = calculate(lista=calculator_ecuatie)
rezultat_str = str(rezultat[-1]).replace('[', '')
rezultat_str = rezultat_str.replace(']', '')
print(rezultat_str)
