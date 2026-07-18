import importlib
import inspect
import os

from ds.thing.Thing import Thing
from utils_future import File, Log

log = Log("BuildThingFactoryEntityClassListMixin")


class BuildThingFactoryEntityClassListMixin:

    THING_DIR = os.path.join("src", "ds", "thing")
    OUT_PATH = os.path.join(
        "src", "ds", "thing", "ThingFactoryEntityClassListMixin.py"
    )
    MIXIN_NAME = "ThingFactoryEntityClassListMixin"

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
        superclasses = set()
        for cls in all_classes:
            for parent in cls.__mro__[1:]:
                superclasses.add(parent)
        return [c for c in all_classes if c not in superclasses]

    def _dedup(self, classes):
        by_name = {}
        for cls in sorted(
            classes, key=lambda c: (len(c.__module__), c.__module__)
        ):
            by_name[cls.__name__] = cls
        return sorted(by_name.values(), key=lambda c: c.__name__)

    def _group_key(self, cls):
        parent = cls.__module__.rsplit(".", 1)[0]
        return parent.rsplit(".", 1)[1]

    def _grouped(self, classes):
        groups = {}
        for cls in classes:
            key = self._group_key(cls)
            groups.setdefault(key, []).append(cls)
        return sorted(groups.items())

    def _import_block(self, classes):
        return "\n".join(
            f"from {c.__module__} import {c.__name__}" for c in classes
        )

    def _list_block(self, classes):
        lines = []
        for group, group_classes in self._grouped(classes):
            lines.append(" " * 8 + "# " + "-" * 20)
            lines.append(" " * 8 + f"# {group} ({len(group_classes)})")
            lines.append(" " * 8 + "# " + "-" * 20)
            for i_cls, cls in enumerate(group_classes, start=1):
                lines.append(f"        {cls.__name__},")
                if i_cls % 5 == 0:
                    lines.append(" " * 8 + "#")
        return "\n".join(lines)

    def _content(self, classes):
        imports = self._import_block(classes)
        items = self._list_block(classes)
        return (
            f"{imports}\n\n\n"
            f"class {self.MIXIN_NAME}:\n"
            f"    ENTITY_CLASS_LIST = [\n{items}\n    ]\n"
        )

    def build(self):
        raw = self._leaf_classes(self._discover_all())
        classes = self._dedup(raw)

        new_content = self._content(classes)

        file = File(self.OUT_PATH)
        old_content = file.read() if file.exists() else None

        if old_content != new_content:
            file.write(new_content)
            log.info(f"Wrote {file}")


if __name__ == "__main__":
    BuildThingFactoryEntityClassListMixin().build()
