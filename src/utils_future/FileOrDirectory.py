import os
from abc import ABC
from functools import cached_property


class FileOrDirectory(ABC):
    def __init__(self, *path_items):
        self.path = os.path.join(*path_items)

    def exists(self):
        return os.path.exists(self.path)

    def size(self):
        if self.exists():
            return os.path.getsize(self.path)
        return None

    def size_human_readable(self):
        size_bytes = self.size()
        if size_bytes is None:
            return "N/A"
        for unit in ["B", "KB", "MB", "GB", "TB"]:
            if size_bytes < 1024:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024
        return f"{size_bytes:.1f} PB"

    def __str__(self):
        return f"{self.path} ({self.size_human_readable()})"

    def __repr__(self):
        return str(self)

    @cached_property
    def short_path(self):
        parts = self.path.split(os.sep)
        n = len(parts)
        for i in range(n):
            partial_path = os.sep.join(parts[i:])
            if len(partial_path) <= 30:
                return partial_path
        raise ValueError("Path is too long to shorten")

    @cached_property
    def short_str(self):
        return f"{self.short_path} ({self.size_human_readable()})"

    def open(self, app=None):
        app = app or "open"
        os.system(f'{app} "{self.path}"')
