def add(*args):
    print(args[1])
    res = 0
    for n in args:
        res += n
    return res

print(add(1,2,3,4))

print(add(1,2,3,4))
def calculate(n, **kwargs):
    print(kwargs)
    for key,val in kwargs.items():
        print(key, val)

    print(kwargs['add'])
    n += kwargs['add']
    n *= kwargs['mul']
    print(n)


calculate(4,add=3, mul=5)

class Car:

    def __init__(self, **kw):

        # self.make = kw['make']
        # self.model = kw['model']

        self.make = kw.get('make')
        self.model = kw.get('model')
        self.colour = kw.get('colour')
        self.seats = kw.get('seat')


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
