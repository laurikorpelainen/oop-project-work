from seat import Seat
class MovieHall:
    def __init__(self, id: str, name: str, seat_count: int):
        self.__id = id
        self.__name = name
        self.__seats = [Seat() for _ in range(seat_count)]

    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def seats(self):
        return self.__seats
    
    def reserve_seat(self, seat_number):
        self.__seats[seat_number].reserve_seat()

    def display_seats(self):
        print([str(seat) for seat in self.__seats])