# Funções 
# Modularização, Reúso de Código, Legibilidade

# def <nome_da_função> ([argumentos]):
#     <instruções>

# def mensagem():
#     print('Teste')
#     print('Outro teste')
# mensagem()

#Função com argumentos

# def soma(a,b):
#     print(a+b)
# soma(12,7)

# def mult(x,y):
#     return x * y
# a = 5
# b = 8
# c = mult(a,b)
# print(f'O produto de {a} e {b} é {c}')

def div(k,j):
    if j != 0:
        return k / j
    else:
        return 'Impossível'

if __name__ == '__main__':
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    r = div(a,b)
    print(f'{a} dividido por {b} é igual a {r}')