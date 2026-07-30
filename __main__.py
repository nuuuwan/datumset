import sys

from utils_future import String

from ds import LankaData, VisualLankaData

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m ds <visual_query_str>")
        sys.exit(1)
    visual_query_str = sys.argv[1]
    tokens = visual_query_str.rsplit("/")

    if not (3 <= len(tokens) <= 4):
        print(
            f"Invalid query: {visual_query_str}"
            + " (must have exactly 3 or 4 tokens)"
        )
        sys.exit(1)

    query_str = "/".join(tokens[:3])
    datumset = LankaData[query_str]

    if len(tokens) == 3:
        print(String(datumset.to_data()).json)

    if len(tokens) == 4:
        VisualLankaData[visual_query_str].open("code")
