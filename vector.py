import math

class Vec3:
    '''
    Simple vector math lib
    '''
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, val):
        return Vec3(self.x + val.x, self.y + val.y, self.z + val.z)

    def __sub__(self, val):
        return Vec3(self.x - val.x, self.y - val.y, self.z - val.z)

    def __mul__(self, val):
        if isinstance(val, Vec3):
            return Vec3(self.x * val.x, self.y * val.y, self.z * val.z)
        else:
            return Vec3(self.x * val, self.y * val, self.z * val)

    def __rmul__(self, val):
        return Vec3(self.x * val, self.y * val, self.z * val)

    def __str__(self):
        return f'Vec3({self.x}, {self.y}, {self.z})'

    def dot(self, val):
        return self.x * val.x + self.y * val.y + self.z * val.z

    def normalize(self):
        norm = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        return Vec3(self.x / norm, self.y / norm, self.z / norm)