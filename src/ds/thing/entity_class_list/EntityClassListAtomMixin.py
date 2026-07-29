from ds.thing.concept.atom.Bool import Bool
from ds.thing.concept.atom.Float import Float
from ds.thing.concept.atom.Int import Int
from ds.thing.concept.atom.Percent import Percent


class EntityClassListAtomMixin:
    ENTITY_CLASS_LIST = [
        Bool,
        Float,
        Int,
        Percent,
    ]
