import unittest
import io
import sys
from hotel_management.hotel import Hotel

class TestHotel(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel()
        self.hotel.create_hotel('PV', 4.3, 100, 'Mexico')
    
    def test_create_hotel(self):
        self.hotel.create_hotel('PV', 4.3, 100, 'Mexico')
        self.assertEqual('PV', self.hotel.name)
        self.assertEqual(4.3, self.hotel.rating)
        self.assertEqual(100, self.hotel.total_rooms)
        self.assertEqual('Mexico', self.hotel.location)
    
    def test_create_hotel_negative_rooms(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.hotel.create_hotel('PV', 4.3, -1, 'Mexico')
        sys.stdout = sys.__stdout__
        expected = "The total number of rooms must be a value greater than 0\n"
        actual = capturedOutput.getvalue()
        self.assertEqual(expected, actual)
    
    def test_create_hotel_negative_rating(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.hotel.create_hotel('PV', -1, 100, 'Mexico')
        sys.stdout = sys.__stdout__
        expected = "Rating must be a valid value between 0 and 5\n"
        actual = capturedOutput.getvalue()
        self.assertEqual(expected, actual)
    
    def test_modify_hotel(self):
        self.hotel.modify_hotel_information('Malibu', 3.2, 200, 'USA')
        self.assertEqual('Malibu', self.hotel.name)
        self.assertEqual(3.2, self.hotel.rating)
        self.assertEqual(200, self.hotel.total_rooms)
        self.assertEqual('USA', self.hotel.location)
    
    def test_modify_hotel_cancel_all_reservations(self):
        self.hotel.modify_hotel_information('Malibu', 3.2, 200, 'USA', cancel_all_reservations=True)
        expected = 0
        actual = len([item for item in self.hotel.reserv.values() if item == True])
        self.assertEqual(expected, actual)
    
    def test_display_information(self):
        actual = self.hotel.display_hotel_information()
        expected = (f"Name: {self.hotel.name}\tRating: {self.hotel.rating}\t"
                f"Total rooms: {self.hotel.total_rooms}\tLocation: {self.hotel.location}\t"
                f"Rooms reserved: {len([item for item in self.hotel.reserv.values() if item == True])}")
        self.assertEqual(expected, actual)
    
    def test_reserve_room(self):
        self.hotel.reserve_room(10)
        self.hotel.reserve_room(14)
        self.hotel.reserve_room(15)
        self.assertEqual(True, self.hotel.reserv[10])
        self.assertEqual(True, self.hotel.reserv[14])
        self.assertEqual(True, self.hotel.reserv[15])
    
    def test_reserve_room_unexisten(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.hotel.reserve_room(1000)
        sys.stdout = sys.__stdout__
        expected = "The room number 1000 does not exist in the current hotel\n"
        actual = capturedOutput.getvalue()
        self.assertEqual(expected, actual)
    
    def test_free_room(self):
        self.hotel.reserve_room(14)
        self.hotel.free_room(14)
        self.assertEqual(False, self.hotel.reserv[14])

    def test_free_room_unexistant(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.hotel.free_room(1000)
        sys.stdout = sys.__stdout__
        expected = "The room number 1000 does not exist in the current hotel\n"
        actual = capturedOutput.getvalue()
        self.assertEqual(expected, actual)

    def test_destroy_hotel(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.hotel.destroy_hotel()
        sys.stdout = sys.__stdout__
        expected = f"File of hotel {self.hotel.name} was removed\n"
        actual = capturedOutput.getvalue()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()