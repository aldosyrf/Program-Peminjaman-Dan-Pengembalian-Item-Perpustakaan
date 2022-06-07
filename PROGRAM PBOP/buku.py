from perpusItem import PerpusItem


class Buku(PerpusItem):
    def __init__(self, judul, harga, isbn, pengarang):
        super().__init__(judul, harga)
        self.isbn = isbn
        self.pengarang = pengarang