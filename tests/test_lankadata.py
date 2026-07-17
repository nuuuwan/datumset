import time
import unittest

from ds import Datumset, LankaData


class TestCase(unittest.TestCase):

    def test_valid(self):
        for query_str in [
            "Person/Time*Country*Religion/Count",
            "Person/Time*Province*Religion/Count",
            "Person/Time*District*Religion/Count",
            "Person/Time*ED*Religion/Count",
            "Person/Time*PD*Religion/Count",
            "Person/Time*LG*Religion/Count",
            "Person/Time*District*Ethnicity/Count",
            "Person/Time*District*HighestEducationLevel/Count",
            "Person/Time*District*IsEconomicallyActive/Count",
            "Person/Time*District*AgeGroup/Count",
            "Person/Time*District*Gender/Count",
            "Person/Time*District*MaritalStatus/Count",
            "House/Time*District*CookingFuel/Count",
            "House/Time*District*FloorType/Count",
            "House/Time*District*Lighting/Count",
            "House/Time*District*RoofType/Count",
            "House/Time*District*ToiletFacilities/Count",
            "House/Time*District*WallType/Count",
            "House/Time*District*HouseholdStructure/Count",
            "House/Time*District*OccupationStatus/Count",
            "House/Time*District*OwnershipStatus/Count",
            "House/Time*District*LivingQuarters/Count",
            "House/Time*District*SourceOfDrinkingWater/Count",
            "House/Time*District*SolidWasteDisposal/Count",
            "House/Time*District*TypeOfUnit/Count",
        ]:
            ds1 = LankaData[query_str]
            ds2 = Datumset.from_data(ds1.to_data())
            self.assertEqual(ds1, ds2)

    def test_performance(self):
        for query_str in [
            "Person/Time*District*Religion/Count",
            "Person/Time*Province*Religion/Count",
            "Person/Time*ED*Religion/Count",
            "Person/Time*PD*Religion/Count",
        ]:
            t0 = time.time()
            datumset = LankaData[query_str]
            self.assertIsNotNone(datumset)
            elapsed_ms = (time.time() - t0) * 1000.0
            MAX_T_MS = 100.0
            self.assertLess(
                elapsed_ms,
                MAX_T_MS,
                f"{query_str} took {elapsed_ms:.2f}ms > {MAX_T_MS}ms",
            )

    def test_invalid(self):
        for query_str in [
            "Person/Time*GND*Religion1/Count",
            "Person/Time*DSD*Ethnicity1/Count",
        ]:
            with self.assertRaises(ValueError):
                LankaData[query_str]
