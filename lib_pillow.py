from PIL import Image, ImageDraw


def create_image():
    """Створює просте зображення та зберігає його."""
    image = Image.new("RGB", (420, 140), color="white")
    draw = ImageDraw.Draw(image)
    draw.rectangle((10, 10, 410, 130), outline="navy", width=4)
    draw.text((35, 55), "Lab 4 - Python libraries", fill="black")
    image.save("lab4_image.png")
    print("[Pillow] Зображення збережено у файлі lab4_image.png")
