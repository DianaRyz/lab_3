import csv
import os


class Iterator:
    def __init__(self, class_name: str, path: str) -> None:
        """
        Initializes an object of the class
            class_name(str): tiger or leopard
            path(str): path of the csv file
        """
        self.class_name = class_name
        self.path = path
        self.counter = 0
        self.list = []

        if os.path.exists(self.path):
            headings = ["Absolute way", "Relative way", "Class"]
            with open(self.path, "r", encoding="utf8") as f:
                read = csv.DictReader(f, fieldnames=headings, delimiter=";")
                for element in read:
                    if element["Class"] == class_name:
                        self.list.append(
                            [element["Absolute way"], element["Relative way"], element["Class"]]
                        )
        else:
            raise FileNotFoundError

    def __iter__(self):
        return self

    def __next__(self):
        """
        The function of switching to the next element in the list, return
        the path to this element
        """
        self.counter += 1
        if self.counter < len(self.list):
            return self.list[self.counter][0]
        elif self.counter == len(self.list):
            raise StopIteration


if __name__ == "__main__":
    iterator = Iterator("leopard", "annotation.csv")
    for i in iterator:
        print(i)
