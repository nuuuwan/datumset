import os

from utils_future import File, Log

log = Log("BuildEntityClassListWriteMixin")


class BuildEntityClassListWriteMixin:

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
        for i_cls, cls in enumerate(classes, start=1):
            lines.append(f"        {cls.__name__},")
            if i_cls % 5 == 0:
                lines.append(" " * 8 + "#")
        return "\n".join(lines)

    def _group_class_name(self, group):
        return "EntityClassList" + group.title().replace("_", "") + "Mixin"

    def _group_out_path(self, group):
        return os.path.join(
            self.OUT_DIR, self._group_class_name(group) + ".py"
        )

    def _group_content(self, group, classes):
        imports = self._import_block(classes)
        items = self._list_block(classes)
        class_name = self._group_class_name(group)
        return (
            f"{imports}\n\n\n"
            f"class {class_name}:\n"
            f"    ENTITY_CLASS_LIST = [\n{items}\n    ]\n"
        )

    def _main_content(self, groups):
        names = [self._group_class_name(group) for group, _ in groups]
        imports = "\n".join(
            f"from ds.thing.entity_class_list.{name} import {name}"
            for name in names
        )
        combined = "\n        + ".join(
            f"{name}.ENTITY_CLASS_LIST" for name in names
        )
        return (
            f"{imports}\n\n\n"
            f"class {self.MIXIN_NAME}:\n"
            f"    ENTITY_CLASS_LIST = (\n        {combined}\n    )\n"
        )

    def _write(self, path, content):
        file = File(path)
        old_content = file.read() if file.exists() else None
        if old_content != content:
            file.write(content)
            log.info(f"Wrote {file}")
