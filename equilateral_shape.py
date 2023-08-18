# State initializer, behavior in methods
# Identify the required state and make that part of your initializer method __init__
# For each behavior you identified, write a method that does that for you:
# Use pseudocode to figure it out
# Translate the pseudocode to real code

class EquilateralShape:
    def __init__(self, num_sides, side_length):
        self.num_sides = num_sides
        self.side_length = side_length

        traingle1 = EquilateralShape(3,1)
        triangle2 = EquilaterlShape(3,100)
        square = EquilateralShape(3, 1)

        print(triangle1.num_sides)      #prints 3
        print(triangle1.side_length)    #prints 1

        print(triangle2.num_sides)      #prints 3
        print(triangle2.side_length)    #prints 100

        print(square.num_sides)         #prints 4
        print(square.side_length)       #prints 1

    def calculate_perimeter(self):
        result = self.num_sides * self.side_length
        return result

    def calculate_area(self):
        side_squared = pow(self.side_length, 2)

        if self.num_sides == 3:
            return math.sqrt(3) / 4 * side_squared
        elif self.num_sides == 4:
            return side_squared
        elif self.num_sides == 5:
            weird_value = math.sqrt(25 + 10 * math.sqrt(5))
            return weird_value / 4 * side_squared
        elif self.num_sides == 6:
            return (3 * math.sqrt(3)) / 2 * side_squared
        else:
            raise ValueError
