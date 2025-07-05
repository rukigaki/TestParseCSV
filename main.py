import csv
from tabulate import tabulate
from pathlib import Path

from src.engine_parse import EngineParse
from src.operations_module import Operations


def parse_func():
    parser = EngineParse()
    args = parser.get_args
    #Объект argparse
    return args


def read_file(args) -> list[dict]:
    path_str = Path(args.file)
    if not path_str.exists():
        raise FileNotFoundError(f"Файл не найден: {path_str}")

    with open(path_str) as f:
        reader = csv.DictReader(f)
        table = list(reader)

    return table


def main():
    args = parse_func()
    table = read_file(args)

    operations = Operations(args)
    table = operations(table)

    print(tabulate(tabular_data=table, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()

