from seat import Seat

class MovieHall:
    __id_counter = 0

    def __init__(self, type, rows: int, columns: int, ticket_price: float):
        self.__type = type
        self.__rows = rows
        self.__columns = columns
        self.__ticket_price = ticket_price
        self.__seats = [[Seat(row, column) for column in range(self.__columns)] for row in range(self.__rows)]
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
    
    @property
    def ticket_price(self):
        return self.__ticket_price
    
    def reserve_seat(self, row, column):
        self.__seats[row-1][column-1].reserve_seat()

    def display_seats(self):
        for row in self.__seats:
            print(" ".join(str(seat) for seat in row))

    def __str__(self):
        return f"Moviehall ID: {self.__id_counter}, Moviehall type: {self.__type}"
