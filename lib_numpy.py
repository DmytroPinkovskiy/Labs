import numpy as np


def calculate_array():
    """Виконує обчислення з масивом NumPy."""
    values = np.array([2, 4, 6, 8, 10])
    print("\n[NumPy] Масив:", values)
    print("Сума:", np.sum(values))
    print("Середнє значення:", np.mean(values))
