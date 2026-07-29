import cProfile
import pstats

from ds import VisualLankaData

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()

    visual_query_str = "Vote/ElectionType=Parliamentary*Time=2024*PD<ED=colombo*Party/Count/MarimekkoChart"
    VisualLankaData[visual_query_str].open("code")

    profiler.disable()
    profile_path = "tests/_profile_lankadata.prof"
    profiler.dump_stats(profile_path)

    p = pstats.Stats(profile_path)

    p.sort_stats("tottime").print_stats(10)
