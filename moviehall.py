from seat import Seat
class MovieHall:
    __id_counter = 1

    def __init__(self, type, seat_count):
        self.__type = type # Type will be child class
        self.__seats = [Seat() for _ in range(seat_count)]
        MovieHall.__id_counter += 1
    
    @property
    def type(self):
        return self.__type

    @property
    def id(self):
        return self.__id_counter
    
    @property
    def seats(self):
        return self.__seats
    
    def reserve_seat(self, seat_number):
        self.__seats[seat_number].reserve_seat()

    def display_seats(self):
        print([str(seat) for seat in self.__seats])

    def __str__(self):
        return f"Moviehall ID: {self.__id_counter}, Moviehall type: {self.__type}"
