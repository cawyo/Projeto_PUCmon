import random
import time

def gerar_pokedex(pokedex):
    print("/////////\nPokedex:")
    for pokemon in pokedex:
        print(pokemon)
        print('/////////')
    time.sleep(2.5)

def gerar_menu():
    print("\n/////////\nVocê olha ao seu redor...\nEscolha:\n1 - Explorar a grama\n2 - Entrar na caverna\n3 - Ver Pokedex\n/////////")
    escolha = int(input("Digite sua escolha: "))
    while escolha < 0 or escolha > 3:
        escolha = int(input("Digite uma escolha listada ou 0 para encerrar: "))
    return escolha

def capturar_pokemon(lista_poke):
    pokemon = random.choice(lista_poke)
    print(f"Você encontrou um {pokemon}!")
    escolha_captura = input("Deseja tentar capturar o pokemon? (s/n): ")
    if escolha_captura.lower() == 's':
        tentativas = 0
        capturou = False
        while tentativas < 3:
            tentativas += 1
            captura = random.randint(1, 6)
            if captura == 1:
                print(f"Você capturou o {pokemon}!")
                pokedex.append(pokemon)
                capturou = True
                break
            else:
                print("A captura falhou.")
                escolha_nova_tentativa = input("Deseja tentar novamente? (s/n): ")
                if escolha_nova_tentativa.lower() != 's':
                    break
        if not capturou:
            print("O pokemon escapou!")

def explorar_area(area, lista_poke):
    print(f"Você está explorando a {area}...")
    time.sleep(1.5)
    while True:
        dado = random.randint(1, 6)
        if dado in [1, 2]:
            capturar_pokemon(lista_poke)
        else:
            print(f"Você não encontrou nenhum pokemon na {area}. :C")

        continuar = input(f"Deseja continuar explorando a {area}? (s/n): ")
        if continuar.lower() != 's':
            break
        time.sleep(1)

def escolher_pokeInicial():
    print("Escolha o seu Pokemon inicial:")
    for i, pokemon in enumerate(pokeIniciais, 1):
        print(f"{i} - {pokemon}")

    escolha = int(input("Digite o número correspondente ao Pokemon escolhido: "))
    while escolha < 1 or escolha > len(pokeIniciais):
        escolha = int(input("Por favor, escolha um número válido: "))

    pokemon_escolhido = pokeIniciais[escolha - 1]
    print(f"Você escolheu {pokemon_escolhido} como seu Pokemon inicial!")
    pokedex.append(pokemon_escolhido)
    time.sleep(1)

    

pokedex = []
pokeIniciais = ['Pikachu','Sprigatito','Litten','Oshawott']
pokeMato = ['Mewtwo', 'Rattata', 'Pidgey', 'Ekans']
pokeCaverna = ['Sandshrew', 'Zubat', 'Diglett']
dado=0
tentativas = 0

print("Olá, eu sou o Professor Carvalho e serei seu guia para esta aventura Pokemon! Vamos começar com seu nome.")
nome = input("Digite seu nome: ")
print(f"Seja bem vindo {nome}! Vamos começar.")
time.sleep(1)
print('Agora, vamos escolher seu primeiro parceiro Pokemon!')
escolher_pokeInicial()
print('Muito bem! Agora estamos pronto para começar! A partir de agora você será apresentado com algumas escolhas, digite o valor correspondente ou 0 para encerrar!')
time.sleep(3)

while True:
    time.sleep(1)
    escolha = gerar_menu()

    if escolha == 0:
        break

    if escolha == 1:
        explorar_area("grama", pokeMato)

    elif escolha == 2:
        explorar_area("caverna", pokeCaverna)

    elif escolha == 3:
        gerar_pokedex(pokedex)

print("Adeus e até a próxima!")