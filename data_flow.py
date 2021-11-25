import unittest
import trip

class DataFlowTestTrip(unittest.TestCase):
    
    def test1(self):
        assert(trip.get_start_time(25, 4) == -1)

    def test2(self):
        assert(trip.get_start_time(10, 3) == 12)

    def test3(self):
        assert(trip.get_start_time(13, 3) == 16)

    def test4(self):
        assert(trip.get_start_time(20, 3) == 8)

    def test5(self):
        assert(trip.get_start_time(11,7) == 14)

    def test6(self):
        assert(trip.get_start_time(15, 7) == 18)

    def test7(self):
        assert(trip.get_start_time(20, 7) == 10)

if __name__ == '__main__':
    unittest.main()
