import importlib
import inspect
import os

from ds.thing.Thing import Thing


class BuildEntityClassListDiscoverMixin:

    def _is_py_file(self, fname):
        return fname.endswith(".py") and not fname.startswith("_")

    def _iter_module_paths(self):
        for root, dirs, files in os.walk(self.THING_DIR):
            dirs[:] = [d for d in dirs if d != "meta"]
            for fname in files:
                if not self._is_py_file(fname):
                    continue
                rel = os.path.relpath(os.path.join(root, fname), "src")
                yield rel.replace(os.sep, ".")[:-3]

    def _is_concrete_thing(self, cls, module):
        if not (inspect.isclass(cls) and issubclass(cls, Thing)):
            return False
        if cls is Thing or inspect.isabstract(cls):
            return False
        return cls.__module__ == module.__name__

    def _add_from_module(self, mod, found):
        for _, cls in inspect.getmembers(mod, inspect.isclass):
            if self._is_concrete_thing(cls, mod):
                found.add(cls)

    def _discover_all(self):
        found = set()
        for mod_path in self._iter_module_paths():
            try:
                mod = importlib.import_module(mod_path)
                self._add_from_module(mod, found)
            except Exception:
                pass
        return found

    def _leaf_classes(self, all_classes):
        all_set = set(all_classes)
        direct_subcount = {cls: 0 for cls in all_classes}
        for cls in all_classes:
            for parent in cls.__bases__:
                if parent in all_set:
                    direct_subcount[parent] += 1
        return [c for c in all_classes if direct_subcount[c] < 2]

    def _dedup(self, classes):
        by_name = {}
        for cls in classes:
            name = cls.__name__
            if name in by_name:
                raise Exception(
                    f"Duplicate: {name} in "
                    f"{cls.__module__} and "
                    f"{by_name[name].__module__}"
                )
            by_name[name] = cls
        return sorted(by_name.values(), key=lambda c: c.__name__)
