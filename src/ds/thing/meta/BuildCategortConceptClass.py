from utils_future import Directory, File, Log, String

log = Log("BuildCategortConceptClass")


class BuildCategortConceptClass:
    def __init__(self, class_group: str, class_name: str, values: dict):
        self.class_group = class_group
        self.class_name = class_name
        self.values = values

    @property
    def value_list(self):
        return [String(v).pascal for v in self.values.keys()]

    def get_content_lines(self):
        class_init_list = "\n            ".join(
            [f'cls("{value}"),' for value in self.value_list]
        )

        content_lines = [
            "# 🤖 via BuildCategortConceptClass.py",
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
        content_lines = self.get_content_lines()
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
        class_file.write("\n".join(content_lines))
        log.info(f"Wrote {class_file}")


if __name__ == "__main__":

    specs = [
        {
            "class_group": "census",
            "class_name": "CensusOfficer",
            "values": {
                "deputy_census_commissioners": 14,
                "assistant_census_commissioners": 14,
                "technical_staff_zonal_supervisors_and_district_statistical_branch_head": 18,
                "technical_staff_divisional_census_officer": 13,
                "technical_staff_area_supervisors": 53,
                "technical_staff_circle_officers": 98,
                "other_non_technical_staff": 70,
                "enumerators_who_used_tablet_computers_capi": 1104,
                "enumerators_who_used_smart_phones_byoad": 1986,
            },
        }
    ]

    for spec in specs:
        builder = BuildCategortConceptClass(
            spec["class_group"],
            spec["class_name"],
            spec["values"],
        )
        builder.build()
