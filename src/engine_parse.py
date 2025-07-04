import argparse


class EngineParse:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("--file")
        self.parser.add_argument("--where")
        self.parser.add_argument("--aggregate")


    @property
    def get_args(self):
        return self.parser.parse_args()