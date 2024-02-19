import unittest
import datetime
import io
import sys
from hotel_management.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer()
        self.customer.create_customer('Rodrigo', 'Lopez', 27, datetime.datetime(2024, 5, 7), datetime.datetime(2024, 5, 14))
    
    def test_create_customer(self):
        self.assertEqual('Rodrigo', self.customer.name)
        self.assertEqual('Lopez', self.customer.last_name)
        self.assertEqual(27, self.customer.age)
        self.assertEqual('07-05-2024', self.customer.date_of_arrival.strftime("%d-%m-%Y"))
        self.assertEqual('14-05-2024', self.customer.date_of_departure.strftime("%d-%m-%Y"))
    
    def test_create_customer_negative_age(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.customer.create_customer('Rodrigo', 'Lopez', -10, datetime.datetime(2024, 5, 7), datetime.datetime(2024, 5, 14))
        sys.stdout = sys.__stdout__
        expected = "Age must be a valid value\n"
        actual = capturedOutput.getvalue()
        self.assertEqual(expected, actual)

    def test_create_customer_wrong_arrival_date(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.customer.create_customer('Rodrigo', 'Lopez', 27, datetime.datetime(2023, 5, 7), datetime.datetime(2024, 5, 14))
        sys.stdout = sys.__stdout__
        expected = "The day of arrival must be a valid date from today onwards\n"
        actual = capturedOutput.getvalue()
        self.assertEqual(expected, actual)
    
    def test_create_customer_wrong_departure_date(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.customer.create_customer('Rodrigo', 'Lopez', 27, datetime.datetime(2024, 5, 7), datetime.datetime(2024, 5, 2))
        sys.stdout = sys.__stdout__
        expected = "Invalid date, must be a date equal or after day of arrival\n"
        actual = capturedOutput.getvalue()
        self.assertEqual(expected, actual)
    
    def test_display_customer(self):
        expected = (f"Name: {self.customer.name}\tLast name: {self.customer.last_name}\t"
                    f"Age: {self.customer.age}\t"
                    f"Date of arrival: {self.customer.date_of_arrival}\t"
                    f"Date of departure: {self.customer.date_of_departure}")
        self.assertEqual(expected, self.customer.display_customer_information())
    
    def test_modify_customer(self):
        self.customer.modify_customer_information('Antonio', 'Medina', 25, datetime.datetime(2024, 5, 7), datetime.datetime(2024, 5, 14))
        self.assertEqual('Antonio', self.customer.name)
        self.assertEqual('Medina', self.customer.last_name)
        self.assertEqual(25, self.customer.age)
    
    def test_delete_customer(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.customer.delete_customer(self.customer.name, self.customer.last_name)
        sys.stdout = sys.__stdout__
        expected = f"File of customer {self.customer.name} {self.customer.last_name} has been removed\n"
        actual = capturedOutput.getvalue()
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()