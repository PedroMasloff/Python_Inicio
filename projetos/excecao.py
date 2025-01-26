n1 = int(input('Digite um número: '))
n2 = int(input('Digite um segundo número: '))

try:
    r  = round(n1 / n2, 2)
except ZeroDivisionError:
    print('Não é possível')
else:
    print(f'Resultado: {r}')