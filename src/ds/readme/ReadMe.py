from functools import cached_property

from utils_future import File, JSONFile, Log

log = Log("ReadMe")


class ReadMe:
    @cached_property
    def readme_file(self):
        return File("README.md")

    def get_lines_for_header(self):
        return [
            "# Lanka Data",
            "",
            "This repository contains data related to Sri Lanka.",
            "",
        ]

    def get_lines_for_query(self, i_query, query_str):
        image_file = File("images", query_str + ".png")

        return [
            f"### {i_query}",
            "",
            "```text",
            query_str,
            "```",
            "",
            f"![{image_file.path}]({image_file.path})",
            "",
        ]

    def get_lines_for_examples(self):
        query_strs = JSONFile(
            "tests", "test_visual_lankadata.data.json"
        ).read()
        lines = ["## Examples", ""]
        for i_query, query_str in enumerate(query_strs, start=1):
            lines.extend(self.get_lines_for_query(i_query, query_str))
        return lines

    def get_lines(self):
        return self.get_lines_for_header() + self.get_lines_for_examples()

    def build(self):
        lines = self.get_lines()
        self.readme_file.write("\n".join(lines))
        log.info(f"Wrote {len(lines)} lines to {self.readme_file}")
