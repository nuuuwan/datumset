from ds.thing.entity.Census import Census
from ds.thing.entity.House import House
from ds.thing.entity.Person import Person
from ds.thing.entity.Vote import Vote


class EntityClassListEntityMixin:
    ENTITY_CLASS_LIST = [
        Census,
        House,
        Person,
        Vote,
    ]
