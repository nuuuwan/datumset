from ds.lanka_data.LankaDataDBMixin import LankaDataDBMixin
from ds.query.Query import Query


class LankaData(LankaDataDBMixin):

    @classmethod
    def __class_getitem__(cls, query_str):
        query = Query(query_str)
        for datumset in cls.list():
            partially_matching_datumset = datumset.is_match(query)
            if partially_matching_datumset:
                infered_query = partially_matching_datumset.query
                assert infered_query == query
                return partially_matching_datumset

        raise ValueError(f'No matching Datumset found for label: "{query}"')
