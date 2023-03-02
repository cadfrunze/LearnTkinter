# def adunare(n1, n2):
#     return n1 + n2
#
#
# def inmultire(n1, n2):
#     return n1 * n2
#
#
# def calculator(n, **kwargs):
#     kwargs['adunare'] = adunare(n1=n, n2=n)
#     kwargs['inmultire'] = inmultire(n1=n, n2=n)
#     if kwargs['adunare']:
#         print(kwargs['adunare'])
#     if kwargs['inmultire']:
#         print(kwargs['inmultire'])
#
#
# print(calculator(n=2, adunare=2))

class Car:

    def __init__(self, **kwargs):
        self.fabricant = kwargs.get('fabricant')
        self.model = kwargs.get('model')
        self.nr_locuri = kwargs.get('nr_locuri')
        self.culoare = kwargs.get('culoare')


masina_mea = Car(fabricant='Dacia', model='Logan')



