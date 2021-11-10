from typing import final
import unittest
import trip

class BoundaryValueTestTrip(unittest.TestCase):
    booking_time_max = 23
    booking_time_min = 1
    booking_time_nom = 12
    booking_time_max_minus = 22
    booking_time_min_plus = 2
    passenger_max = 7
    passenger_min = 1
    passenger_nom = 4
    passenger_max_minus = 6
    passenger_min_plus = 2

    def test1(self):
        assert(trip.get_start_time(self.booking_time_nom, self.passenger_nom) == 12)

    def test2(self):
        assert(trip.get_start_time(self.booking_time_nom, self.passenger_min) == 12)

    def test3(self):
        assert(trip.get_start_time(self.booking_time_nom, self.passenger_min_plus) == 12)

    def test4(self):
        assert(trip.get_start_time(self.booking_time_nom, self.passenger_max_minus) == 14)

    def test5(self):
        assert(trip.get_start_time(self.booking_time_nom, self.passenger_max) == 14)

    def test6(self):
        assert(trip.get_start_time(self.booking_time_min, self.passenger_nom) == 8)

    def test7(self):
        assert(trip.get_start_time(self.booking_time_min_plus, self.passenger_nom) == 8)

    def test8(self):
        assert(trip.get_start_time(self.booking_time_max_minus, self.passenger_nom) == 8)

    def test9(self):
        assert(trip.get_start_time(self.booking_time_max, self.passenger_nom) == 8)
    

class EquivalenceClassTestTrip(unittest.TestCase):
    booking_time_1 = 1
    booking_time_2 = 9
    booking_time_3 = 11
    booking_time_4 = 13
    booking_time_5 = 15
    booking_time_6 = 17
    
    number_passenger_1 = 2
    number_passenger_2 = 6

    def test1(self):
        assert(trip.get_start_time(self.booking_time_1, self.number_passenger_1) == 8)

    def test2(self):
        assert(trip.get_start_time(self.booking_time_2, self.number_passenger_1) == 12)
    
    def test3(self):
        assert(trip.get_start_time(self.booking_time_3, self.number_passenger_1) == 12)

    def test4(self):
        assert(trip.get_start_time(self.booking_time_4, self.number_passenger_1) == 16)

    def test5(self):
        assert(trip.get_start_time(self.booking_time_5, self.number_passenger_1) == 16)

    def test6(self):
        assert(trip.get_start_time(self.booking_time_6, self.number_passenger_1) == 8)

    def test7(self):
        assert(trip.get_start_time(self.booking_time_1, self.number_passenger_2) == 10)

    def test8(self):
        assert(trip.get_start_time(self.booking_time_2, self.number_passenger_2) == 10)

    def test9(self):
        assert(trip.get_start_time(self.booking_time_3, self.number_passenger_2) == 14)

    def test10(self):
        assert(trip.get_start_time(self.booking_time_4, self.number_passenger_2) == 14)

    def test11(self):
        assert(trip.get_start_time(self.booking_time_5, self.number_passenger_2) == 18)

    def test12(self):
        assert(trip.get_start_time(self.booking_time_6, self.number_passenger_2) == 18)

if __name__ == '__main__':
    unittest.main()
