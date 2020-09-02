class RectangularRoom:
    SQUARE_FEET_TO_SQUARE_METER_CONVERSION = 0.09290304
    lengthFeet = 0.0
    widthFeet = 0.0

    def __init__(self, length, width):
        self.lengthFeet = length
        self.widthFeet = width

    def areaFeet(self):
        return self.lengthFeet * self.widthFeet

    def areaMeters(self):
        return round(self.areaFeet() * self.SQUARE_FEET_TO_SQUARE_METER_CONVERSION, 3)


if __name__ == "__main__":
    length = input("What is the length of the room in feet? ")
    width = input("What is the width of the room in feet? ")
    print("You entered dimensions of " + length + " feet by " + width + " feet.")
    print("The area is")
    room = RectangularRoom(float(length), float(width))
    print(str(room.areaFeet()) + " square feet")
    print(str(room.areaMeters()) + " square meters.")
