from moviehall import MovieHall

class PremiumHall(MovieHall):
    """
    Subclass of MovieHall representing a premium experience hall.
    Extends base hall features with premium amenities like Dolby sound, 3D, and reclining seats
    """
    def __init__(self, rows, columns, ticket_price=23.90, type='Premium'):
        # Initialize with default premium ticket price and type, delegates to MovieHall constructor
        super().__init__(type, rows, columns, ticket_price)

    def get_hall_features(self) -> list[str]:
        # Extend base hall features with premium amenities
        features = super().get_hall_features()
        features.extend(["Dolby Atmos sound", "3D projection", "Reclining seats"])
        return features