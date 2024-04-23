import random


pokedex = []
pokeMato = ['Mewtwo', 'Rattata', 'Pidgey', 'Ekans']
pokeCaverna = ['Sandshrew', 'Zubat', 'Diglett']
escolha = 0
dado=0
tentativas = 0

print("Ola, eu sou o Professor Carvalho e serei seu guia para esta aventura Pokemon! Vamos começar com seu nome.")
nome = input("Digite seu nome: ")
print(f"Seja bem vindo {nome}! Vamos começar.\nNossa aventura será composta de várias escolhas, apenas digite o valor correspondente ou 0 para encerrar!")

while True:
    print("\n/////////\nVocê olha ao seu redor...\nEscolha:\n1 - Explorar a grama\n2 - Entrar na caverna\n3 - Ver Pokedex\n/////////")
    escolha = int(input("Digite sua escolha: "))
    while escolha < 0 or escolha > 3:
        escolha = int(input("Digite uma escolha listada ou 0 para encerrar: "))

    if escolha == 0:
        break

    if escolha == 1:
        print("Você está explorando a grama...")
        while True:
            dado = random.randint(1, 6)
            if dado in [1, 2]:
                pokemon = random.choice(pokeMato)
                print(f"Você encontrou um {pokemon} na grama!")
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
            else:
                print("Você não encontrou nenhum pokemon na grama. :C")

            continuar = input("Deseja continuar explorando a grama? (s/n): ")
            if continuar.lower() != 's':
                break

    elif escolha == 2:
        print("Você está explorando a caverna...")
        while True:
            dado = random.randint(1, 6)
            if dado in [1, 2]:
                pokemon = random.choice(pokeCaverna)
                print(f"Você encontrou um {pokemon} na caverna!")
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
            else:
                print("Você não encontrou nenhum pokemon na caverna. :C")

            continuar = input("Deseja continuar explorando a caverna? (s/n): ")
            if continuar.lower() != 's':
                break

    elif escolha == 3:
        print("/////////\nPokedex:")
        for pokemon in pokedex:
            print(pokemon)
        print('/////////')

print("Adeus e até a próxima!")