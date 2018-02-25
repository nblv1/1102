#my_sum = lambda a, b: a + b


#print (my_sum(1, 2))

def my_filter (element):
    return True if element > 0 else False


def filter_with_cnd(element, condition=0):
    return True if element > condition else False


def my_map(func, iters, *args, **kwargs):
    result = []
    for element in iters:
        result.append(func(element, *args, **kwargs))
    return result


print(my_map(my_filter, [2, 32, -1]))
print(my_map(filter_with_cnd, [2, 32], condition=20))