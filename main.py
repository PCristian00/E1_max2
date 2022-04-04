def my_max(a, b):
    print(' a ' + str(a) + ' b ' + str(b))
    if a == b:
        print('I numeri sono identici')
        print(str(a) + ' == ' + str(b))
    elif a > b:
        print('Il numero più grande tra i due è ' + str(a))
        print(str(a) + ' > ' + str(b))
    else:
        print('Il numero più grande tra i due è ' + str(b))
        print(str(b) + ' > ' + str(a))


x = int(input('Inserire primo numero: '))
y = int(input('Inserire secondo numero: '))
my_max(x, y)
print('Usando max')
print(max(x, y))
