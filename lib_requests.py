import requests


def check_site():
    """Перевіряє доступність сайту через HTTP-запит."""
    print("\n[requests] Перевірка сайту https://example.com")
    try:
        response = requests.get("https://example.com", timeout=5)
        print("HTTP-статус:", response.status_code)
    except requests.RequestException as error:
        print("Не вдалося перевірити сайт:", error)
