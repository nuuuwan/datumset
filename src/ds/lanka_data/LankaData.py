from ds.datum.Datum import Datum
from ds.datum_set.Datumset import Datumset
from ds.datum_set.MatchedDatumset import MatchedDatumset
from ds.measurement.District import District
from ds.measurement.House import House
from ds.measurement.Int import Int
from ds.measurement.Person import Person
from ds.measurement.Religion import Religion
from ds.measurement.Time import Time
from ds.query.Query import Query


class LankaData:
    @classmethod
    def list(cls) -> list[Datumset]:
        return [
            Datumset(
                Datum(
                    Person,
                    Time("2012"),
                    district=District['LK-11'],
                    religion=Religion['Buddhist'],
                    n=Int(88),
                ),
                Datum(
                    Person,
                    Time("2024"),
                    district=District['LK-11'],
                    religion=Religion['Buddhist'],
                    n=Int(100),
                ),
                Datum(
                    House,
                    Time("2024"),
                    district=District['LK-12'],
                    religion=Religion['Buddhist'],
                    n=Int(200),
                ),
                Datum(
                    Person,
                    Time("2024"),
                    district=District['LK-12'],
                    religion=Religion['Hindu'],
                    n=Int(150),
                ),
            )
        ]

    @classmethod
    def __class_getitem__(cls, query_str):
        query = Query(query_str)
        for datumset in cls.list():
            match_info = datumset.is_match(query)
            if match_info:
                matching_datumset, match = match_info
                return MatchedDatumset(query, matching_datumset, match)
        raise ValueError(f"No matching Datumset found for label: \"{query}\"")


if __name__ == '__main__':
    for query_str in [
        'Person/2012/Religion*District',
        'Person/2024/Religion*District',
        'Person/2024/District*Religion',
        'Person/2024/District',
        'Person/2024/Religion',
        'Person/2012+2024/Religion',
        'Person+House/2012+2024/Religion',
    ]:
        print(LankaData[query_str].to_str())
        print('-' * 32)
