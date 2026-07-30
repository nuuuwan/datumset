from ds.thing.entity_class_list.EntityClassListAtomMixin import EntityClassListAtomMixin
from ds.thing.entity_class_list.EntityClassListCensusMixin import EntityClassListCensusMixin
from ds.thing.entity_class_list.EntityClassListConceptMixin import EntityClassListConceptMixin
from ds.thing.entity_class_list.EntityClassListElectionMixin import EntityClassListElectionMixin
from ds.thing.entity_class_list.EntityClassListEntityMixin import EntityClassListEntityMixin
from ds.thing.entity_class_list.EntityClassListGovernmentMixin import EntityClassListGovernmentMixin
from ds.thing.entity_class_list.EntityClassListHouseholdMixin import EntityClassListHouseholdMixin
from ds.thing.entity_class_list.EntityClassListPersonMixin import EntityClassListPersonMixin
from ds.thing.entity_class_list.EntityClassListRegionMixin import EntityClassListRegionMixin
from ds.thing.entity_class_list.EntityClassListTimeMixin import EntityClassListTimeMixin


class ThingFactoryEntityClassListMixin:
    ENTITY_CLASS_LIST = (
        EntityClassListAtomMixin.ENTITY_CLASS_LIST
        + EntityClassListCensusMixin.ENTITY_CLASS_LIST
        + EntityClassListConceptMixin.ENTITY_CLASS_LIST
        + EntityClassListElectionMixin.ENTITY_CLASS_LIST
        + EntityClassListEntityMixin.ENTITY_CLASS_LIST
        + EntityClassListGovernmentMixin.ENTITY_CLASS_LIST
        + EntityClassListHouseholdMixin.ENTITY_CLASS_LIST
        + EntityClassListPersonMixin.ENTITY_CLASS_LIST
        + EntityClassListRegionMixin.ENTITY_CLASS_LIST
        + EntityClassListTimeMixin.ENTITY_CLASS_LIST
    )
