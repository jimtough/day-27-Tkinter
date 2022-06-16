def add(*args):
    print(args)
    print(type(args))
    print(f"number of arguments: {len(args)}")
    sum_of_args = 0
    for n in args:
        sum_of_args += n
    return sum_of_args


print(add(1, 2, 3, 4, 5, 6))
