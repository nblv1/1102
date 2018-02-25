#print([x for x in range(1,6) if x % 2 == 1])

#print(list(filter(lambda x: x % 2 , range(1, 6))))


mylist = ['coffee', 'milk', 'latte']
mylist2 = ['water', 'hot', 'tap']
mylist3 = ['food', 'borsch', 'caviar']

result = []
for a in mylist:
    for b in mylist2:
        for c in mylist3:
             result.append((a, b, c))

print(result)


a = list(enumerate(['coffee', 'milk', 'latte']))
print(a)

for j, fg in enumerate(['coffee', 'milk', 'latte']):
    print(j, fg)





