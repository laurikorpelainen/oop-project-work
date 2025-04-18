from seat import Seat
from config import testing
class MovieHall:
    __id_counter = 0

    def __init__(self, type, rows: int, columns: int, ticket_price: float):

        if testing:
            assert isinstance(type, str) and len(type) > 0, "Type must be a non-empty string"
            assert isinstance(rows, int) and rows > 0, "Rows must be a positive integer"
            assert isinstance(columns, int) and columns > 0, "Columns must be a positive integer"
            assert isinstance(ticket_price, float) and ticket_price >= 0, "Ticket price must be a non-negative float"

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
    
    def reserve_seat(self, row: int, column: int):

        if testing:
            assert isinstance(row, int) and row > 0, 'Row must be a positive integer bigger than 0'
            assert isinstance(column, int) and column >= 1, 'Column must be a positive integer bigger than 0'

        self.__seats[row-1][column-1].reserve_seat()

    def display_seats(self):
        for row in self.__seats:
            print(" ".join(str(seat) for seat in row))

    def get_hall_features(self) -> list[str]:
        return [f"{self.__rows * self.__columns} seats"]

    def __str__(self):
        return f"Moviehall ID: {self.__id_counter}, Moviehall type: {self.__type}"
