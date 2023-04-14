def swapl():
    l = [8, 11, 12, 86]
    first = l.pop(0)
    last = l.pop(-1)
    l.insert(0,last)
    l.append(first)
    return l
print(swapl())