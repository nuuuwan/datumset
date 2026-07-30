import os

from ds.thing.meta.build.BuildEntityClassListDiscoverMixin import (
    BuildEntityClassListDiscoverMixin,
)
from ds.thing.meta.build.BuildEntityClassListWriteMixin import (
    BuildEntityClassListWriteMixin,
)


class BuildThingFactoryEntityClassListMixin(
    BuildEntityClassListDiscoverMixin,
    BuildEntityClassListWriteMixin,
):

    THING_DIR = os.path.join("src", "ds", "thing")
    OUT_DIR = os.path.join("src", "ds", "thing", "entity_class_list")
    MIXIN_NAME = "ThingFactoryEntityClassListMixin"

    def _main_out_path(self):
        return os.path.join(self.OUT_DIR, self.MIXIN_NAME + ".py")

    def build(self):
        raw = self._leaf_classes(self._discover_all())
        classes = self._dedup(raw)
        groups = self._grouped(classes)
        for group, group_classes in groups:
            self._write(
                self._group_out_path(group),
                self._group_content(group, group_classes),
            )
        self._write(self._main_out_path(), self._main_content(groups))


if __name__ == "__main__":
    BuildThingFactoryEntityClassListMixin().build()
