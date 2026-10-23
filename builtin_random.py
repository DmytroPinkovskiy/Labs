import random


def random_demo():
    """Генерує випадкове число та перемішує список."""
    print("\n[random] Випадкове число від 1 до 100:", random.randint(1, 100))
    numbers = [1, 2, 3, 4, 5]
    random.shuffle(numbers)
    print("[random] Перемішаний список:", numbers)
