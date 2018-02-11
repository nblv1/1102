


my_lits = []
for num in range(1500, 2701):
    if not  num % 7 and not num % 5:
        my_lits.append(num)

print(my_lits)


loop_mumber = 5  #перша задача
star = '*'
for i in range(loop_mumber):
    for j in range(i):
        print(star, end='')
    print()
