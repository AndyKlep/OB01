# Задача: Разработать простую игру, где игрок может использовать различные типы оружия для борьбы с монстрами. Программа должна быть спроектирована таким образом, чтобы легко можно было добавлять новые типы оружия, не изменяя существующий код бойцов или механизм боя.
from abc import ABC, abstractmethod

class WeaponAbs(ABC):
    def __init__(self, name, stamina, damage, type_of_hit):
        self.name = name
        self.stamina = stamina
        self.damage = damage
        self.type_of_hit = type_of_hit

    @abstractmethod
    def attack(self, target):
        pass

    def check_stamina(self):
        if self.stamina <= 0:
            print(f"{self.name} сломался.")
            self.name = 'Сломанный ' + self.name
            self.damage = 0

    def __repr__(self):
        return f'{self.name} может наносить {self.damage} {self.type_of_hit} урона. Прочность: {self.stamina}.'

class Sword(WeaponAbs):
    def __init__(self, name, stamina, damage):
        super().__init__(name, stamina, damage, 'рубящего')

    def attack(self, target: EnemyAbs):
        self.stamina = self.stamina - target.solid
        if self.damage <= target.defense:
            print('Броня крепка, урон не прошел.')
        else:
            target.hp  = target.hp - self.damage + target.defense
            print(f"{self.name} нанес {self.damage} {self.type_of_hit} урона {target.name}.")
        print(f'У {self.name} осталось {self.stamina} прочности.')


class Bow(WeaponAbs):
    def __init__(self, name, stamina, damage):
        super().__init__(name, stamina, damage, 'колющего')

    def attack(self, target: EnemyAbs):
        self.stamina = self.stamina - 1
        if self.damage <= target.defense:
            print('Броня крепка, урон не прошел.')
        else:
            target.hp  = target.hp - self.damage + target.defense
            print(f"Выстрел из {self.name} нанес {self.damage} {self.type_of_hit} урона {target.name}.")
        print(f'У {self.name} осталось {self.stamina} прочности.')

class EnemyAbs():
    def __init__(self, name, hp, solid, defense):
        self.name = name
        self.hp = hp
        self.solid = solid
        self.defense = defense

    def get_hp(self):
        print(f"У {self.name} {self.hp} единиц здоровья.")

    def is_dead(self):
        if self.hp <= 0:
            return True

    def __repr__(self):
        return f'{self.name}, {self.hp} здоровья, {self.defense} брони, {self.solid} жесткости.'

class OrcEnemy(EnemyAbs):
    def __init__(self, name, hp):
        super().__init__(name, hp, 2, 4)
        # self.defense = 4
        # self.solid = 2

class SlimeEnemy(EnemyAbs):
    def __init__(self, name, hp):
        super().__init__(name, hp, 0, 1)
        # self.defense = 1
        # self.solid = 0

class Fighter():
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def get_the_weapon(self, weapon: WeaponAbs):
        if self.weapon == None:
            self.weapon = weapon
            print(f'Герой {self.name} взял {self.weapon.name}.')
        else:
            self.drop_the_weapon()
            self.get_the_weapon(weapon)

    def drop_the_weapon(self):
        if self.weapon == None:
            pass
        else:
            print(f'Герой отложил в сторону {self.weapon.name}')
            self.weapon = None

    def attack(self, target):
        if self.weapon == None:
            print('У вас нет оружия, чтобы атаковать.')
        else:
            self.weapon.attack(target)
            self.weapon.check_stamina()
            if target.is_dead():
                print(f"{target.name} повержен.")
            else:
                target.get_hp()

ivan = Fighter('Ivan')
sword1 = Sword('Простой меч', 10, 4)
sword2 = Sword('Длинный меч', 20, 5)
bow1 = Bow('Короткий лук', 7, 2)
bow2 = Bow("Длинный лук", 20, 5)

orc1 = OrcEnemy('Lilo', 15)
orc2 = OrcEnemy('Stich', 50)
slime1 = SlimeEnemy('Poring', 6)
slime2 = SlimeEnemy('Poporing', 20)

weaponlist = [sword1, sword2, bow1, bow2]
enemylist = [orc1, orc2, slime1, slime2]

while True:
    choose = input('Выберете действие:\n'
          '1. Взять оружие\n'
          '2. Биться с монстром.\n'
            '3. Информация об экипированном оружии.\n'
            '0. Выход.\n')
    if choose == '0':
        break
    elif choose == '1':
        print('Список доступного оружия:')
        for i, weapon in enumerate(weaponlist, start=1):
            print(f'{i}. {weapon.name}')
        weapon_of_choise = input("Выберите номер оружия\n")
        ivan.get_the_weapon(weaponlist[int(weapon_of_choise)-1])
    elif choose == '2':
        print('Список монстров:')
        for i, enemy in enumerate(enemylist, start=1):
            print(f"{i}.", enemy)
        target_of_choise = input('Кого бить?\n')
        ivan.attack(enemylist[int(target_of_choise)-1])
    elif choose == '3':
        print(ivan.weapon)




