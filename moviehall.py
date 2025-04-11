from seat import Seat
class MovieHall:
    __id_counter = 1

    def __init__(self, type, rows: int, collumns: int):
        self.__type = type # Type will be child class
        self.__rows = rows
        self.__collumns = collumns
        self.__seats = [[Seat(row, collum) for collum in range(self.__collumns)] for row in range(self.__rows)]
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
    
    def reserve_seat(self, row, collumn):
        self.__seats[row][collumn].reserve_seat()

    def display_seats(self):
        for row in self.__seats:
            print(" ".join(str(seat) for seat in row))

    def __str__(self):
        return f"Moviehall ID: {self.__id_counter}, Moviehall type: {self.__type}"
