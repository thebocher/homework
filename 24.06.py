print('-' * 10, 1, '-' * 10)
def dec1(func):
    def inner(*args, **kwargs):
        if not args[0]:
            return float('nan')
        else:
            return func(*args, **kwargs)
    return inner
@dec1
def func9(a, b):
    return b / a
f = func9(0, 10)
print(f)

print('-' * 10, 2, '-' * 10)
def dec2(func):
    def inner(*args, **kwargs):
        print(locals())
        return func(*args, **kwargs)
    return inner
@dec2
def func_for_2(a, b, *c):
    return "func_for_2 called"
print(func_for_2(1, 2, 2, 3, 4, 5, 5, 6))

print('-' * 10, 4, '-' * 10)
def b(func):
    def inner(*a, **kw):
        return f'<b>{func(*a, **kw)}</b>'
    return inner

def i(func):
    def inner(*a, **kw):
        return f'<i>{func(*a, **kw)}</i>'
    return inner

def u(func):
    def inner(*a, **kw):
        return f'<u>{func(*a, **kw)}</u>'
    return inner
@b
@i
@u
def func_for_4(a):
    return a
print(func_for_4('text'))

print('-' * 10, 5, '-' * 10)
def dec5(func):
    if not callable(func):
        arg = func
        def outer(func):
            def inner(*a, **kw):
                return f'{func(*a, **kw)}, arg = {arg}'
            return inner
        return outer
    else:
        arg = None
        def inner(*a, **kw):
            return f'{func(*a, **kw)}, arg = {arg}'
        return inner

@dec5(123)
def func_for_5(b):
    return b
print(func_for_5('func5'))
