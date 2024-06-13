class Light:
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def get_direction(self, hit_point):
        '''
        Light direction to the geo intersect point
        '''
        return (self.position - hit_point).normalize()