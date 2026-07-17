from ds import LankaData

if __name__ == "__main__":
    for query_str in [
        "Person/Time*District*Religion/Count",
        "Person/Time*Province*Religion/Count",
        "Person/Time*ED*Religion/Count",
        "Person/Time*PD*Religion/Count",
    ]:
        LankaData[query_str]
