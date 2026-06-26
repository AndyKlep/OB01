import random

class Hero():
    def __init__(self, name, health=100, power_attack=20):
        self.name = name
        self.health = health
        self.power_attack = power_attack

    def attack(self, other: Hero):
        other.health -= self.power_attack
        print(f"Нанесен удар на {self.power_attack}, у {other.name} осталось {other.health}.")

    def is_alive(self):
        return self.health > 0

class Game():
    def __init__(self, player: Hero, computer: Hero):
        self.player = player
        self.computer = computer

    def only_one_winner(self, winner: Hero, looser: Hero):
        print(f"{looser.name} повержен, {winner.name} победил.")

    def start(self):
        print(f"Игра началась.")
        round_number = 0
        while True:
            round_number += 1
            print(f"Раунд {round_number}")
            computer_target = random.randint(1, 2)
            computer_def = random.randint(1, 2)
            player_target = input(f"Выберите куда бить: 1 - для удара поверху, 2 - для удара по низу\n")
            player_def = input(f"Выберите что защищать: 1 - верх, 2 - низ\n")

            #Блок атаки игрока
            if player_target == computer_def:
                print(f"{self.player.name} нанес удар, но {self.computer.name} отразил удар.")
            elif player_target != computer_def and player_target in range(1, 2):
                self.player.attack(self.computer)
            else:
                print(f"{self.player.name} бьет мимо противника.")

            #Блок атаки компьютера
            if computer_target == player_def:
                print(f"{self.player.name} защитился от удара {self.computer.name}.")
            elif computer_target != player_def and player_def in range(1, 2):
                self.computer.attack(self.player)
            else:
                print(f"{self.player.name} даже не поднял щит.")
                self.computer.attack(self.player)

            #Проверка состояния здоровья
            if not self.player.is_alive() and not self.computer.is_alive():
                print(f"{self.player.name} и {self.computer.name} одновременно поразили друг друга и погибли. Победителя нет.")
            elif not self.player.is_alive():
                self.only_one_winner(self.player, self.computer)
                break
            elif not self.computer.is_alive():
                self.only_one_winner(self.computer, self.player)
                break
            else:
                continue


