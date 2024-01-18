import json
import random
import time
import os
import codecs

PHRASES_FILE = "sentences.txt"
USERS_FILE = "users.json"
STATS_FILE = "stats.json"


def load_phrases():
    with open(PHRASES_FILE, "r", encoding="utf-8") as f:
        phrases = [line.strip() for line in f.readlines()]
    return phrases


def encrypt_phrase(phrase):
    return codecs.encode(phrase, "rot13")


def decrypt_phrase(encrypted_phrase):
    return codecs.decode(encrypted_phrase, "rot13")


def add_user(login, password, encrypted_phrase, avg_time):
    if not os.path.isfile(USERS_FILE):

        with open(USERS_FILE, "w") as f:
            users = {login: {"password": password, "encrypted_phrase": encrypted_phrase, "avg_time": avg_time}}
            json.dump(users, f)
    else:

        with open(USERS_FILE, "r") as f:
            users = json.load(f)
        users[login] = {"password": password, "encrypted_phrase": encrypted_phrase, "avg_time": avg_time}
        with open(USERS_FILE, "w") as f:
            json.dump(users, f)


def register_user():
    login = input("Придумайте логин: ")
    password = input("Придумайте пароль: ")
    phrases = load_phrases()
    phrase = random.choice(phrases)
    encrypted_phrase = encrypt_phrase(phrase)
    print(f"Введите данную фразу 4 раза: {decrypt_phrase(encrypted_phrase)}")
    times = []
    for i in range(4):
        start_time = time.time()
        typed_phrase = input("Ввод: ")
        end_time = time.time()
        time_taken = end_time - start_time
        times.append(time_taken)
        if typed_phrase != phrase:
            print("Ошибка. Неправильное предложение.")
            return
    avg_time = sum(times) / len(times)
    add_user(login, password, encrypted_phrase, avg_time)
    print(f"avg_time = {avg_time}")
    print("Регистрация выполнена!")


def authenticate_user():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    with open(USERS_FILE, "r") as f:
        users = json.load(f)
    if login not in users or users[login]["password"] != password:
        print("Неверный логин или пароль.")
        return
    encrypted_phrase = users[login]["encrypted_phrase"]
    phrase = decrypt_phrase(encrypted_phrase)
    print(f"Введите данную фразу 4 раза: {phrase}")
    times = []
    for i in range(4):
        start_time = time.time()
        typed_phrase = input("Ввод: ")
        end_time = time.time()
        time_taken = end_time - start_time
        times.append(time_taken)
        if typed_phrase != phrase:
            print("Ошибка. Неправильное предложение.")
            return
    avg_time = sum(times) / len(times)
    print(users[login]["avg_time"])
    print(f"avg_time = {avg_time}")
    if abs(avg_time - users[login]["avg_time"]) < 2:
        print("Вы успешно авторизовались!")
        with open(STATS_FILE, "a") as f:
            f.write(f"{login}: {avg_time}\n")
    else:
        print("Ошибка авторизации. Проверка не пройдена.")


if __name__ == "__main__":
    while True:
        choice = input("Введите 'reg' для регистрации, 'log' для авторизации, 'quit' чтобы выйти: ")
        if choice == "reg":
            register_user()
        elif choice == "log":
            authenticate_user()
        elif choice == "quit":
            break
        else:
            print("Неправильная команда!")
