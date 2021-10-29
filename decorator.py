def sub(a,b):
    print(a-b)
sub(6,10)
def smart_sub(func):
    def inner(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)
    return inner
sub= smart_sub(sub)
sub(6,10)
