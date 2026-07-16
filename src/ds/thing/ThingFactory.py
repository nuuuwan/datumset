from ds.thing.concept.District import District
from ds.thing.concept.Int import Int
from ds.thing.concept.Religion import Religion
from ds.thing.concept.Time import Time
from ds.thing.entity.House import House
from ds.thing.entity.Person import Person


class ThingFactory:
    @classmethod
    def __class_getitem__(cls, class_name: str):
        entity_class = dict(
            Religion=Religion,
            District=District,
            Person=Person,
            House=House,
            Int=Int,
            Time=Time,
        ).get(class_name)

        if not entity_class:
            raise ValueError(
                f"[ThingFactory] Unknown class_name: {class_name}"
            )
        return entity_class

    @classmethod
    def from_value(cls, data):
        class_name, value = data.split(":", 1)
        cls_for_name = ThingFactory[class_name]
        inst = cls_for_name.from_data(value)
        return inst
