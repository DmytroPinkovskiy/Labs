from datetime import datetime


def datetime_demo():
    """Показує поточну дату й час."""
    now = datetime.now()
    print("\n[datetime] Поточні дата й час:", now.strftime("%d.%m.%Y %H:%M:%S"))
