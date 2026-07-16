import hashlib

import requests

from utils_future.Directory import Directory
from utils_future.File import File
from utils_future.Log import Log

log = Log("WWW")


class WWW:
    def __init__(self, url: str):
        self.url = url

    def __str__(self):
        return f"🌐{self.url}"

    @property
    def temp_file(self):
        temp_dir = Directory.get_temp("datumset", "www")
        h = hashlib.md5(self.url.encode()).hexdigest()[:8]
        return File(temp_dir.path, h)

    def read(self):
        if self.temp_file.exists():
            return self.temp_file.read()

        response = requests.get(self.url, timeout=10)
        response.raise_for_status()
        content = response.text
        self.temp_file.write(content)
        log.debug(f"Wrote {self} to {self.temp_file}")
        return content

    def download(self, file: File):
        content = self.read()
        file.write(content)
        log.debug(f"Downloaded {self} to {file}")
