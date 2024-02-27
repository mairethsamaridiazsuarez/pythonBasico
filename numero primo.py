n = int(input('ingresa un numero : '))
x = 1
b = 0
while x <= n:
    if n % x== 0 :
        b = b + 1
    x = x + 1
if b == 2 :
    print ('el numero ',n, 'es primo')
else :
    print ('el numero ', n, 'no es primo')
