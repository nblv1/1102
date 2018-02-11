def spam():
    global eggs
    print(eggs)
    eggs = 'my_local_name'

eggs = 'global'
spam()
print(eggs)


