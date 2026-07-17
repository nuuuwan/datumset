import requests

from utils_future.Log import Log

log = Log("WWW")


class WWW:
    def __init__(self, url: str):
        self.url = url

    def __str__(self):
        return f"🌐{self.url}"

    def download(self, output_file):
        if output_file.exists():
            return

        response = requests.get(self.url, timeout=10)
        response.raise_for_status()
        content = response.text

        output_file.write(content)
        log.debug(f"Downloaded {self} to {output_file}")
