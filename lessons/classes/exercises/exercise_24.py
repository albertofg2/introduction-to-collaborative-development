import math

class Coordinate:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return float(self._x)

    @property
    def y(self):
        return float(self._y)

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Coordinate value must be an integer or float")
        self._x = value

    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Coordinate value must be an integer or float")
        self._y = value

    def distance_to_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __add__(self, other):
        if not isinstance(other, Coordinate):
            raise TypeError("Cannot add non-coordinate object to coordinate")
        return Coordinate(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Coordinate):
            raise TypeError("Cannot subtract non-coordinate object from coordinate")
        return Coordinate(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("Cannot multiply coordinate by non-integer or non-float value")
        return Coordinate(self.x * other, self.y * other)

    def __truediv__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("Cannot divide coordinate by non-integer or non-float value")
        return Coordinate(self.x / other, self.y / other)

    def __eq__(self, other):
        if not isinstance(other, Coordinate):
            return False
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        if not isinstance(other, Coordinate):
            raise TypeError("Cannot compare coordinate with non-coordinate object")
        return self.distance_to_origin() < other.distance_to_origin()

    def __len__(self):
        return 2

    def __hash__(self):
        return hash((self.x, self.y))

    def __iter__(self):
        yield self.x
        yield self.y

    def __getattr__(self, attr):
        if attr == "magnitude":
            return self.distance_to_origin()
        else:
            raise AttributeError(f"'Coordinate' object has no attribute '{attr}'")

    def __setattr__(self, attr, value):
        if attr == "magnitude":
            raise AttributeError("Cannot set 'magnitude' attribute")
        else:
            super().__setattr__(attr, value)

    def __repr__(self):
        return f"Coordinate({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"
