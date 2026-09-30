def if_number(fun):
    def wrapper(*args):
        for num in args:
            if not isinstance(num, (int, float, bool)):
                raise ValueError("Only numbers can be parameters")
        return fun(*args)
    return wrapper


@if_number
def checker(p1, p2):
    return p1 + p2


checker(1, 90)