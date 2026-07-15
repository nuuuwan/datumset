from ds.measurement.Region import Region


class District(Region):
    @classmethod
    def list(cls):
        return [
            cls(id="LK-11", name="Colombo"),
            cls(id="LK-12", name="Gampaha"),
        ]
