def file_writter(func):
    def wrapper(name):
        with open ('names.odt', 'a')  as fp:
            fp.write(name  + '\n')
        return func(name)
    return wrapper

@file_writter
def get_name(name):
    return f'My name is {name}'


print(get_name('Max'))
print(get_name('Joed'))
print(get_name('Alii'))
print(get_name('Ivan'))
print(get_name('Trina'))