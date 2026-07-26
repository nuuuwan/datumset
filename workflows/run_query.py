import json
import sys

from utils_future import Log

from ds import LankaData

log = Log("run_query")

if __name__ == "__main__":
    query_str = (
        sys.argv[1]
        if len(sys.argv) > 1
        else "Person/Time*Country*Religion/Count"
    )
    log.debug(f"{query_str=}")
    ds = LankaData[query_str]
    print(json.dumps(ds.to_data(), indent=2))
