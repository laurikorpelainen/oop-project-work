from seat import Seat
class MovieHall:
    def __init__(self, id, name, seat_count):
        self.__id = id
        self.__name = name
        self.__seats = [Seat() for _ in range(seat_count)]

    @property
    def seats(self):
        return self.__seats