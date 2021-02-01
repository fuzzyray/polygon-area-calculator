class Rectangle:
    def __init__(self, width, height):
        pass

    def __repr__(self):
        return super().__repr__()

    def set_width(self, width):
        pass

    def set_height(self, height):
        pass

    def get_area(self):
        pass

    def get_perimeter(self):
        pass

    def get_diagonal(self):
        pass

    def get_picture(self):
        pass

    def get_amount_inside(self, shape):
        pass

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        pass

    def set_height(self, height):
        self.set_side(height)

    def set_width(self, width):
        self.set_side(width)
        super().set_width(width)

    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)

