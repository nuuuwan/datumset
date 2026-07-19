from utils_future import Directory, File, JSONFile, Log, String

log = Log("BuildCategoryConceptClass")


class BuildCategoryConceptClass:
    def __init__(
        self,
        class_group: str,
        class_name: str,
        value_list: list = None,
        value_to_value: dict = None,
    ):
        self.class_group = class_group
        self.class_name = class_name
        self.value_list = value_list
        self.value_to_value = value_to_value

    @property
    def values(self):
        if self.value_to_value is not None:
            return [String(v).snake for v in self.value_to_value.keys()]
        if self.value_list is not None:
            return [String(v).snake for v in self.value_list]
        raise ValueError(
            "Either value_list or value_to_value must be provided."
        )

    def get_content_lines(self):
        class_init_list = []
        for i_value, value in enumerate(self.values, start=0):
            if i_value % 5 == 0:
                min_value = i_value + 1
                max_value = min(i_value + 5, len(self.values))
                class_init_list.append(f"# {min_value} - {max_value}")
            class_init_list.append(f'cls("{value}"),')

        class_init_list = "\n            ".join(class_init_list)

        content_lines = [
            "# 🤖 via BuildCategoryConceptClass.py",
            "from ds.thing.concept.CategoryConcept import CategoryConcept",
            "",
            "",
            f"class {self.class_name}(CategoryConcept):",
            "    @classmethod",
            "    def list(cls):",
            "        return [",
            f"            {class_init_list}",
            "        ]",
            "",
        ]
        return content_lines

    def build(self):
        directory = Directory(
            "src",
            "ds",
            "thing",
            "concept",
            self.class_group,
        )
        directory.make()
        class_file = File(
            directory.path,
            f"{self.class_name}.py",
        )
        # if class_file.exists():
        #     return
        content_lines = self.get_content_lines()

        class_file.write("\n".join(content_lines))
        log.info(f"Wrote {class_file}")


if __name__ == "__main__":

    specs = JSONFile(
        "src", "ds", "thing", "meta", "build_category_concept_specs.json"
    ).read()

    for spec in specs:
        builder = BuildCategoryConceptClass(
            spec["class_group"],
            spec["class_name"],
            value_list=spec.get("value_list"),
            value_to_value=spec.get("value_to_value") or spec.get("values"),
        )
        builder.build()
