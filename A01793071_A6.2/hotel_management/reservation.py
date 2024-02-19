"""Class abstraction of a Reservation"""
import json
from hotel_management.customer import Customer
from hotel_management.hotel import Hotel


class Reservation:
    """Class abstraction of a Reservation"""
    def __init__(self) -> None:
        self.customer = []
        self.hotel = None

    def create_reservation(self, customers: list[Customer],
                           hotel: Hotel) -> None:
        """Creates a json file given the hotel and customers information"""
        print(f"Making reservation in hotel {hotel.name}")
        for c in customers:
            print(f"For customer: {c.name}")
        self.customer = customers
        self.hotel = hotel
        json_dump = {
            'reservation': {
                'customers': [],
                'hotel': None
            }
        }
        for c in customers:
            json_dump['reservation']['customers'].append(
                {
                    'name': c.name,
                    'lastName': c.last_name,
                    'age': c.age,
                    'dateArrival': c.date_of_arrival.strftime("%d-%m-%Y"),
                    'dateDeparture': c.date_of_departure.strftime("%d-%m-%Y")
                }
            )
        json_dump['reservation']['hotel'] = {
            'name': hotel.name,
            'rating': hotel.rating,
            'location': hotel.location,
            'total_rooms': hotel.total_rooms,
            'reserved_rooms': hotel.reserv
        }
        with open(hotel.name + '_reservations.json', 'w',
                  encoding='utf-8') as outfile:
            outfile.write(json.dumps(json_dump, indent=2))

    def cancel_reservation(self, customer: Customer, hotel: Hotel) -> None:
        """Cancels a reservation given a hotel and a customer"""
        json_dump = {}
        with open(hotel.name + '_reservations.json', 'r',
                  encoding='utf-8') as outfile:
            json_dump = json.load(outfile)
        if json_dump['reservation']['hotel']['name'] == hotel.name:
            for index, c in enumerate(json_dump['reservation']['customers']):
                if c['name'] == customer.name:
                    print(f"Canceling reservation for {customer.name}")
                    del json_dump['reservation']['customers'][index]
                    break
            with open(hotel.name + '_reservations.json', 'w',
                      encoding='utf-8') as outfile_write:
                outfile_write.write(json.dumps(json_dump, indent=2))
        else:
            print(f"The hotel with name {hotel.name} does not exists")
