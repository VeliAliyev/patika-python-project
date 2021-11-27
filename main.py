def flatten(a):
    flat = []
    for x in a:
        if isinstance(x, list):
            flat.extend(flatten(x))
        else:
            flat.append(x)
    return flat


def my_reverse(a):
    a.reverse()
    for x in a:
        if isinstance(x, list):
            x.reverse()
    return a


a = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
b = flatten(a)
print(b)

a = [[1, 2], [3, 4], [5, 6, 7]]
print(a)
b = my_reverse(a)
print(b)
