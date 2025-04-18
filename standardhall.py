from moviehall import MovieHall

class StandardHall(MovieHall):
    """
    Subclass of MovieHall representing a standard hall experience.
    Adds common features such as 2D projection and basic seating to the base features.
    """
    def __init__(self, rows, columns, ticket_price=14.90, type='Standard'):
        # Initialize with default standard ticket price and type, delegates to MovieHall constructor
        super().__init__(type, rows, columns, ticket_price)

    def get_hall_features(self) -> list[str]:
        # Extend base hall features with standard amenities
        features = super().get_hall_features()
        features.extend(["Regular sound system", "2D projection", "Standard seating"])
        return features