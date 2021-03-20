# Задание 4
# Напишите Программу - которая работает по принципу алгоритма Шифр Цезаря.
# Нужно создать класс состоящий из 2 методов:
# 1. Метод который ШИФРУЕТ данные.
# 2. Метода который ДЕШИФРУЕТ эти же данные.
# Представим что ваш метод получает слово состоящее из ЛЮБЫХ символов.
# Ваш 1-й метод должен вернуть зашифрованную строку.
# Алгоритм Шифрования: ASCII позиция + 7.
# Алгоритм Дешифровки: Обратная операция Алгоритма Шифрования.


class CaesarCipher:
    @staticmethod
    def encrypt(encrypt,key):
        result = ""
        for char in encrypt:
            if char == " ": 
                result += " "
                continue
            if ord(char) > 96 :
                result += chr((ord(char) + key - 97) % 26 + 97)
            else:
                result += chr((ord(char)+ key - 65) % 26 +65)
           
        return result

    # this method decrypt cipher text
    @staticmethod
    def decrypt(encrypt,key):
        result = ""
        for char in encrypt:
            if char == " ":
                result += " "
                continue
            if ord(char) > 96 :
                result += chr((ord(char) - key - 97) % 26 + 97)
            else:
                result += chr((ord(char) - key -65) % 65 +65)

        return result
if __name__ == "__main__":    
    encrypt = input("введите текст: ")
    key = 7
    encrypted = CaesarCipher.encrypt(encrypt,key)
    decrypted = CaesarCipher.decrypt(encrypted,key)
    print("encrypt : ", encrypt)
    print("encrypted : ", encrypted)
    print("decrypted : ", decrypted) 