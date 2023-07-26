"""Define a class with a generator which can iterate the numbers,
    which are divisible by 7, between a given range 0 and n.
    Suppose the following input is supplied to the program:
    7
    Then, the output should be:
    0
    7
    14 -- I suppose it is a mistake as 14 > n?
    Hints:
    Verify the output with running tests: python tasks_test.py.
    Consider use class, function and comprehension."""

class NumGenerator:
    def __init__(self, div_by):
        self.div_by = div_by
    def div_by_7(self):
        output_list = [i for i in range(0, self.div_by+1) if i % 7 == 0]

        return output_list


"""A robot moves in a plane starting from the original point (0,0). 
    The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
    The trace of robot movement is shown as the following:
    UP 5
    DOWN 3
    LEFT 3
    RIGHT 2
    The numbers after the direction are steps. 
    Please write a program to compute the distance from current position after a 
    sequence of movement and original point. If the distance is a float, 
    then just print the nearest integer. 
    Hints:
    Here distance indicates to euclidean distance. Import math module to use sqrt function.."""

from math import sqrt
def robot_moves(input_str):
    # Parse input string to get a list, remove empty values
    input_list = [i.strip() for i in filter(None, input_str.split(' '))]
    # Convert list to a dictionary
    input_dict = {input_list[i]: int(input_list[i + 1]) for i in range(0, len(input_list), 2)}
    # Create variables a and b to store final values of the vectors
    a = 0
    b = 0
    for key in input_dict:
        if key == 'UP':
            a += input_dict[key]
        elif key == 'DOWN':
            a -= input_dict[key]
        elif key == 'RIGHT':
            b += input_dict[key]
        elif key == 'LEFT':
            b -= input_dict[key]
    # Calculate the hypotenuse, convert to int
    c = int(sqrt(a**2 + b**2))

    return c
