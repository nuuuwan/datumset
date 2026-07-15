from ds.lanka_data.LankaData import LankaData

if __name__ == '__main__':

    for query_str in [
        'Person/2012/Religion*District',
        'Person/2024/Religion*District',
        'Person/2024/District*Religion',
        'Person/2024/District',
        'Person/2024/Religion',
        'Person/2012+2024/Religion',
        'Person+House/2012+2024/Religion',
    ]:
        print(LankaData[query_str].to_str())
        print('-' * 32)
