from rich.console import Console
from rich.table import Table


def show_rich_table():
    """Показує таблицю з кольоровим форматуванням."""
    console = Console()
    table = Table(title="Приклади бібліотек")
    table.add_column("Тип", style="cyan")
    table.add_column("Приклад", style="magenta")
    table.add_row("Стороння", "rich")
    table.add_row("Вбудована", "math")
    console.print(table)
