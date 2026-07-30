import cProfile
import pstats
import sys

from ds import VisualLankaData

DEFAULT_VISUAL_QUERY_STR = (
    "Vote"
    + "/ElectionType=Presidential_Time=2015_PD<ED=colombo_Party"
    + "/Count"
    + "/MekkoChart"
)

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()

    visual_query_str = (
        sys.argv[1] if len(sys.argv) > 1 else DEFAULT_VISUAL_QUERY_STR
    )
    VisualLankaData[visual_query_str].open("code")

    profiler.disable()
    profile_path = "tests/_profile_lankadata.prof"
    profiler.dump_stats(profile_path)

    p = pstats.Stats(profile_path)

    p.sort_stats("tottime").print_stats(10)
