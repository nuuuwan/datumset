from utils_future import Directory, File, Log, String

log = Log("BuildCategortConceptClass")


class BuildCategortConceptClass:
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
            return [String(v).pascal for v in self.value_to_value.keys()]
        if self.value_list is not None:
            return [String(v).pascal for v in self.value_list]
        raise ValueError(
            "Either value_list or value_to_value must be provided."
        )

    def get_content_lines(self):
        class_init_list = []
        for i_value, value in enumerate(self.values, start=0):
            if i_value % 5 == 0:
                min_value = i_value
                max_value = min(i_value + 4, len(self.values) - 1)
                class_init_list.append(f"# {min_value} - {max_value}")
            class_init_list.append(f'cls("{value}"),')

        class_init_list = "\n            ".join(class_init_list)

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
            "value_to_value": {
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
        },
        {
            "class_group": "census",
            "class_name": "CensusTopic",
            "value_list": [
                "schedule",
                "Demographic and Personal Information",
                "Name",
                "Relationship to head of the household",
                "Sex",
                "Date of birth",
                "Age",
                "Marital Status",
                "Ethnic group",
                "Religion",
                "Citizenship",
                "N.I.C. No.",
                "Status of clergy/priest",
                "Educational Characteristics",
                "Ability to speak Sinhala & Tamil",
                "Ability to speak English",
                "Ability to speak Sinhala, English & Tamil",
                "Literacy",
                "English Literacy",
                "Sinhala, English & Tamil Literacy",
                "Computer Literacy",
                "Digital Literacy",
                "Educational attainment/Highest level of",
                "School Attendance/ Attend in educational",
                "Vocational & Apprenticeship qualification",
            ],
        },
        {
            "class_group": "government",
            "class_name": "AdministrativeEntity",
            "value_to_value": {
                "assistant_government_agend_divisions": 10,
                "grama_sevaka_divisions": 230,
                "municipal_councils": 0,
                "urban_councils": 4,
                "town_councils": 6,
            },
        },
        {
            "class_group": "government",
            "class_name": "Sector",
            "value_to_value": {
                "urban": 10,
                "rural": 230,
                "estate": 0,
                "estate-rural": 4,
                "estate-urban": 6,
            },
        },
        {
            "class_group": "people",
            "class_name": "MigrationStatus",
            "value_to_value": {
                "local": 1123880,
                "foreign": 951,
                "migrant": 180877,
            },
        },
        {
            "class_group": "people",
            "class_name": "MigrationDirection",
            "value_to_value": {
                "in_migrants": 1123880,
                "out_migrants": 951,
            },
        },
        {
            "class_group": "time",
            "class_name": "TimeGroup0510More",
            "value_list": [
                "00_04_years",
                "05_09_years",
                "10_or_more_years",
            ],
        },
        {
            "class_group": "people",
            "class_name": "MigrationReason",
            "value_to_value": {
                "marriage": 0.349,
                "employment_searching_for_job": 0.261,
                "education": 0.043,
                "accompanied_a_family_member": 0.19,
                "returning_for_permanent_residence": 0.128,
                "development_projects": 0.002,
                "resettled_after_displacement": 0.002,
                "a_disaster_a_displaced_happened_in_the_prior_place": 0.006,
                "other": 0.018,
            },
        },
        {
            "class_group": "people",
            "class_name": "ResidentRelativeToDistrict",
            "value_list": [
                "in_district",
                "in_other_district",
            ],
        },
        {
            "class_group": "people",
            "class_name": "EmmigrationReason",
            "value_list": [
                "employment",
                "education",
                "accompanying_family_member_in_need",
                "other",
            ],
        },
    ]

    for spec in specs:
        builder = BuildCategortConceptClass(
            spec["class_group"],
            spec["class_name"],
            value_list=spec.get("value_list"),
            value_to_value=spec.get("value_to_value"),
        )
        builder.build()
