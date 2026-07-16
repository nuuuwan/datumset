from utils_future.FileOrDirectory import FileOrDirectory


class File(FileOrDirectory):
    ENCODING = "utf-8"

    def read(self):
        with open(self.path, "r", encoding=self.ENCODING) as f:
            return f.read()

    def write(self, data):
        with open(self.path, "w", encoding=self.ENCODING) as f:
            return f.write(data)
