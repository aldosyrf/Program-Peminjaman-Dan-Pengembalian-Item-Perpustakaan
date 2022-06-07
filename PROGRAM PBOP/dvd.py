from perpusItem import PerpusItem


class Majalah(PerpusItem):
    def __init__(self, judul, harga, genre):
        super().__init__(judul, harga)
        self.genre = genre