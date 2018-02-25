def tuble_ex():
    t = input('Введіть цифри')
    if len(t) > 6:
      raise ValueError('Видаліть четверте число')
    return t
a,b,c,d,f,g = tuble_ex()
print(a,b,c,d,f,g)
print(type(tuble_ex()))