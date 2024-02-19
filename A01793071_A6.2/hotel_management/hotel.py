"""Class abstraction of a Hotel"""
import json
import os


class Hotel:
    """Class abstraction of a Hotel"""
    def __init__(self) -> None:
        self.name = ""
        self.rating = 0
        self.total_rooms = 0
        self.location = ""
        self.reserv = {}

    def create_hotel(self, name: str, rating: float, total_rooms: int,
                     location: str) -> None:
        """Saves the hotel information to a json and the present object"""
        self.name = name
        if 0 < rating <= 5:
            self.rating = rating
        else:
            print("Rating must be a valid value between 0 and 5")
            return
        if total_rooms > 0:
            self.total_rooms = total_rooms
        else:
            print("The total number of rooms must be a value greater than 0")
            return
        self.location = location
        rooms = list(range(1, total_rooms + 1))
        self.reserv = {rooms[i]: False for i in range(len(rooms))}
        json_dump = {
            'hotel': {
                'name': self.name,
                'rating': self.rating,
                'location': self.location,
                'total_rooms': self.total_rooms,
                'reserved_rooms': self.reserv
            }
        }
        with open(name + '_hotel.json', 'w', encoding='utf-8') as outfile:
            outfile.write(json.dumps(json_dump, indent=2))

    def destroy_hotel(self):
        """Deletes the hotel file json if there is one"""
        file_to_del = os.getcwd() + '/' + self.name + '_hotel.json'
        if os.path.isfile(file_to_del) and os.path.exists(file_to_del):
            os.remove(file_to_del)
            print(f"File of hotel {self.name} was removed")
        else:
            print(f"The file regarding the hotel {self.name} does not exists")

    def modify_hotel_information(self, name: str, rating: float,
                                 total_rooms: int, location: str,
                                 cancel_all_reservations=False) -> None:
        """Modifies the object with the new hotel information and json file"""
        file_to_del = os.getcwd() + '/' + self.name + '_hotel.json'
        os.remove(file_to_del)
        print(f"File of hotel {self.name} was changed to {name}")
        self.name = name
        if 0 < rating <= 5:
            self.rating = rating
        else:
            print("Rating must be a valid value between 0 and 5")
        if total_rooms > 0:
            self.total_rooms = total_rooms
        else:
            print("The total number of rooms must be a value greater than 0")
        self.location = location
        if cancel_all_reservations:
            rooms = list(range(1, total_rooms + 1))
            self.reserv = {rooms[i]: False for i in range(len(rooms))}
        json_dump = {
            'hotel': {
                'name': self.name,
                'rating': self.rating,
                'location': self.location,
                'total_rooms': self.total_rooms,
                'reserved_rooms': self.reserv
            }
        }
        with open(name + '_hotel.json', 'w', encoding='utf-8') as outfile:
            outfile.write(json.dumps(json_dump, indent=2))

    def display_hotel_information(self) -> str:
        """Displays the hotel information"""
        return (f"Name: {self.name}\tRating: {self.rating}\t"
                f"Total rooms: {self.total_rooms}\tLocation: {self.location}\t"
                f"Rooms reserved: {list(self.reserv.values()).count(True)}")

    def reserve_room(self, room: int) -> None:
        """Reserves a room for the hotel"""
        # if room > 0 and room < len(self.reserv) + 1:
        if 0 < room < len(self.reserv) + 1:
            self.reserv[room] = True
        else:
            print(
                f"The room number {room} does not exist in the current hotel")

    def free_room(self, room: int) -> None:
        """Cancels a reservation of a room for the hotel"""
        if 0 < room < len(self.reserv) + 1:
            self.reserv[room] = False
        else:
            print(
                f"The room number {room} does not exist in the current hotel")
