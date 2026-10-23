from colorama import Fore, Style, init


def show_colored():
    """Виводить кольоровий текст у консолі."""
    init(autoreset=True)
    print(Fore.GREEN + "[colorama] Кольоровий текст" + Style.RESET_ALL)
