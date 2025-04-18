from seat import Seat
from config import testing
class MovieHall:
    """
    Defines the MovieHall class which represents a hall inside a movie theater.
    Responsible for seating layout, pricing, reservation logic, and displaying hall features.
    """
    __id_counter = 0    # Counter to assign unique IDs

    def __init__(self, type, rows: int, columns: int, ticket_price: float):
        # Initialize a new movie hall with type, seating layout, and ticket price
        if testing:
            assert isinstance(type, str) and len(type) > 0, "Type must be a non-empty string"
            assert isinstance(rows, int) and rows > 0, "Rows must be a positive integer"
            assert isinstance(columns, int) and columns > 0, "Columns must be a positive integer"
            assert isinstance(ticket_price, float) and ticket_price >= 0, "Ticket price must be a non-negative float"

        self.__type = type
        self.__rows = rows
        self.__columns = columns
        self.__ticket_price = ticket_price
        # Create a 2D list of Seat objects for the hall
        self.__seats = [[Seat(row, column) for column in range(self.__columns)] for row in range(self.__rows)]
        MovieHall.__id_counter += 1 # Increment global movie ID counter
    
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
        # Reserve a seat at a given row and column
        if testing:
            assert isinstance(row, int) and row > 0, 'Row must be a positive integer bigger than 0'
            assert isinstance(column, int) and column >= 1, 'Column must be a positive integer bigger than 0'

        self.__seats[row-1][column-1].reserve_seat()

    def display_seats(self):
        # Print the seating layout, 0 for available, 1 for reserved
        for row in self.__seats:
            print(" ".join(str(seat) for seat in row))

    def get_hall_features(self) -> list[str]:
        # Return basic hall features, like number of seats
        return [f"{self.__rows * self.__columns} seats"]

    def __str__(self):
        # String representation of the MovieHall instance
        return f"Moviehall ID: {self.__id_counter}, Moviehall type: {self.__type}"
