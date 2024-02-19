"""Class abstraction of a Customer"""
import datetime
import json
import os


class Customer:
    """Class abstraction of a Customer"""
    def __init__(self) -> None:
        self.name = ""
        self.last_name = ""
        self.age = 0
        self.date_of_arrival = None
        self.date_of_departure = None

    def create_customer(self, name: str, last_name: str, age: int,
                        date_of_arrival: datetime.datetime,
                        date_of_departure: datetime.datetime) -> None:
        """Creates a json file of the information of the customer"""
        self.name = name
        self.last_name = last_name
        if age > 0:
            self.age = age
        else:
            print("Age must be a valid value")
        if date_of_arrival > datetime.datetime.now():
            self.date_of_arrival = date_of_arrival
        else:
            print("The day of arrival must be a valid date from today onwards")
        if date_of_departure >= date_of_arrival:
            self.date_of_departure = date_of_departure
        else:
            print("Invalid date, must be a date equal or after day of arrival")
        json_dump = {
            'customer': {
                'name': self.name,
                'lastName': self.last_name,
                'age': self.age,
                'dateArrival': self.date_of_arrival.strftime("%d-%m-%Y"),
                'dateDeparture': self.date_of_departure.strftime("%d-%m-%Y")
            }
        }
        with open(name + last_name + '_customer.json', 'w',
                  encoding='utf-8') as outfile:
            outfile.write(json.dumps(json_dump, indent=2))

    def delete_customer(self, name: str, last_name: str) -> None:
        """Deletes the json file of the given customer if it exists"""
        file_to_del = os.getcwd() + '/' + name + last_name + '_customer.json'
        if os.path.isfile(file_to_del) and os.path.exists(file_to_del):
            os.remove(file_to_del)
            print(f"File of customer {name} {last_name} has been removed")
        else:
            print(f"File of customer {name} {last_name} does not exists")

    def display_customer_information(self) -> str:
        """Displays the information of the customer"""
        return (f"Name: {self.name}\tLast name: {self.last_name}\t"
                f"Age: {self.age}\t"
                f"Date of arrival: {self.date_of_arrival}\t"
                f"Date of departure: {self.date_of_departure}")

    def modify_customer_information(self, name: str, last_name: str, age: int,
                                    date_of_arrival: datetime.datetime,
                                    date_of_departure:
                                    datetime.datetime) -> None:
        """Modifies the json file with the new customer information"""
        file_to_del = os.getcwd() + '/' + self.name + \
            self.last_name + '_customer.json'
        os.remove(file_to_del)
        print(f"File of customer {self.name} {self.last_name} has been"
              f"changed to the data of {name} {last_name}")
        self.create_customer(name, last_name, age, date_of_arrival,
                             date_of_departure)
