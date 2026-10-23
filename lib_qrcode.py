import qrcode


def create_qr():
    """Створює QR-код із посиланням і зберігає його у файл."""
    image = qrcode.make("https://www.python.org")
    image.save("python_qr.png")
    print("[qrcode] QR-код збережено у файлі python_qr.png")
