from ds.thing.concept.census.CensusOfficer import CensusOfficer
from ds.thing.concept.census.CensusTopic import CensusTopic


class EntityClassListCensusMixin:
    ENTITY_CLASS_LIST = [
        CensusOfficer,
        CensusTopic,
    ]
