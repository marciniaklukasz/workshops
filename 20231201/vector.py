class V:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return V (self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return V (self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"Wektor({self.x}, {self.y})"

    def __eq__(self, other):
        if V (self.x == other.x, self.y == other.y):
            (False, False)
            return "Not matched"
        else:
            return "Matched"

    def __mul__(self, other):
        return V (self.x * input, self.y * input)

wektor1 = V (2, 3)
wektor2 = V (5, 7)
input = int(input('liczba:'))

wektor3 = wektor1 * wektor2
print (wektor3)