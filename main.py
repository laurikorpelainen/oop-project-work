from booking import Booking
from movietheatre import MovieTheatre
from standardhall import StandardHall
from premiumhall import PremiumHall
from movie import Movie
from user import User
import datetime

def main():
    # Initialize the booking system
    app = Booking()
    
    # Create movie halls
    std_hall1 = StandardHall(rows=5, columns=10)
    std_hall2 = StandardHall(rows=6, columns=8)
    premium_hall = PremiumHall(rows=4, columns=8)
    premium_hall2 = PremiumHall(rows=5, columns=10)

    # Assign halls to cities
    turku_halls = [std_hall1, premium_hall]
    raisio_halls = [std_hall2, premium_hall2]

    # Add theaters to the booking system
    theater1 = app.add_theater(MovieTheatre("Finnkino", "Turku", turku_halls))
    theater2 = app.add_theater(MovieTheatre("Finnkino", "Raisio", raisio_halls))
    
    # Add movies
    movie1 = app.add_movie(Movie("The Matrix", 136, "Wachowski Brothers", "Sci-Fi", 13))
    movie2 = app.add_movie(Movie("Toy Story", 81, "John Lasseter", "Animation", 0))
    movie3 = app.add_movie(Movie("The Shawshank Redemption", 142, "Frank Darabont", "Drama", 16))
    
    # Set up screening dates
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    
    # Create screenings for the movies
    app.create_screening(theater1, movie1, theater1.halls[0], "18:00", today)
    app.create_screening(theater1, movie1, theater1.halls[1], "21:00", today)
    app.create_screening(theater2, movie2, theater2.halls[0], "15:30", today)
    app.create_screening(theater2, movie3, theater2.halls[1], "19:30", tomorrow)
    
    selected_theater = None # No theater selected yet
    
    # User interaction loop
    while True:
        print("\nMOVIE BOOKING APP")
        print("1. Register as a user")
        print("2. Select theater")
        print("3. Book tickets")
        print("4. View user bookings")
        print("5. Display available seats")
        print("6. Display hall features")
        print("7. Display balance")
        print("8. Add balance")
        print("0. Exit\n")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            # Register user
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            user = app.register_user(User(name, age, 100.0))

            print(f"User registered: {user}")
        

        elif choice == "2":
            # Select a theater
            print("Available theaters:")
            for i, theater in enumerate(app.get_theaters()):
                print(f"{i+1}. {theater.name} ({theater.city})")

            theater_idx = int(input("Select theater (number): ")) - 1
            selected_theater = app.get_theaters()[theater_idx]
            print(f"Selected theater: {selected_theater.name} ({selected_theater.city})")
        

        elif choice == "3":
            # Book tickets
            if not app.user:
                print("No user registered. Please register a user first.")
                continue
            if not selected_theater:
                print("No theater selected. Please select a theater first.")
                continue
                
            screenings = app.get_screenings(selected_theater)
            available_movies = list({screening.movie for screening in screenings})
            
            if not available_movies:
                print("No movies available in this theater.")
                continue
            
            # List available movies
            print("Available movies:")
            for i, movie in enumerate(available_movies):
                print(f"{i+1}. {movie.title}")

            movie_idx = int(input("Select movie (number): ")) - 1
            selected_movie = available_movies[movie_idx]
            
            # Show screenings for selected movie
            movie_screenings = [s for s in screenings if s.movie == selected_movie]
            print("Available screenings:")

            for i, screening in enumerate(movie_screenings):
                print(f"{i+1}. {app.format_screening_str(screening)}")

            screening_idx = int(input("Select screening (number): ")) - 1
            selected_screening = movie_screenings[screening_idx]

            # Show seat layout
            print("Current seat reservation (0 = available, 1 = reserved):")
            selected_screening.hall.display_seats()
            
            # Select seats
            num_seats = int(input("How many seats do you want to book? "))
            seats = []
            
            for i in range(num_seats):

                row = int(input(f"Enter row for seat {i+1}: "))
                col = int(input(f"Enter column for seat {i+1}: "))
                seats.append((row, col))
            
            # Attempt booking
            booking, message = app.create_booking(app.user, selected_screening, seats)
            print(message)

            if booking:
                print(f"Booking created: {app.format_booking_str(booking)}")


        elif choice == "4":
            # Show user's bookings
            bookings = app.get_user_bookings(app.user)
            print(f"Bookings for {app.user.name}:")

            if not bookings:
                print("No bookings found")
            else:
                for booking in bookings:
                    print(app.format_booking_str(booking))


        elif choice == "5":
            # Show seat availability
            screenings = app.get_screenings(selected_theater)
            available_movies = list({screening.movie for screening in screenings})
            
            if not available_movies:
                print("No movies available in this theater.")
                continue
            
            print("Available movies:")
            for i, movie in enumerate(available_movies):
                print(f"{i+1}. {movie.title}")

            movie_idx = int(input("Select movie (number): ")) - 1
            selected_movie = available_movies[movie_idx]
            
            movie_screenings = [s for s in screenings if s.movie == selected_movie]
            
            print("Available screenings:")
            for i, screening in enumerate(movie_screenings):
                print(f"{i+1}. {app.format_screening_str(screening)}")

            screening_idx = int(input("Select screening (number): ")) - 1
            selected_screening = movie_screenings[screening_idx]

            selected_screening.hall.display_seats()


        elif choice == "6":
            # Display features of a selected hall in the theater
            print("Available theaters:")
            for i, theater in enumerate(app.get_theaters()):
                print(f"{i+1}. {theater.name} ({theater.city})")

            theater_idx = int(input("Select theater (number): ")) - 1
            selected_theater = app.get_theaters()[theater_idx]
            print(f"Selected theater: {selected_theater.name} ({selected_theater.city})")

            for i, hall in enumerate(selected_theater.halls):
                print(f"{i+1}. {hall.type}")

            hall_idx = int(input("Select hall (number): ")) - 1

            print("\nHALL FEATURES")
            for feature in selected_theater.halls[hall_idx].get_hall_features():
                print(feature)
        

        elif choice == "7":
            # Display the current user's balance
            if not app.user:
                print("No user registered. Please register a user first.")
                continue

            print(f"Your balance is: {app.user.balance} €")


        elif choice == "8":
            # Add funds to user account
            if not app.user:
                print("No user registered. Please register a user first.")
                continue

            amount = float(input("How much balance would you like to add? "))
            print(app.user.add_funds(amount))


        elif choice == "0":
            # Exit app
            print("Thank you for using the Movie Booking App!")
            break 
         
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()
