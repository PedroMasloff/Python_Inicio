#Escopo global e local

var_global = "Curso completo de python"

def escreve_texto():
    var_local = 'Pedro'
    print(f'Variável Global: {var_global}')
    print(f'Variável Local: {var_local}')


if __name__ == '__main__':
    print(f'Executar a funcao escreve texto()')
    escreve_texto()

    print('tentar acessar diretamente')
    # print(f'Variável Global: {var_global}')
    # print(f'Variável Local: {var_local}')