import string

l = [string.ascii_uppercase, string.ascii_lowercase, string.digits]
print(l)
# my_list = list(string.ascii_uppercase)
# print(my_list)
# my_list_length = len(my_list)
# for inx in range (my_list_length):
#   if n % 2 == 0:


list_new = ['mfmfmf', 'dndndnd', 'djdjdj', 7, 88, 8, 8.1]
for element in list_new:
    if isinstance(element, int):  # якщо елемети списку є int
     print(element)

a_list = [1, 'a', None, 'ice', bool]
a_list_lenght = len(a_list)
for inx in range(a_list_lenght):
    if not isinstance(a_list_lenght, str): #якщо не  str
        a_list[inx] = str(a_list[inx])  #перетворити елементи a_list у str
print(a_list)

digit_list = [1, 9, 10, 10, 90, 1000]
for numb in digit_list:  # з номерів списку
    if numb % 2 == 0:  # для номера, який ділиться на 2
       print(numb)
