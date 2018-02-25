def p_decorate(name):
    print('Name is', name)
    return p_decorate

@p_decorate
def my_file(file):
    with open('my_test_file', 'r+') as fp:
        print(fp.read())
    return my_file



p_decorate('Ivan')
p_decorate('Katya')
p_decorate('Dina')

