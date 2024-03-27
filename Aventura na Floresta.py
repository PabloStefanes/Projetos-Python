from time import sleep
from random import randint

# Apresentação inicial
print('Você está partindo em uma aventura na floresta.')
sleep(1)

# Lista para armazenar os itens
itens = []

# Solicitar ao usuário a quantidade de itens
while True:
    try:
        quantidade = int(input("Quantos equipamentos você deseja adicionar? "))
        if quantidade <= 0:
            print("Por favor, digite um número maior que zero.")
        else:
            break
    except ValueError:
        print("Por favor, digite um número válido.")

# Solicitar os itens ao usuário
for i in range(quantidade):
    while True:
        equipamento = input(f'Digite o {i+1}º equipamento de {quantidade}: ')
        if equipamento.isalpha():
            itens.append(equipamento)
            break
        else:
            print('Digite apenas letras!')

# Exibir a lista de itens
if itens:
    print("Lista de itens:")
    for item in itens:
        print(f"- {item}")
else:
    print("Nenhum equipamento foi adicionado.")
sleep(1)

# Início da aventura na floresta
print('Agora você entrou na floresta, mas está perdido.')
sleep(1)
print('Descubra quantos passos (1 a 10) precisar dar para sair.')

# Gerar um número aleatório de passos necessários para sair
passos = randint(1, 10)

# Solicitar ao usuário a estimativa de passos
quantidade_passos = int(input('Quantos passos você quer dar? '))

# Verificar se a estimativa está correta
while quantidade_passos != passos:
    # Informar se é mais ou menos
    if quantidade_passos > passos:
        print('É menos!')
    else:
        print('É mais!')
    print('GAME OVER! Tente novamente')
    quantidade_passos = int(input('Quantos passos você quer dar? '))

# Se acertou a estimativa, parabenizar
print('PARABÉNS! Você saiu da floresta e poderá continuar a aventura.')
