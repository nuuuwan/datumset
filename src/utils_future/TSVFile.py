import csv

from utils_future.File import File


class TSVFile(File):
    def read(self):
        with open(self.path, encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter="\t")
            d_list = list(reader)
            return d_list
