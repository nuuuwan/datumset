from functools import cached_property


class String:
    def __init__(self, s: str):
        self.s = s

    @cached_property
    def cleaned_s(self) -> str:
        return self.s.strip().replace(",", "").replace(" ", "_").lower()

    @cached_property
    def pascal(self) -> str:
        return "".join(word.capitalize() for word in self.s.split("_"))

    @cached_property
    def int(self) -> int:
        try:
            return int(float(self.cleaned_s))
        except ValueError:
            return None
