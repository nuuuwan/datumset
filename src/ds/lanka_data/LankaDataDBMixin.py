from ds.datum.Datum import Datum
from ds.datumset.Datumset import Datumset
from ds.thing.concept.Int import Int
from ds.thing.concept.region.District import District
from ds.thing.concept.Religion import Religion
from ds.thing.concept.Time import Time
from ds.thing.entity.Person import Person


class LankaDataDBMixin:
    @classmethod
    def list(cls) -> list[Datumset]:
        return [
            Datumset(
                Datum(
                    Person,
                    dict(
                        Time=Time("2012"),
                        District=District["LK-11"],
                        Religion=Religion["Buddhist"],
                    ),
                    dict(Count=Int(88)),
                ),
                Datum(
                    Person,
                    dict(
                        Time=Time("2012"),
                        District=District["LK-11"],
                        Religion=Religion["Hindu"],
                    ),
                    dict(Count=Int(44)),
                ),
                Datum(
                    Person,
                    dict(
                        Time=Time("2012"),
                        District=District["LK-12"],
                        Religion=Religion["Buddhist"],
                    ),
                    dict(Count=Int(121)),
                ),
                Datum(
                    Person,
                    dict(
                        Time=Time("2012"),
                        District=District["LK-12"],
                        Religion=Religion["Hindu"],
                    ),
                    dict(Count=Int(12)),
                ),
            ),
        ]
