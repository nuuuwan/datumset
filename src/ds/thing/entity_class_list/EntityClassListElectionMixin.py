from ds.thing.concept.election.ElectionType import ElectionType
from ds.thing.concept.election.Party import Party
from ds.thing.concept.election.Summary import Summary


class EntityClassListElectionMixin:
    ENTITY_CLASS_LIST = [
        ElectionType,
        Party,
        Summary,
    ]
