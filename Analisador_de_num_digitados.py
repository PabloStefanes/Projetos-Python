# Este programa analisa os dados dos números digitados pelo usuário.
def obter_num():
    # Função para obter os números digitados pelo usuário.
    return tuple(int(input(f'Digite {i+1}º de 4 valores: ')) for i in range(4))

def encontrar_indices(tupla, valor):
    # Função para analisar todos os índices de um determinado número.
    return tuple(i for i in range(len(tupla)) if tupla[i] == valor)

def analisar_num():
    # Função para analisar os números digitados pelo usuário.
    num = obter_num()

    # Imprime os números analisados sem colchetes e parênteses.
    print(f'Os números digitados foram:', end=' ')
    print(*num, sep=', ')

    # Analisa se o número 9 foi digitado. Caso sim, a quantidade de vezes.
    if 9 not in num:
        print('O número 9 não foi digitado.')
    else:
        print(f'Quantidade de números 9: {num.count(9)}')

    # Analisa se o número 3 foi digitado. Caso sim, retorna seu índice.
    if 3 not in num:
        print('O número 3 não foi digitado.')
    else:
        indices_3 = encontrar_indices(num, 3)
        print('índices do número 3:', end=' ')
        print(*indices_3, sep=', ')

    # Analisa os números pares digitados pelo usuário.
    pares = [n for n in num if n % 2 == 0]
    if not pares:
        print('Não foram digitados números pares.')
    else:
        print('Números pares digitados:', end=' ')
        print(*pares, sep=', ')

# Chamando a função para analisar os dados.
analisar_num()
