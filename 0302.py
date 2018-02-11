import random
import string


l = [string.ascii_uppercase, string.ascii_lowercase, string.digits]
my_pass_len = input('Довжина пароля')
codes = string.ascii_uppercase + string.ascii_lowercase + string.digits
password = random.sample(codes, int(my_pass_len))#генерує пароль з кількістю заданих рядків
print(''.join(password))