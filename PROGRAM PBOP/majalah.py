from perpusItem import PerpusItem


class Majalah(PerpusItem):
    def __init__(self, judul, harga, volume):
        super().__init__(judul, harga)
        self.volume = volume