from ds.thing.concept.region.Region import Region


class District(Region):

    @classmethod
    def list(cls):
        return super().list() + [
            cls(id="LK-12-Negombo", name="Negombo"),
            cls(id="LK-62-Chilaw", name="Chilaw"),
        ]
