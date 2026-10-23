import os


def os_demo():
    """Показує робочу папку та вміст поточної директорії."""
    print("\n[os] Робоча папка:", os.getcwd())
    print("[os] Кількість елементів у папці:", len(os.listdir(".")))
