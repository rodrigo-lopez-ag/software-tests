import unittest
import datetime
import sys
import io
from hotel_management.reservation import Reservation
from hotel_management.hotel import Hotel
from hotel_management.customer import Customer

class TestReservation(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel()
        self.hotel.create_hotel('PV', 4.3, 100, 'Mexico')
        self.customer1 = Customer()
        self.customer1.create_customer('Rodrigo', 'Lopez', 27, datetime.datetime(2024, 5, 7), datetime.datetime(2024, 5, 14))
        self.customer2 = Customer()
        self.customer2.create_customer('Antonio', 'Medina', 25, datetime.datetime(2024, 5, 7), datetime.datetime(2024, 5, 14))
        self.customers_list = [self.customer1, self.customer2]
        self.reservation = Reservation()
        self.reservation.create_reservation(self.customers_list, self.hotel)
    
    def test_create_reservation(self):
        hotel_name = self.reservation.hotel.name
        expected = 'PV'
        self.assertEqual(expected, hotel_name)
    
    def test_cancel_reservation(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        # self.customer.create_customer('Rodrigo', 'Lopez', 27, datetime.datetime(2024, 5, 7), datetime.datetime(2024, 5, 2))
        self.reservation.cancel_reservation(self.customer1, self.hotel)
        sys.stdout = sys.__stdout__
        expected = "Canceling reservation for Rodrigo\n"
        actual = capturedOutput.getvalue()
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
