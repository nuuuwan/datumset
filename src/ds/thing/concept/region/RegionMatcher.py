from utils_future import String


class RegionMatcher:
    # DSD<District:colombo

    @classmethod
    def get_child_regions(cls, parent_region, child_region_class):
        parent_ent = parent_region.get_ent()
        child_region_ents = child_region_class.get_ents()

        matching_child_values = []
        parent_id = parent_ent["id"]
        for child_region_ent in child_region_ents:
            child_id = child_region_ent["id"]
            if parent_id in child_id:
                matching_child_values.append(
                    String(child_region_ent["name"]).snake
                )

        if not matching_child_values:
            raise ValueError(
                f"No child regions of type {child_region_class}"
                + f" found for parent region: {parent_region}"
            )

        return [child_region_class(value) for value in matching_child_values]
