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
                    District=District["LK-11"],
                    Religion=Religion["Buddhist"],
                    Count=Int(88),
                ),
                Datum(
                    Person,
                    Time("2024"),
                    District=District["LK-11"],
                    Religion=Religion["Buddhist"],
                    Count=Int(100),
                ),
                Datum(
                    House,
                    Time("2024"),
                    District=District["LK-12"],
                    Religion=Religion["Buddhist"],
                    Count=Int(200),
                ),
                Datum(
                    House,
                    Time("2012"),
                    District=District["LK-12"],
                    Religion=Religion["Buddhist"],
                    Count=Int(200),
                ),
                Datum(
                    Person,
                    Time("2024"),
                    District=District["LK-12"],
                    Religion=Religion["Hindu"],
                    Count=Int(150),
                ),
                Datum(
                    Person,
                    Time("2024"),
                    District=District["LK-12"],
                    Religion=Religion["Hindu"],
                    Count=Int(150),
                ),
            ),
            Datumset(
                Datum(
                    Person,
                    Time("2012"),
                    Religion=Religion["Buddhist"],
                    Count=Int(88),
                ),
            ),
        ]
