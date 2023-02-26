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
PUTERE = '**'

data_dict = {
    PLUS: add,
    MINUS: subs,
    INMULTIT: mult,
    IMPARTIT: divide,
    PUTERE: la_putere,
}

user_input = input('Zii ecuatia: ')
user_input = user_input.replace(" ", '')

user_list = [item for item in user_input]


# user_list1 = [int(num) for num in user_input if num != '+' or num != '-' or num != '/' or num != '*' or num != '**']


def curatire(lista, indexul):
    indexul = indexul + 1
    for _ in range(3):
        lista.pop(indexul)
        indexul = indexul - 1

    return lista


def calculate(lista):
    while INMULTIT or IMPARTIT in lista:
        if INMULTIT and IMPARTIT not in lista:
            break
        if INMULTIT in lista:
            indexul = lista.index(INMULTIT)
            ecuatia = data_dict[INMULTIT]
            suma = ecuatia(lista[indexul - 1], lista[indexul + 1])
            curatire(lista=lista, indexul=indexul)
            lista.insert(indexul - 1, suma)

        if IMPARTIT in lista:
            indexul = lista.index(IMPARTIT)
            ecuatia = data_dict[IMPARTIT]
            suma = ecuatia(lista[indexul - 1], lista[indexul + 1])
            curatire(lista=lista, indexul=indexul)
            lista.insert(indexul - 1, suma)

    while PLUS or MINUS in lista:
        if PLUS and MINUS not in lista:
            print(PLUS in lista)
            print(MINUS in lista)
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


print(calculate(lista=user_list))
# print(sum(user_list1))
