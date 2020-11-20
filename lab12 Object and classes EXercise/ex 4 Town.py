class Town:
    def __init__(self, name):
        self.name = name

    def set_latitude(self, latitude):
        return

    def set_longitude(self, longitude):
        return

    def __repr__(self):
        return


town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)
