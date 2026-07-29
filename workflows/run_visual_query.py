import sys

from utils_future import Log

from ds import VisualLankaData

log = Log("run_query")

if __name__ == "__main__":
    visual_query_str = (
        sys.argv[1]
        if len(sys.argv) > 1
        else "Person/Time=2024*Province*Religion/Count/MarimekkoChart"
    )
    log.debug(f"{visual_query_str=}")
    VisualLankaData[visual_query_str].open("code")
