from utils_future import Directory, File, Log

log = Log("BuiltEntityClass")


class BuiltEntityClass:
    def __init__(
        self,
        class_name: str,
    ):
        self.class_name = class_name

    def get_content_lines(self):

        content_lines = [
            "# 🤖 via BuiltEntityClass.py",
            "from ds.thing.entity.Entity import Entity",
            "",
            "",
            f"class {self.class_name}(Entity):",
            "    pass",
            "",
        ]
        return content_lines

    def build(self):
        directory = Directory(
            "src",
            "ds",
            "thing",
            "entity",
        )
        directory.make()

        class_file = File(
            directory.path,
            f"{self.class_name}.py",
        )
        if class_file.exists():
            return
        content_lines = self.get_content_lines()

        class_file.write("\n".join(content_lines))
        log.info(f"Wrote {class_file}")


if __name__ == "__main__":

    class_names = ["Census"]

    for class_name in class_names:
        builder = BuiltEntityClass(
            class_name,
        )
        builder.build()
