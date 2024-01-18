import random
import math


def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)  # вычисляем значение функции эйлера от n

    e = random.randrange(1, phi)  # выбираем целое число е, которое является взаимно простым со значением функ Эйлера
    g = math.gcd(e, phi)  # находим НОД е и функции Эйлера
    while g != 1:
        e = random.randrange(1, phi)
        g = math.gcd(e, phi)

    # Вычисляем значение d, которое является обратным по модулю е к значению функции эйлера
    d = reverse_mod(e, phi)

    # возвращаем ((публичный ключ) (приватный ключ))
    return ((n, e), (n, d))


def encrypt(pk, plaintext):
    n, e = pk

    # кодируем каждый символ в сообщении в код с помощью код^e mod n
    cipher = [pow(ord(char), e, n) for char in plaintext]

    # возвращаем массив битов
    return cipher


def decrypt(pk, ciphertext):
    n, d = pk

    # декодируем каждый символ в сообщении с помощью код^e mod n
    plain = [chr(pow(char, d, n)) for char in ciphertext]

    return ''.join(plain)


def reverse_mod(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


p = 19
q = 43
public, private = generate_keypair(p, q)

message = "I love DSTU"
encrypted_message = encrypt(public, message)

decrypted_message = decrypt(private, encrypted_message)

print(f"Публичный ключ: {public}")
print(f"Приватный ключ: {private}")
print(f"Закодированное сообщение: {encrypted_message}")
print(f"Декодированное сообщение: {decrypted_message}")
