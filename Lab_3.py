from random import randint

from faker import Faker

fake = Faker()
M, N = 9, 6
db = {}
access = (
    'открытые данные',
    'секретно',
    'совершенно секретно'
)
commands = ('request', 'quit')
db_objects = {}


def request(name_person):
    while True:
        obj = int(input('К какому объекту хотите получить доступ ')) - 1
        if obj in range(N):
            break
    if db_objects[obj] <= db.get(name_person)[obj]:
        print('Операция прошла успешно')
    else:
        print('Отказ в доступе')


if __name__ == "__main__":
    print('\n   Уровни конфиденциальности объектов')
    for i in range(N):
        db_objects[i] = access[randint(0, 2)]
    for key, value in db_objects.items():
        print("{0}:\t{1}".format(key, value))
    for i in range(M):
        db[fake.name()] = [access[randint(0, 2)] for _ in range(N)]
    print("\n   Уровни доступа пользователей")
    for key, value in db.items():
        print("{0}:\t{1}".format(key, value))

    while True:
        name = input("Введите идентификатор(имя) пользователя: ")
        if name == '0':
            break
        if not (db.get(name) is None):
            print(f"    Уровни доступа пользователя {name}")
            print(db.get(name))
            print(f"    Доступные объекты: \n{db_objects}")
            while True:
                command = input('Жду ваших указаний ')
                if command == commands[0]:
                    request(name)
                elif command == commands[1]:
                    break
                else:
                    print('Введите корректно...')
