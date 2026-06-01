#Ты разрабатываешь программное обеспечение для сети магазинов. Каждый магазин в этой сети имеет свои особенности, но также существуют общие характеристики, такие как адрес, название и ассортимент товаров. Ваша задача — создать класс Store, который можно будет использовать для создания различных магазинов.

class Store():
    def __init__(self, name, address, items):
        self.name: str = name
        self.address: str = address
        self.items: dict[str, float] = items

    def add_item(self):
        tov_type, tov_price = input('Для добавления товара или изменения цены введите его название и цену\n').split()
        if tov_type in self.items and tov_price == self.items[tov_type]:
            print(f'Такая позиция уже есть в магазине {self.name}')
        elif tov_type in self.items:
            self.items[tov_type] = tov_price
            print(f'Цена товара {tov_type} была изменена.')
        else:
            self.items[tov_type] = tov_price
            print(f'Товар {tov_type} добавлен в магазин {self.name}')

    def list_items(self):
        if len(self.items) == 0:
            print('Нет товаров в этом магазине.')
        else:
            print(f'Список товаров в магазине {self.name}:')
            for i, (key, value) in enumerate(self.items.items(), start=1):
                print(f'{i}.{key}: {value}')

    def info_store(self):
        print(f'Это магазин {self.name} по адресу {self.address}. В нем продается {len(self.items)} наименований товаров.')

    def del_item(self):
        choice = input('Выберите товар для удаления\n')
        if choice in self.items:
            del self.items[choice]
            print('Товар был удален')
        else:
            print('Нет такого товара в списке')

    def which_price(self):
        tov = input('Цену какого товара вы хотите узнать?\n')
        if tov in self.items:
            print(f'Цена {tov} составляет {self.items[tov]}')
        else:
            print('Нет такого товара в списке')
            return None

mag1 = Store('Mega', "Белая Дача", {"мангал": 1500, "шампуры": 300, "Сковорода": 777})
mag2 = Store('Ikea', "Newerland, st. 27", {"Bed": 2000, "Table": 1674, "Chair": 890})
mag3 = Store('M-Video', "ulitsa Lenina 2", {"TV": 3000, "Computer": 4000, "Fridze": 3300})

store_list = [mag1, mag2, mag3]

while True:
    print("1. Посмотреть список магазинов.")
    print("2. Выбрать магазин.")
    print('3. Создать новый магазин.')
    print('4. Удалить магазин из списка.')
    print("0. Выход")
    choice = input("Выберите действие: ")
    if choice == "1":
        for i, store in enumerate(store_list, start=1):
            print(f'\t{i}.{store.name}')
    elif choice == "2":
        mag = input("Напишите название магазина\n")
        for store in store_list:
            if mag == store.name:
                while True:
                    store.info_store()
                    print('\t1. Посмотреть список товаров.')
                    print('\t2. Добавить товар или изменить цену.')
                    print("\t3. Удалить товар.")
                    print("\t4. Запросить цену товара.")
                    print("\t0. Вернуться к выбору магазинов.")
                    chochoice = input("Выберите действие в магазина: ")
                    if chochoice == "1":
                        store.list_items()
                    elif chochoice == "2":
                        store.add_item()
                    elif chochoice == "3":
                        store.del_item()
                    elif chochoice == "4":
                        store.which_price()
                    elif chochoice == "0":
                        break
                    else:
                        print('Неверная команда.')
    elif choice == "3":
        mag_name = input('Введите название магазина\n')
        mag_adr = input('Введите адрес магазина\n')
        store_list.append(Store(mag_name, mag_adr, {}))
        print(f'Магазин {mag_name} по адресу {mag_adr} добавлен.')
    elif choice == "4":
        mag = input("Напишите название магазина, который нужно удалить из списка\n")
        for store in store_list:
            if mag == store.name:
                store_list.remove(store)
    elif choice == "0":
        break
    else:
        print('Неверная команда')

