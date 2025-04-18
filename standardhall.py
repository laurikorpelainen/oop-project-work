from moviehall import MovieHall

class StandardHall(MovieHall):
    def __init__(self, rows, columns, ticket_price=14.90, type='Standard'):
        super().__init__(type, rows, columns, ticket_price)

    def get_hall_features(self) -> list[str]:
        features = super().get_hall_features()
        features.extend(["Regular sound system", "2D projection", "Standard seating"])
        return features