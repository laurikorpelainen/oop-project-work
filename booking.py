from movietheatre import MovieTheatre
from moviehall import MovieHall
from standardhall import StandardHall
from premiumhall import PremiumHall
from movie import Movie
from seat import Seat
from user import User
from screening import Screening

class Booking:
    __booking_id_counter = 0
    __screening_id_counter = 0
    
    def __init__(self):
        self.__user = None
        self.__theaters = []
        self.__movies = []
        self.__screenings = []
        self.__bookings = []
    
    def register_user(self, user):
        self.__user = user
        return self.__user
        
    def add_theater(self, theater):
        self.__theaters.append(theater)
        self.__screenings[theater] = []
        return theater
    
    def add_movie(self, movie):
        self.__movies.append(movie)
        return movie
    
    def create_screening(self, theater, movie, hall, time, date):
        Booking.__screening_id_counter += 1
        screening = Screening(Screening.Booking.__screening_id_counter, movie, hall,time,date)
        self.__screenings[theater].append(screening)
        return screening
    
    def create_booking(self, user, screening, seats):
        # Check if user is old enough for the movie
        if user.age < screening.movie.age_rating:
            return None, "User is too young for this movie"
        
        # Check if user has enough balance to buy a ticket
        if user.balance < screening.hall.ticket_price:
            return None, f"User balance too low. Current balance {user.balance}"
        
        # Check if seats are valid and available
        for row, col in seats:
            if row < 0 or col < 0 or row >= (len(screening.hall.seats) + 1) or col >= (len(screening.hall.seats[0]) + 1):
                return None, "Invalid seat position"
            if screening.hall.seats[row - 1][col - 1].__str__() == "1":
                return None, "One or more seats are already reserved"
        
        # Reserve a seat
        for row, column in seats:
            screening.hall.reserve_seat(row, column)

        #Reduce ticket price from user balance
        user.decrease_funds(screening.hall.ticket_price)
            
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
        return self.__user
    
    def get_theaters(self):
        return self.__theaters
    
    def get_movies(self):
        return self.__movies
    
    def get_screenings(self, theater=None):
        if theater:
            return self.__screenings.get(theater, [])
        else:
            all_screenings = []
            for theater_screenings in self.__screenings.values():
                all_screenings.extend(theater_screenings)
            return all_screenings
    
    def get_bookings(self):
        return self.__bookings
    
    def get_user_bookings(self, user):
        return [booking for booking in self.__bookings if booking["user"] == user]
    
    def format_booking_str(self, booking):
        seats_str = ", ".join([f"({r},{c})" for r, c in booking["seats"]])
        return f"Booking ID: {booking['id']}, User: {booking['user'].name}, " \
               f"Movie: {booking['screening'].movie.title}, Seats: {seats_str}"
               
    def format_screening_str(self, screening):
        return f"Screening ID: {screening.id}, Movie: {screening.movie.title}, " \
               f"Date: {screening.date}, Time: {screening.time}"