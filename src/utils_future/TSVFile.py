import csv

from utils_future.File import File
from utils_future.Log import Log

log = Log("TSVFile")


class TSVFile(File):
    def read(self):
        with open(self.path, encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter="\t")
            d_list = list(reader)
            log.debug(f"Read {len(d_list)} rows from {self}")
            return d_list
