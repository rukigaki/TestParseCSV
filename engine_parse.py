import argparse


class EngineParse:
    def __init__(self):
      self.parser = argparse.ArgumentParser()

    @property
    def get_args(self):

        self.parser.add_argument("--file")
        self.parser.add_argument("--where")
        self.parser.add_argument("--aggregate")

        args = self.parser.parse_args()

        return args