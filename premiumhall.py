from moviehall import MovieHall

class PremiumHall(MovieHall):
    def __init__(self, rows, columns, ticket_price=23.90, type='Premium'):
        super().__init__(type, rows, columns, ticket_price)

    def get_hall_features(self) -> list[str]:
        features = super().get_hall_features()
        features.extend(["Dolby Atmos sound", "3D projection", "Reclining seats"])
        return features