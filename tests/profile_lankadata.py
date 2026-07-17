import cProfile
import pstats

from ds import LankaData

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()

    for query_str in [
        "Person/Time*District*Religion/Count",
        "Person/Time*Province*Religion/Count",
        "Person/Time*ED*Religion/Count",
        "Person/Time*PD*Religion/Count",
    ]:
        LankaData[query_str]

    profiler.disable()
    profile_path = "tests/profile_lankadata.prof"
    profiler.dump_stats(profile_path)

    p = pstats.Stats(profile_path)

    p.sort_stats("tottime").print_stats(20)
