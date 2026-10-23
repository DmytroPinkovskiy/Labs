products = {
    1: {"name": "Клавіатура", "price": 850.00, "stock": 10},
    2: {"name": "Миша", "price": 450.00, "stock": 15},
    3: {"name": "Навушники", "price": 1250.50, "stock": 7},
    4: {"name": "Монітор", "price": 5200.00, "stock": 4},
    5: {"name": "Килимок", "price": 199.99, "stock": 20}
}

cart = {}

ADMIN_LOGIN = "admin"
ADMIN_PASSWORD = "admin123"

format_price = lambda price: f"{price:.2f} грн"


def get_number(message):
    try:
        number = int(input(message))
        if number <= 0:
            print("Число повинно бути більшим за нуль.")
            return None
        return number
    except ValueError:
        print("Помилка! Введіть ціле число.")
        return None


def show_catalog():
    print("\n========== КАТАЛОГ ТОВАРІВ ==========")

    sorted_products = sorted(
        products.items(),
        key=lambda item: item[1]["price"]
    )

    for product_id, product in sorted_products:
        print(
            f"{product_id}. {product['name']} | "
            f"Ціна: {format_price(product['price'])} | "
            f"У наявності: {product['stock']}"
        )


def show_cart():
    print("\n========== ВАШ КОШИК ==========")

    if not cart:
        print("Кошик порожній.")
        return

    for product_id, quantity in cart.items():
        product = products[product_id]
        total = product["price"] * quantity

        print(
            f"{product['name']} | "
            f"Кількість: {quantity} | "
            f"Сума: {format_price(total)}"
        )

    total_price = sum(
        products[product_id]["price"] * quantity
        for product_id, quantity in cart.items()
    )

    print(f"Разом: {format_price(total_price)}")


def add_to_cart():
    show_catalog()

    product_id = get_number("Введіть номер товару: ")
    if product_id is None:
        return

    if product_id not in products:
        print("Такого товару немає.")
        return

    quantity = get_number("Введіть кількість: ")
    if quantity is None:
        return

    product = products[product_id]
    already_in_cart = cart.get(product_id, 0)

    if already_in_cart + quantity > product["stock"]:
        print("Недостатньо товару на складі.")
        return

    cart[product_id] = already_in_cart + quantity
    print("Товар додано до кошика!")


def remove_from_cart():
    show_cart()

    if not cart:
        return

    product_id = get_number("Введіть номер товару для видалення: ")
    if product_id is None:
        return

    if product_id not in cart:
        print("Цього товару немає у кошику.")
        return

    del cart[product_id]
    print("Товар видалено з кошика.")


def buy_products():
    if not cart:
        print("Ваш кошик порожній.")
        return

    show_cart()
    answer = input("Підтвердити покупку? (так/ні): ").strip().lower()

    if answer != "так":
        print("Покупку скасовано.")
        return

    for product_id, quantity in cart.items():
        if quantity > products[product_id]["stock"]:
            print("Покупку неможливо оформити: недостатньо товару.")
            return

    total_price = sum(
        products[product_id]["price"] * quantity
        for product_id, quantity in cart.items()
    )

    for product_id, quantity in cart.items():
        products[product_id]["stock"] -= quantity

    print(
        f"Покупку успішно оформлено на суму "
        f"{format_price(total_price)}!"
    )
    cart.clear()


def admin_menu():
    login = input("Логін адміністратора: ")
    password = input("Пароль адміністратора: ")

    if login != ADMIN_LOGIN or password != ADMIN_PASSWORD:
        print("Неправильний логін або пароль.")
        return

    print("\n========== ПАНЕЛЬ АДМІНІСТРАТОРА ==========")

    for product_id, product in products.items():
        print(
            f"{product_id}. {product['name']} | "
            f"Залишок: {product['stock']} шт. | "
            f"Ціна: {format_price(product['price'])}"
        )


def main():
    while True:
        print("\n========== МІНІМАГАЗИН ==========")
        print("1. Переглянути каталог")
        print("2. Додати товар до кошика")
        print("3. Переглянути кошик")
        print("4. Видалити товар із кошика")
        print("5. Купити товари")
        print("6. Увійти як адміністратор")
        print("0. Вийти")

        choice = input("Оберіть дію: ").strip()

        if choice == "1":
            show_catalog()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            show_cart()
        elif choice == "4":
            remove_from_cart()
        elif choice == "5":
            buy_products()
        elif choice == "6":
            admin_menu()
        elif choice == "0":
            print("Дякуємо за покупку! До побачення.")
            break
        else:
            print("Невірний пункт меню. Спробуйте ще раз.")


if __name__ == "__main__":
    main()