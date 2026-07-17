import csv

from utils_future.File import File
from utils_future.Log import Log

log = Log("TSVFile")


class TSVFile(File):
    def read(self):
        with open(self.path, encoding="utf-8") as f:
            reader = csv.reader(f, delimiter="\t")
            headers = next(reader)
            d_list = [dict(zip(headers, row)) for row in reader if row]
            log.debug(f"Read {len(d_list)} rows from {self}")
            return d_list
