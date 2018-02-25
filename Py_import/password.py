ALPHA = 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя'
def encode(text, step):
    return text.translate ( str.maketrans (ALPHA, ALPHA[step:] + ALPHA[:step]))
def decode (text, step):
    return text.translate ( str.maketrans (ALPHA[step:] + ALPHA[:step], ALPHA))


my_text = input('Ведіть текст для кодування ')
my_text2 = input('Ведіть текст для кодування 2 ')
print(encode(str(my_text), 2))
print(encode(str(my_text), 26))

print(decode(encode(str(my_text), 2), 2))
print(decode(encode(str(my_text), 26), 26))
