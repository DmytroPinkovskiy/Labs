import json


def json_demo():
    """Перетворює словник у JSON і назад."""
    student = {"name": "Dmytro", "lab": 4, "status": "in progress"}
    json_text = json.dumps(student, ensure_ascii=False, indent=2)
    restored = json.loads(json_text)
    print("\n[json] Дані у форматі JSON:")
    print(json_text)
    print("Назва лабораторної після читання JSON:", restored["lab"])
