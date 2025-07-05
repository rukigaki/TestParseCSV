import argparse


class EngineParse:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("--file", help="Путь к CSV-файлу для обработки.")
        self.parser.add_argument("--where", help="Фильтрация строк по условию.")
        self.parser.add_argument("--aggregate", help="Агрегация по столбцу. Пример: price=avg (поддерживаются: avg, min, max).")
        self.parser.add_argument("--order_by", help="Сортировка по столбцу. Пример: price:asc или rating:desc.")


    @property
    def get_args(self):
        return self.parser.parse_args()