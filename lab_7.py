import tkinter as tk
import time
from threading import Timer

users = {
    "timix": "1337",
    "max": "2228",
    "ramis": "1477"
}

attempts = 0


def check_login():
    global attempts
    username = username_entry.get()
    password = ''.join(password_entry)
    #print(password)

    if username in users and password == users[username]:
        success_window = tk.Toplevel()
        success_window.title("Success")
        success_message = tk.Label(success_window, text="Вы успешно авторизовались!")
        success_message.pack()
        #message_label.config(text=f"Ваш пароль: {password}")
        attempts = 0
    else:
        attempts += 1
        message_label.config(text=f"Неверный логин или пароль! Попыток осталось: {3-attempts}")

    if attempts == 2:
        message_label.config(text=f"Осталась последняя попытка до блокировки на 5 секунд.")
    if attempts >= 3:
        #fail_window = tk.Toplevel()
        #fail_window.title("Ошибка")
        #fail_message = tk.Label(fail_window, text="У вас закончились попытки входа!")
       # fail_message.pack()
        message_label.config(text=f"Время прошло, можете попробовать снова...")
        # fail_message.mainloop()
        login_window.after(5000)
        # fail_message.destroy()
        attempts = 0
        #message_label.config(text=f"У вас закончились попытки входа!")
        # password_label.destroy()
        #password_frame.destroy()
        # username_label.destroy()
        # username_entry.destroy()


def button_click(button):
    global password_entry
    password_entry.append(button.cget("text"))
    if len(password_entry) == 4:
        check_login()
        password_entry = []


login_window = tk.Tk()
login_window.title("Графический ключ")

username_label = tk.Label(login_window, text="Имя пользователя", height=3)
username_label.pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

password_label = tk.Label(login_window, text="Пароль", height=3)
password_label.pack()
password_frame = tk.Frame(login_window)
password_frame.pack()

password_entry = []
buttons = []

for i in range(3):
    button_row = []
    for j in range(3):
        button = tk.Button(password_frame, text=str(i*3+j+1), width=15, height=7)
        button.grid(row=i, column=j)
        button.config(command=lambda button=button: button_click(button))
        button_row.append(button)
    buttons.append(button_row)


message_label = tk.Label(login_window, fg="red")
message_label.pack()

login_window.mainloop()



