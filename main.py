from lib_requests import check_site
from lib_colorama import show_colored
from lib_pyfiglet import show_banner
from lib_art import show_art
from lib_rich import show_rich_table
from lib_termcolor import show_termcolor
from lib_emoji import show_emoji
from lib_qrcode import create_qr
from lib_pillow import create_image
from lib_numpy import calculate_array
from builtin_math import math_demo
from builtin_random import random_demo
from builtin_datetime import datetime_demo
from builtin_os import os_demo
from builtin_json import json_demo


def main():
    print("\n=== ЛАБОРАТОРНА РОБОТА 4 ===")
    print("Демонстрація 10 сторонніх і 5 вбудованих бібліотек Python\n")

    show_colored()
    show_banner()
    show_art()
    show_rich_table()
    show_termcolor()
    show_emoji()
    create_image()
    calculate_array()
    math_demo()
    random_demo()
    datetime_demo()
    os_demo()
    json_demo()
    check_site()
    create_qr()

    print("\nУсі демонстрації завершено.")


if __name__ == "__main__":
    main()
