import random

def get_numbers_ticket(minv, maxv, quantity):
        if minv >= 1 and maxv <= 1000 and quantity >= 1 and quantity <= (maxv - minv + 1):
            return sorted(random.sample(range(minv, maxv + 1), quantity))
        else:
            return []
min = int(input("Введіть мінімальне число (>=1): "))
max = int(input("Введіть максимальне число (<=1000): "))
quantity = int(input("Введіть кількість переможних чисел: "))
lottery_numbers = get_numbers_ticket(min, max, quantity)
print("Ваші лотерейні числа:", lottery_numbers)