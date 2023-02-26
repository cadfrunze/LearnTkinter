# def add(*args):
#     sum = 0
#     for n in args:
#         sum = sum + n
#     return sum


def calculate(n, **kwargs):
    print(f"{n}  + {kwargs['add']} = ", n + kwargs['add'])
    print(f"{n} * {kwargs['multiply']} = ", n * kwargs['multiply'])


calculate(n=2, add=5, multiply=4)


