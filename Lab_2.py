from random import randint
from faker import Faker

fake = Faker()
M, N = 9, 6

rules = {
    "Полный запрет": bin(0)[2:],
    "Передача прав": bin(1)[2:],
    "Запись": bin(2)[2:],
    "Запись, Передача прав": bin(3)[2:],
    "Чтение": bin(4)[2:],
    "Чтение, Передача прав": bin(5)[2:],
    "Чтение, запись": bin(6)[2:],
    "Полный доступ": bin(7)[2:]

}
names = {}


def do_obt():
    objt = int(input("Над каким объектом производится операция? ")) - 1
    while True:
        if objt in range(N):
            break
        else:
            objt = int(input("Над каким объектом производится операция? ")) - 1
    return objt


if __name__ == "__main__":
    for i in range(M):
        names[fake.name()] = [bin(randint(0, 7))[2:] for _ in range(N)]
    for key, value in names.items():
        print("{0}:\t{1}".format(key, value))

    while True:
        name = input("Введите идентификатор(имя) пользователя: ")
        if name == '0':
            break
        if not (names.get(name) is None):
            print(
                f"0   0	Полный запрет"
                f"\n1   1	Передача прав"
                f"\n2   10	Запись"
                f"\n3   11	Запись, Передача прав	"
                f"\n4   100	Чтение	"
                f"\n5   101	Чтение, Передача прав	"
                f"\n6   110	Чтение, Запись	"
                f"\n7   111	Полный доступ	"
            )
        while True:
            print(f"Права пользователя {name}: ", names.get(name))
            c = input("Введите команду (Чтение, Запись...): ")
            if c == '0':
                break
            command = rules.get(c)
            while True:
                if command is None:
                    c = input("Введите команду (Чтение, Запись...): ")
                    if c == '0':
                        break
                    command = rules.get(c)
                else:
                    break
            if c == '0':
                break
            obt = do_obt()
            cur_rule = names.get(name)[obt]
            match c:
                case "Передача прав":
                    if cur_rule in ["1", "11", "101", "111"]:
                        different = input("На кого оформить права? Введите имя человека (0-отмена операции) - ")
                        while True:
                            if not (names.get(different) is None) or different == '0':
                                break
                        if different == '0':
                            print("Операция отменена")
                        else:
                            dif_val = names.get(different)
                            dif_val[obt] = cur_rule
                            names.update({different: dif_val})
                            print("Операция выполнена успешно!")
                    else:
                        print("Нет доступа! Операция невозможна.")
                case "Чтение":
                    if cur_rule in ["100", "101", "110", "111"]:
                        print("Операция выполнена успешно!")
                    else:
                        print("Нет доступа! Операция невозможна.")
                case "Запись":
                    if cur_rule in ["10", "11", "110", "111"]:
                        print("Операция выполнена успешно!")
                    else:
                        print("нет доступа")
                case default:
                    print("Нет доступа или неверная команда!")

            if int(input("Выйти из пользователя? (0 - не выходить): ")):
                break
