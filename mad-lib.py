from time import sleep

def validar_letras(palavra):
    return palavra.isalpha()

def entrada_com_validacao(mensagem):
    while True:
        palavra = input(mensagem).upper()
        if validar_letras(palavra):
            return palavra
        else:
            print('\33[41m\33[97mPor favor, insira apenas letras!!!\33[m')

print('Aqui está um Mad Lib para você:')
sleep(1)  # Gera um temporizador de 1s para que a linha de baixo apareça
print('\33[7mTítulo: Uma Viagem Inesquecível\33[m')  # o código faz uma cor de fundo branca no texto
sleep(1)

substantivo_plural = entrada_com_validacao('Escreva um substantivo (plural): ')
nome_de_lugar = entrada_com_validacao('Escreva o nome de um lugar: ').upper()
verbo_passado = entrada_com_validacao('Escreva um verbo no passado: ')
adjetivo = entrada_com_validacao('Escreva um adjetivo: ')
nome_proprio = entrada_com_validacao('Escreva um nome próprio: ')
verbo_gerundio = entrada_com_validacao('Escreva um verbo no gerúndio: ')
substantivo = entrada_com_validacao('Escreva um substantivo: ')
adjetivo2 = entrada_com_validacao('Escreva um adjetivo: ')
verbo_infinitivo = entrada_com_validacao('Escreva um verbo no infinitivo: ')
nome_de_lugar2 = entrada_com_validacao('Escreva o nome de um lugar: ')

print(f'No verão passado, eu e meus {substantivo_plural} decidimos fazer uma viagem para {nome_de_lugar}.\n '
      f'Quando chegamos lá, nós {verbo_passado} em um hotel muito {adjetivo} chamado {nome_proprio}.\n '
      f'O tempo estava tão bom que passamos a maior parte do tempo {verbo_gerundio} na praia,\n '
      f'aproveitando o sol e o mar {substantivo}. À noite, nós saíamos para jantar em restaurantes {adjetivo2}\n '
      f'e depois {verbo_infinitivo} pela cidade. Foi uma viagem {nome_de_lugar2} que sempre lembraremos com carinho.')

