def add(*args):
    print(args)
    print(type(args))
    print(f"number of arguments: {len(args)}")
    sum_of_args = 0
    for n in args:
        sum_of_args += n
    return sum_of_args


print(add(1, 2, 3, 4, 5, 6))


def my_kwargs_function(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key)
        print(value)


my_kwargs_function(things="hello", stuff="kwargs!")


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    return n


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargzzz):
        # NOTE: using bracket notation on the Dict for a non-existent key
        #       will result in a runtime error. If you use the get() method
        #       instead, it will return None.
        # self.make = kwargzzz["make"]
        # self.make = kwargzzz["model"]
        self.make = kwargzzz.get("make")
        self.model = kwargzzz.get("model")


my_car = Car(make="Nissan")
print(f"make: {my_car.make} | model: {my_car.model}")
