import os
import tempfile

from utils_future.FileOrDirectory import FileOrDirectory


class Directory(FileOrDirectory):
    def make(self):
        os.makedirs(self.path, exist_ok=True)

    @classmethod
    def get_temp(cls, *args):
        director = cls(tempfile.gettempdir(), *args)
        director.make()
        return director
