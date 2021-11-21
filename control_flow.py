import unittest
import trip

class ControlFlowTestTrip(unittest.TestCase):
    
    def test1(self):
        assert(trip.get_start_time(24, 1) == -1)

    def test2(self):
        assert(trip.get_start_time(9, 3) == 12)

    def test3(self):
        assert(trip.get_start_time(13, 3) == 16)

    def test4(self):
        assert(trip.get_start_time(5, 3) == 8)

    def test5(self):
        assert(trip.get_start_time(13, 6) == 14)

    def test6(self):
        assert(trip.get_start_time(15, 6) == 18)

    def test7(self):
        assert(trip.get_start_time(20, 7) == 10)

if __name__ == '__main__':
    unittest.main()
