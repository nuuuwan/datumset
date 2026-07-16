from ds.datum.Datum import Datum
from ds.datum_set.Datumset import Datumset
from ds.thing.concept.District import District
from ds.thing.concept.Int import Int
from ds.thing.concept.Religion import Religion
from ds.thing.concept.Time import Time
from ds.thing.entity.House import House
from ds.thing.entity.Person import Person


class LankaDataDBMixin:
    @classmethod
    def list(cls) -> list[Datumset]:
        return [
            Datumset(
                Datum(
                    Person,
                    Time("2012"),
                    district=District["LK-11"],
                    religion=Religion["Buddhist"],
                    n=Int(88),
                ),
                Datum(
                    Person,
                    Time("2024"),
                    district=District["LK-11"],
                    religion=Religion["Buddhist"],
                    n=Int(100),
                ),
                Datum(
                    House,
                    Time("2024"),
                    district=District["LK-12"],
                    religion=Religion["Buddhist"],
                    n=Int(200),
                ),
                Datum(
                    Person,
                    Time("2024"),
                    district=District["LK-12"],
                    religion=Religion["Hindu"],
                    n=Int(150),
                ),
                Datum(
                    Person,
                    Time("2024"),
                    district=District["LK-12"],
                    n=Int(150),
                ),
            ),
            Datumset(
                Datum(
                    House,
                    Time("2012"),
                    district=District["LK-11"],
                    religion=Religion["Buddhist"],
                    n=Int(88),
                ),
            ),
        ]
