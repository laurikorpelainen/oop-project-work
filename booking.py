from movietheatre import MovieTheatre
from moviehall import MovieHall
from movie import Movie
from user import User
from screening import Screening
from config import testing

class Booking:
    """
    This defines the Booking class to handle all movie ticket booking operations including
    user registration, theater/movie/screening management, seat reservations, and payment handling.
    """
    __booking_id_counter = 0    # Tracks booking ID for uniqueness
    __screening_id_counter = 0  # Tracks screening ID for uniqueness
    
    def __init__(self):
        # Initialize internal storage for booking system data
        self.__user: User = None
        self.__theaters: list[MovieTheatre] = []
        self.__movies: list[Movie] = []
        self.__screenings: dict[MovieTheatre, list[Screening]] = {}
        self.__bookings: list[dict] = []
    

    def register_user(self, user: User) -> User:
        # Register a new user to the system
        if testing:
            assert isinstance(user, User), "User must be a User object"

        self.__user = user
        return self.__user
        

    def add_theater(self, theater: MovieTheatre) -> MovieTheatre:
        # Add a new movie theater and initialize its screening list
        if testing:
            assert isinstance(theater, MovieTheatre), "Theater must be a MovieTheatre object"

        self.__theaters.append(theater)
        self.__screenings[theater] = []
        return theater
    

    def add_movie(self, movie: Movie) -> Movie:
        # Add a movie to the system
        if testing:
            assert isinstance(movie, Movie), "Movie must be a Movie object"

        self.__movies.append(movie)
        return movie
    

    def create_screening(self, theater: MovieTheatre, movie: Movie, hall: MovieHall, time: str, date: object) -> Screening:
        # Schedule a movie screening in a specific hall at a specific time/date
        if testing:
            assert isinstance(theater, MovieTheatre), "Theater must be a MovieTheatre object"
            assert isinstance(movie, Movie), "Movie must be a Movie object"
            assert isinstance(hall, MovieHall), "Hall must be a MovieHall object"
            assert isinstance(time, str) and len(time) > 0, "Time must be non-negative length string"
            assert isinstance(date, object), "Time must be a datetime object"
            assert theater in self.__theaters, "Theater must be registered first"
            assert movie in self.__movies, "Movie must be registered first"
            assert hall in theater.halls, "Hall must belong to the theater"

        Booking.__screening_id_counter += 1
        screening = Screening(movie, hall, time, date, theater)
        self.__screenings[theater].append(screening)
        return screening
    

    def create_booking(self, user: User, screening: Screening, seats: list[tuple[int, int]]) -> tuple[dict, str]:
        # Book selected seats for a user in a specific screening
        if testing:
            assert isinstance(user, User), 'User must be a User object'
            assert isinstance(screening, Screening), 'Screening must be a Screening object'
            assert isinstance(seats, list), "Seats must be a list of tuples"
            assert all(isinstance(seat, tuple) and len(seat) == 2 for seat in seats), "Each seat must be a tuple of (row, column)"

        # Check if user is old enough for the movie
        if user.age < screening.movie.age_rating:
            return None, "User is too young for this movie"
        
        # Check if user has enough balance to buy a ticket
        total_price = screening.hall.ticket_price * len(seats)
        if user.balance < total_price:
            return None, f"User balance too low. Need {total_price}, current balance {user.balance}"
        
        # Check if seats are valid and available
        for row, col in seats:
            if row < 0 or col < 0 or row >= (len(screening.hall.seats) + 1) or col >= (len(screening.hall.seats[0]) + 1):
                return None, "Invalid seat position"
            if screening.hall.seats[row - 1][col - 1].__str__() == "1":
                return None, "One or more seats are already reserved"
        
        # Reserve a seat
        for row, column in seats:
            screening.hall.reserve_seat(row, column)

        # Reduce ticket price from user balance
        user.decrease_funds(total_price)
            
        Booking.__booking_id_counter += 1
        booking = {
            "id": Booking.__booking_id_counter,
            "user": user,
            "screening": screening,
            "seats": seats
        }
        
        self.__bookings.append(booking)
        return booking, "Booking successful"
    

    @property
    def user(self):
        # Get the currently registered user
        return self.__user

    def get_theaters(self):
        # Return list of added theaters
        return self.__theaters

    def get_movies(self):
        # Return list of added movies
        return self.__movies

    def get_screenings(self, theater=None):
        # Return screenings for a specific theater or all if not specified
        if theater:
            return self.__screenings.get(theater, [])
        else:
            all_screenings = []
            for theater_screenings in self.__screenings.values():
                all_screenings.extend(theater_screenings)
            return all_screenings

    def get_bookings(self):
        # Return all bookings
        return self.__bookings

    def get_user_bookings(self, user: User) -> list:
        # Return bookings for a specific user
        if testing:
            assert isinstance(user, User), 'User must a User object'

        return [booking for booking in self.__bookings if booking["user"] == user]

    def format_booking_str(self, booking: dict) -> str:
        # Convert a booking dictionary to a readable string
        if testing:
            assert isinstance(booking, dict), "Booking must be a dictionary"
            
        seats_str = ", ".join([f"({r},{c})" for r, c in booking["seats"]])
        return f"Booking ID: {booking['id']}, User: {booking['user'].name}, " \
               f"Movie: {booking['screening'].movie.title}, Seats: {seats_str}"

    def format_screening_str(self, screening: Screening) -> str:
        # Convert a screening object to a readable string
        if testing:
            assert isinstance(screening, Screening), "Screening must be a Screening object"

        return f"Screening ID: {screening.id}, Movie: {screening.movie.title}, " \
               f"Date: {screening.date}, Time: {screening.time}"