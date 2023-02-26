# num1 = [1, 2, 3]
# num2 = [1, 3, 2]
#
# x = num1 + num2
# print(x)
#
# while 2 in x:
#     x.remove(2)
#
# print(x)

def add(*args):
    sum = 0
    for n in args:
        sum = sum + n
    return sum



print(add(1, 1, 1))
