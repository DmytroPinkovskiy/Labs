import pyfiglet


def show_banner():
    """Створює текстовий банер з ASCII-символів."""
    print("\n[pyfiglet]")
    print(pyfiglet.figlet_format("LAB 4", font="small"))
