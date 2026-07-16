import os

from utils_future.FileOrDirectory import FileOrDirectory


class Directory(FileOrDirectory):
    def make(self):
        os.makedirs(self.path, exist_ok=True)
