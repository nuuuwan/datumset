from ds.datum_set.MatchedDatumset import MatchedDatumset
from ds.lanka_data.LankaDataDBMixin import LankaDataDBMixin
from ds.query.Query import Query


class LankaData(LankaDataDBMixin):

    @classmethod
    def __class_getitem__(cls, query_str):
        query = Query(query_str).normalize()
        for datumset in cls.list():
            partially_matching_datumset = datumset.is_match(query)
            if partially_matching_datumset:
                infered_query = partially_matching_datumset.infer_query()
                if infered_query == query:
                    matched_datumset = MatchedDatumset(
                        query, partially_matching_datumset
                    )
                    matched_datumset.to_file()
                    return matched_datumset
        raise ValueError(f'No matching Datumset found for label: "{query}"')
