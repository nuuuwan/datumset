from functools import cached_property


class String:
    def __init__(self, s: str):
        self.s = s

    @cached_property
    def cleaned_s(self) -> str:
        return self.s.strip().replace(",", "").replace(" ", "_").lower()

    @cached_property
    def pascal(self) -> str:
        s = self.s

        s = s.replace(" - ", "_to_")

        if "years" in s:
            if s[2:3] == "_":
                s = s[0:2] + "_to_" + s[3:]
            s = s.replace("_to_or_", "_or_")

        s = s.replace("&", "_and_")
        s = s.replace("/", "_or_")
        s = s.replace(".", "_")
        s = s.replace(",", "_")
        s = s.replace(" ", "_")
        s = s.replace("-", "_")
        s = "".join(c if c.isalnum() else "_" for c in s)

        return "".join(word.capitalize() for word in s.split("_"))

    @cached_property
    def int(self) -> int:
        try:
            return int(float(self.cleaned_s))
        except ValueError:
            return None
