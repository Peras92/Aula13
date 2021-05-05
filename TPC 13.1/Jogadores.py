import json


class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds


class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


lebron = BasketballPlayer(first_name="Lebron", last_name="James", height_cm=203, weight_kg=113, points=27.2,
                          rebounds=7.4, assists=7.2)

kev_dur = BasketballPlayer(first_name="Kevin", last_name="Durant", height_cm=210, weight_kg=108, points=27.2,
                           rebounds=7.1, assists=4)


# football
ronaldo = FootballPlayer(first_name="Cristiano", last_name="Ronaldo", height_cm=184, weight_kg=79, goals=586,
                         yellow_cards=95, red_cards=11)

messi = FootballPlayer(first_name="Lionel", last_name="Messi", height_cm=170, weight_kg=67, goals=575,
                       yellow_cards=67, red_cards=0)


escolha = input("Bem vindo ao catalogo de jogadores" + "\n" + "Pretendes adicionar jogares de Basketball (B) ou Football (F)? ")

if escolha.upper() == "F":
    primeiro_nome = input("Primeiro nome do jogador? ")
    ultimo_nome = input("Ultimo nome do jogador? ")
    altura = input("Altura do jogador (em cm)? ")
    peso = input("Peso do jogador (em kg)? ")
    golos = input("Numero de golos do jogador? ")
    amarelo = input("Número de cartões amarelos do jogador? ")
    vermelho = input("Número de cartões vermelhos do jogador? ")

    novo_jogador = FootballPlayer(first_name=primeiro_nome, last_name=ultimo_nome, height_cm=altura, weight_kg=peso, goals=golos, yellow_cards=amarelo, red_cards=vermelho)

    with open("football.json", "r") as lista_football:
        lista_football = json.loads(lista_football.read())

    lista_football.append(novo_jogador.__dict__)

    with open('football.json', 'w') as json_file:
        json.dump(lista_football, json_file)

    print("Jogador adicionado com sucesso." + "/n" + "Esta é a nossa base de dados completa:")
    for i in lista_football:
        print(i)

elif escolha.upper() == "B":
    primeiro_nome = input("Primeiro nome do jogador? ")
    ultimo_nome = input("Ultimo nome do jogador? ")
    altura = input("Altura do jogador (em cm)? ")
    peso = input("Peso do jogador (em kg)? ")
    pontos = input("Média de pontos do jogador? ")
    ressalto = input("Número de ressaltos do jogador? ")
    assistencias = input("Número de assistencias do jogador? ")

    novo_jogador = BasketballPlayer(first_name=primeiro_nome, last_name=ultimo_nome, height_cm=altura, weight_kg=peso, points=pontos, rebounds=ressalto, assists=assistencias)


    with open("basket.json", "r") as lista_basket:
        lista_basket = json.loads(lista_basket.read())

    lista_basket.append(novo_jogador.__dict__)

    with open('basket.json', 'w') as json_file:
        json.dump(lista_basket, json_file)

    print("Jogador adicionado com sucesso." + "/n" + "Esta é a nossa base de dados completa:")
    for i in lista_basket:
        print(i)

else:
    print("Por favor escolhe uma das opções permitidas")
