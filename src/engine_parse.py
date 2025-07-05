import argparse


class EngineParse:
    def __init__(self):
        # TODO: Можно ли установить порядок передачи аргументов, и можно ли привязать один аргумент к другому,
        #  чтобы один был зависим от другого при вызове???
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("--file") # TODO: Дописать строку для --help
        self.parser.add_argument("--where") # TODO: Дописать строку для --help
        self.parser.add_argument("--aggregate") # TODO: Дописать строку для --help
        self.parser.add_argument("--order_by") # TODO: Дописать строку для --help


    @property
    def get_args(self):
        return self.parser.parse_args()