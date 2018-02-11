y = 0
while y < 4: #доки y менше за 4
    print ('*' * (y+1)) #то друкуй Y+1 зірочок
    y += 1 # кроком y + 1
x = 5
while x > 0:
    print ('*' * x)
    x -= 1


a = list(range(1500, 2701, 1))
for num in a:
    if num % 7 == 0:
        print(num)#виведе число, що ділится на 7 і помножене на 5



#for i in range(10, 0, -1):
#        if i == 1:
#               print('1 , 1 bottle of beer!')
#                print('So take it down, pass it around, no more bottles of beer on the wall!')
#       elif i == 2:
#               print('2 more bottles of beer on the wall, 2 more bottles of beer!')
#                print('So take one down, pass it around, 1 more bottle of beer on the wall!')
#        else:
#               print('{0} bottles of beer on the wall, {0} bottles of beer!'.format(i))
#                print('So take it down, pass it around, {0} more bottles of beer on the wall!'.format(i - 1))