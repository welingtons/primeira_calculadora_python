# Calculadora_Python
print ('\n', 'CALCULADORA PYTHON', '\n')

print ('1 - Soma')
print ('2 - Subtração')
print ('3 - Multiplicação')
print ('4 - Divisão','\n')

operação = input('Escolha a operação (1/2/3/4): ')
arg1 = int (input('Digite o primeiro valor: '))
arg2 = int (input('Digite o segundo valor: '))
if operação =='1':
    print (arg1, '+', arg2, '=', arg1 + arg2)
elif operação =='2':
    print (arg1, '-', arg2, '=', arg1 - arg2)
elif operação =='3':
    print (arg1, 'x', arg2, '=', arg1 * arg2)
else:
    print (arg1, ':', arg2, '=', arg1 / arg2)