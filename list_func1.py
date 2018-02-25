list1 = list(x for x in range(10))
list2 = list(x for x in range(0, 9, 2))
list3 = []
list4 = [10, 10, 2, 7, 4, 8, 8]

#def inter(ls1, ls2):
 #   return set(ls1) & set(ls2)#для знаходження спільних еклентів у set

#print(inter(list4, list2))


def make_print(my_var): #використання key words
    print(my_var)
    if my_var == 4:
        return
    return my_var * my_var

make_print(my_var=8)


