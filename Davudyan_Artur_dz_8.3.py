from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'{func.__name__}(', end='')

        res_args = []
        for arg in args:
            res_args.append(f'{str(arg)}: {type(arg)}')
        if kwargs:
            print(', '.join(res_args), end=', ')
        else:
            print(', '.join(res_args), end=')')

        res_kwargs = []
        for key, value in kwargs.items():
            res_kwargs.append(f'{str(key)}: {type(key)}, {str(value)}: {type(value)}')
        print(', '.join(res_kwargs), end=')\n')

        return func(*args, **kwargs)

    return wrapper


@type_logger
def calc_cube(x, **kwargs):
    return x ** 3


a = calc_cube(5, h=7)
print(a)
