class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self, thinkness=1):
        print(self._length * self._width * thinkness)


road = Road(10, 10)
road.asphalt_mass(2)
