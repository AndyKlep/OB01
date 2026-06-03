# Разработай систему управления учетными записями пользователей для небольшой компании. Компания разделяет сотрудников на обычных работников и администраторов. У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа. Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут добавлять или удалять пользователя из системы.
# # Требования:
# # 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа ('user' для обычных сотрудников).
# # 2.Класс Admin: Этот класс должен наследоваться от класса User. Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin'). Класс должен также содержать методы add_user и remove_user, которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров User).
# # 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи. Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).

class User():
    _last_id = 0
    def __init__(self, name, user_list):
        self.name = name
        User._last_id += 1
        self.__id = User._last_id
        self._seclvl = "user"
        self.user_list = user_list
        self.user_list.append(self)

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def full_name(self):
        print(f"{self.__id} {self.name} {self.get_seclvl()}")

    def get_seclvl(self):
        return self._seclvl

    def set_seclvl(self, seclvl):
        self._seclvl = seclvl

    def __repr__(self):
        return f"User({self.name}, {self._seclvl})"



class Admin(User):
    def __init__(self, name, user_list):
        super().__init__(name, user_list)
        self._seclvl = "admin"


    def add_user(self, name, user_list):
        User(name, user_list)
        print(f'Пользователь с именем {name} добавлен.')


    def del_user(self, user_list, id):
        for user in user_list:
            if user.get_id() == id:
                if user.get_seclvl() == "admin":
                    print(f"У вас нет прав на удаление администратора {user.name}.")
                else:
                    user_list.remove(user)
                    print(f'Администратор {self.name} удалил пользователя {user.name}.')

    def lowing_user(self, user_list, id):
        for user in user_list:
            if user.get_id() == id:
                if user.get_seclvl() == "admin":
                    user.to_user()
                    user_list.remove(user)
                    print(f"Админ {self.name} понизил в правах собрата {user.name} (ну по крайней мере в рамках списка).")
                    break
                else:
                    print(f'Пользователь {user.name} и так не имеет прав администратора.')

    def to_user(self):
        tmp_id = User._last_id
        not_admin = User(self.name, self.user_list)
        not_admin.set_id(self.get_id())
        User._last_id = tmp_id


def all_list_info(user_list):
    user_list.sort(key=lambda x: x.get_id())
    for user in user_list:
        user.full_name()
    print('____________________')

users_list1 = []

u1 = User('Ivan', users_list1)
u2 = User('Anotole', users_list1)
u3 = User('Anya', users_list1)
a1 = Admin("Kolya", users_list1)
a2 = Admin('Vova', users_list1)

#Вывод начальной информации
print(users_list1)
all_list_info(users_list1)

#Добавление пользователя
a1.add_user("Nina", users_list1)
all_list_info(users_list1)

#Удаление пользователя
a2.del_user(users_list1, 3)
a2.del_user(users_list1, a1.get_id())
all_list_info(users_list1)

#Изменение статуса пользователя (правда это не изменит прав a2)
a1.lowing_user(users_list1, u1.get_id())
a1.lowing_user(users_list1, a2.get_id())
a2.add_user("Roma", users_list1)
all_list_info(users_list1)
print(a2)