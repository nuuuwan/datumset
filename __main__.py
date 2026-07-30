import sys

from ds import VisualLankaData

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m ds <visual_query_str>")
        sys.exit(1)
    visual_query_str = sys.argv[1]
    VisualLankaData[visual_query_str].open("code")
