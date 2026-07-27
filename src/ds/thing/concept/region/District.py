from ds.thing.concept.region.Region import Region


class District(Region):

    @classmethod
    def list(cls):
        return super().list() + [
            cls("Negombo"),
            cls("Chilaw"),
        ]
