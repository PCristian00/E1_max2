def my_max(a, b):
    print(str(a)+' ? '+str(b))
    if a == b:
        print('I numeri sono identici')
        print(str(a) + ' == ' + str(b))
    elif a > b:
        print('Il numero più grande tra i due è ' + str(a))
        print(str(a)+' > '+str(b))
    else:
        print('Il numero più grande tra i due è ' + str(b))
        print(str(b) + ' > ' + str(a))


x = input('Inserire primo numero: ')
y = input('Inserire secondo numero: ')
my_max(x, y)
