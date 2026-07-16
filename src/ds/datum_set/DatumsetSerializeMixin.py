import json

from propcache import cached_property

from ds.datum.Datum import Datum
from utils_future import Directory, JSONFile, Log

log = Log("DatumsetSerializeMixin")


class DatumsetSerializeMixin:
    @cached_property
    def dir_data(self):
        dir_data = Directory("data", self.query.query_str)
        dir_data.make()
        return dir_data

    @cached_property
    def data_file(self):
        return JSONFile(self.dir_data.path, "data.json")

    def to_data(self):
        arr = [datum.to_data() for datum in self._value]
        idx = {}
        for data in arr:
            entity_class_name = list(data.keys())[0]
            entity_data = data[entity_class_name]
            time_value = list(entity_data.keys())[0]
            time_data = entity_data[time_value]

            if entity_class_name not in idx:
                idx[entity_class_name] = {}
            if time_value not in idx[entity_class_name]:
                idx[entity_class_name][time_value] = []
            idx[entity_class_name][time_value].append(time_data)

        sorted_idx = {}
        for entity_class_name, entity_data in idx.items():
            sorted_idx[entity_class_name] = dict(
                sorted(entity_data.items(), key=lambda x: x[0])
            )
        sorted_sorted_idx = dict(
            sorted(sorted_idx.items(), key=lambda x: x[0])
        )

        return sorted_sorted_idx

    @classmethod
    def from_data(cls, data):
        datum_list = []
        for entity_class_name, entity_data in data.items():
            for time_value, time_data in entity_data.items():
                for time_data_item in time_data:
                    datum = Datum.from_attributes(
                        entity_class_name, time_value, time_data_item
                    )
                    datum_list.append(datum)

        return cls(*datum_list)

    def to_file(self):
        self.data_file.write(self.to_data())
        log.info(f"Wrote {self.data_file}")

    def to_str(self):
        return json.dumps(self.to_data(), indent=4)

    @classmethod
    def from_str(cls, data_str):
        data = json.loads(data_str)
        return cls.from_data(data)
