# Задание 1
#При заданном целом числе n посчитайте n + nn + nnn.
#Выполнить задачу с помощью класса.


class Summa_N:
    def __init__(self, n):
        self.n = n
       
    
    def get_sum(self):
        l = self.n + int(f'{self.n}'+ f'{self.n}') + int(f'{self.n}'+ f'{self.n}' + f'{self.n}')
        print(l)

N = int(input("Vedite N: "))

a = Summa_N(N)
a.get_sum()