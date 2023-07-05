import copy
import random

def to_list(old_dict: dict) -> list:
    """Takes a dictionary where the keys are strings and the values are the 
    frequency of each of those strings, then returns a list of strings 
    relative to the frequency of each key."""
    new_list = []
    for key, value in old_dict.items():
        for n in range(value):
            new_list.append(key)

    return new_list

class Hat:
    def __init__(self, **colours: int) -> None:
        """Initializes the Hat object, taking n parameters with colour names 
        and integers as arguments"""
        self.contents = to_list(colours)
        self.contents_copy = self.contents

    def draw(self, how_many: int) -> list:
        """The draw method takes an integer, how_many, that represents the 
        size of the random sample to be taken from the contents of the hat, 
        self.contents. It starts a loop beginning with the value of how_many, 
        and decrements the value, as long as self.contents is not empty. Every 
        time it loops, a random ball is popped from self.contents and appended 
        to the random_sample list. In the end, the random_sample list is 
        returned."""
        random_sample = []
        while how_many > 0:
            if len(self.contents) > 0:
                random_sample.append(self.contents.pop(
                    random.randint(0, len(self.contents) - 1)))
                how_many -= 1
            else:
                break
        return random_sample

def experiment(hat, expected_balls: dict, num_balls_drawn: int, 
        num_experiments: int) -> float:
    """Takes a Hat object, a dictionary similar in format to the dictionary 
    created by the colours keyword arguments of Hat.__init__(), an integer 
    representing the number of balls to be drawn from Hat.contents and another 
    integer to represent the number of experiments to be carried out. The 
    function then performs Hat.draw() N times and counts the number of times 
    in which the sample includes the expected_balls. Finally, the number of 
    successful estimations is divided by the number of experiments and the 
    quotient is returned."""
    M = 0
    for experiment in range(num_experiments):
        hat_deepcopy = copy.deepcopy(hat)
        sample = sorted(hat_deepcopy.draw(num_balls_drawn))
        sample_dict = {ball: sample.count(ball) for ball in set(sample)}

        if all(sample_dict.get(ball, 0) >= count 
               for ball, count in expected_balls.items()):
            M += 1
    
    prob = M / num_experiments
    return prob
