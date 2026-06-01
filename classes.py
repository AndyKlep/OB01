#Задача: Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task():
    def __init__(self, name, description, limit, done):
        self.name = name
        self.description = description
        self.limit = limit
        self.done = done

    def mark_done(self):
        self.done = True

    def all_info(self):
        status = "выполнено" if self.done else "не выполнено"
        print(f"Вот полная информация о задаче {self.name}:\nОписание: {self.description}\nСрок выполнения:{self.limit}\nЗавершена: {status}")

def add_task(t_list):
    name = input("Введите имя задачи:\n")
    description = input("Введите описание задачи:\n")
    limit = input("Введите срок выполнения задачи:\n")
    t_list.append(Task(name, description, limit, False))
    print(f"Задача {name} добавлена")

def show_all_tasks(t_list):
    if len(t_list) == 0:
        print("Список пуст, милорд")
    else:
        print("Все задачи:")
        for i, task in enumerate(t_list, start=1):
            status = "выполнено" if task.done else "не выполнено"
            print(f"{i}. {task.name}, срок: {task.limit}, статус: {status}")

def complete_task(t_list):
    show_all_tasks(t_list)
    index = int(input("Введите номер выполненной задачи: ")) - 1
    if 0 <= index < len(t_list):
        t_list[index].mark_done()
        print("Задача отмечена как выполненная")
    else:
        print("Неверный номер задачи")

def show_current_tasks(t_list):
    print("Текущие задачи:")
    for i, task in enumerate(t_list, start=1):
        if not task.done:
            print(f"{i}. {task.description}, срок: {task.limit}")

def delete_task(t_list):
    show_all_tasks(t_list)
    index = int(input("Введите номер выполненной задачи: ")) - 1
    if 0 <= index < len(t_list):
        t_list[index].delete()
        print("Задача удалена")
    else:
        print("Неверный номер задачи")

def show_info_task(t_list):
    show_all_tasks(t_list)
    index = int(input("Введите номер выполненной задачи: ")) - 1
    if 0 <= index < len(t_list):
        t_list[index].all_info()
    else:
        print("Неверный номер задачи")

tasks = []

worker = Task("Work", "Go work", "18:00", True )
tasks.append(worker)
sleeper = Task("Sleep", "Go sleep", "7:00", False )
tasks.append(sleeper)

while True:
    print("1. Добавить задачу")
    print("2. Отметить задачу выполненной")
    print("3. Показать текущие задачи")
    print("4. Показать все задачи")
    print("5. Удалить задачу")
    print("6. Подробная информация о задаче")
    print("0. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        complete_task(tasks)
    elif choice == "3":
        show_current_tasks(tasks)
    elif choice == "4":
        show_all_tasks(tasks)
    elif choice == "5":
        delete_task(tasks)
    elif choice == "6":
        show_info_task(tasks)
    elif choice == "0":
        print("Выход из программы")
        break
    else:
        print("Неверный ввод")

