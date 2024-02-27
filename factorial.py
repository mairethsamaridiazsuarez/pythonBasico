print ('escribe un numero')
num = int(input())
fact = 1
for i in range (1,num+1) :
    fact*=i
print ('El resultado de la factorial del numrero ' , num ,'es : ', fact)