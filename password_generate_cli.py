
import random 

def password_random(length_paswd, var_password):
    #Исходникик для работы с паролем
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = alphabet + alphabet.upper()
    numbers = "1234567890"
    symbols = "!@$%^()_:;.,></?"
    methods = {
        1: random.choices(alphabet, k=length_paswd), 
        2: random.choices(numbers, k=length_paswd),
        3: random.choices(alphabet + numbers, k=length_paswd),
        4: random.choices(alphabet + numbers + symbols, k=length_paswd)
    }


    password_out = methods[var_password]
    return password_out


print("""Добро пожаловать в генератор паролей
        Сгенерировать пароль по следующим параметрам:
      1 - Буквенный пароль
      2 - Пароль из цифр
      3 - Буквы и цифры
      4 - Буквы, цифры и символы""")

var_password = int(input("Введите параметр: "))
length_password = int(input("Введите длину пароля: "))

print(*password_random(length_password, var_password), sep="")

