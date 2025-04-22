import unittest
from moviehall import MovieHall
from movie import Movie
from user import User
from seat import Seat
from movietheatre import MovieTheatre
from screening import Screening
from premiumhall import PremiumHall
from standardhall import StandardHall

testing = True

class TestMovieBooking(unittest.TestCase):

    def test_standard_hall(self):

        # Test standard hall
        standard_hall = StandardHall(10, 10, 14.90)
        self.assertEqual(standard_hall.type, "Standard")  # Check if the type is correct
        self.assertEqual(standard_hall.ticket_price, 14.90)  # Check if the price is correct
        self.assertEqual(len(standard_hall.seats), 10)  # Check if there are 10 rows
        self.assertEqual(len(standard_hall.seats[0]), 10)  # Check if each row has 10 seats
        
    def test_premium_hall(self):

        # Test premium hall
        premium_hall = PremiumHall(12, 15, 23.90)
        self.assertEqual(premium_hall.type, "Premium")  # Check if the type is correct
        self.assertEqual(premium_hall.ticket_price, 23.90)  # Check if the price is correct
        self.assertEqual(len(premium_hall.seats), 12)  # Check if there are 12 rows
        self.assertEqual(len(premium_hall.seats[0]), 15)  # Check if each row has 15 seats

    def test_screening(self):
        
        movie = Movie("Interstellar", 180, "Christopher Nolan", "Sci-Fi", 10)
        hall = StandardHall(10, 10, 14.90)
        theater = MovieTheatre("Tennispalatsi", "Helsinki", [hall])

        screening = Screening(movie, hall, "20:00", "2025-05-01", theater) # Create a screening for the movie
        self.assertEqual(screening.movie.title, "Interstellar") # Check if the movie title is correct
        self.assertEqual(screening.hall, hall) # Check if the hall is correctly assigned
        self.assertEqual(screening.time, "20:00") # Check if the time is correctly assigned
        self.assertEqual(screening.date, "2025-05-01") # Check if the date is correctly assigned
        self.assertEqual(screening.theater.name, "Tennispalatsi") # Check if the theater is correctly assigned

    def test_seat_reservation(self):
        
        hall = StandardHall(5, 5, 14.90)  # Create a hall with 5x5 seats
        hall.seats[0][0].reserve_seat() # Reserve the first seat
        self.assertTrue(hall.seats[0][0].is_reserved)  # Check that the seat is reserved
        hall.seats[0][0].reserve_seat() # Try to reserve the same seat again
        self.assertTrue(hall.seats[0][0].is_reserved) # Check that the seat is still reserved

    def test_theater_hall_addition(self):

        theater = MovieTheatre("Tennispalatsi", "Helsinki", [MovieHall("Standard", 10, 10, 14.90)]) # Create a theater with no halls initially
        hall1 = MovieHall("Standard", 10, 10, 14.90) # Create a standard hall
        theater.add_hall(hall1) # Add the hall to the theater
        self.assertEqual(len(theater.halls), 2)  # Check that the hall was added to the theater
        #We expect 1 hall in the theater now

    def test_user_creation(self):

        user = User("Lauri Uusitalo", 80, 5.0)

        self.assertEqual(user.name, "Lauri Uusitalo")  # Test name
        self.assertEqual(user.age, 80)  # Test age
        self.assertEqual(user.balance, 5.0)  # Test balance


if __name__ == '__main__':
    unittest.main()