import unittest

from ds import Datumset

TEST_DATUMSET = Datumset.from_data(
    {
        "Person": {
            "Time:2012": {
                "District:LK-11": {
                    "Religion:buddhist": {
                        "Count": "Int:123",
                    },
                    "Religion:hindu": {
                        "Count": "Int:456",
                    },
                },
                "District:LK-12": {
                    "Religion:buddhist": {
                        "Count": "Int:1231",
                    },
                    "Religion:hindu": {
                        "Count": "Int:4561",
                    },
                },
            },
            "Time:2024": {
                "District:LK-11": {
                    "Religion:buddhist": {
                        "Count": "Int:1230",
                    },
                    "Religion:hindu": {
                        "Count": "Int:4560",
                    },
                },
                "District:LK-12": {
                    "Religion:buddhist": {
                        "Count": "Int:12310",
                    },
                    "Religion:hindu": {
                        "Count": "Int:45610",
                    },
                },
            },
        }
    }
)


class TestCase(unittest.TestCase):
    def test_split(self):
        datumset = TEST_DATUMSET

        split_datumsets = datumset.split("Time")

        self.assertEqual(len(split_datumsets), 2)

        self.assertEqual(
            split_datumsets[0].to_data(),
            {
                "Person": {
                    "Time:2012": {
                        "District:LK-11": {
                            "Religion:buddhist": {
                                "Count": "Int:123",
                            },
                            "Religion:hindu": {
                                "Count": "Int:456",
                            },
                        },
                        "District:LK-12": {
                            "Religion:buddhist": {
                                "Count": "Int:1231",
                            },
                            "Religion:hindu": {
                                "Count": "Int:4561",
                            },
                        },
                    },
                }
            },
        )
        self.assertEqual(
            split_datumsets[1].to_data(),
            {
                "Person": {
                    "Time:2024": {
                        "District:LK-11": {
                            "Religion:buddhist": {
                                "Count": "Int:1230",
                            },
                            "Religion:hindu": {
                                "Count": "Int:4560",
                            },
                        },
                        "District:LK-12": {
                            "Religion:buddhist": {
                                "Count": "Int:12310",
                            },
                            "Religion:hindu": {
                                "Count": "Int:45610",
                            },
                        },
                    },
                }
            },
        )
