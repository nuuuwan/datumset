import unittest

from ds import MatchedDatumset, LankaData,Query
class TestCase(unittest.TestCase):
    def test_basic(self):
        for query_str in [
            'Person/2012/Religion*District',
            'Person/2024/Religion*District',
            'Person/2024/District*Religion',
            'Person/2024/District',
            'Person/2024/Religion',
            'Person/2012+2024/Religion',
            'Person+House/2012+2024/Religion',
            'House+Person/2012+2024/Religion',
        ]:
            print('=' * 32)
            print(query_str)
            print('=' * 32)
            
            mds1 =  LankaData[query_str]
            s1 =mds1.to_str()
            print(s1)
            print('-' * 32)

            mds2 = MatchedDatumset.from_str(s1)
            print(mds2)
            print('-' * 32)


            print(mds2.query.query_str)
            print('-' * 32)
            
            self.assertEqual(mds2.query, Query(query_str))
            print('-' * 32)
