import copy
import random

class Hat:
    def __init__(self, **balls):
        self.balls = dict(balls)
        self.contents = []
        for colour, number in self.balls.items():
            for i in range(number):
                self.contents.append(colour)

    def draw(self, number_of_balls_to_draw):
        random_balls = []
        temp_contents = self.contents
        if number_of_balls_to_draw > len(self.contents):
            return self.contents
        for i in range(number_of_balls_to_draw):
          random_ball = random.choice(temp_contents)
          random_balls.append(random_ball)
          temp_contents.remove(random_ball)
        return random_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    times_occurred = 0
    for experiment in range(num_experiments):
      hat_copy = copy.deepcopy(hat)
      expected_balls_copy = copy.deepcopy(expected_balls)
      result = hat_copy.draw(num_balls_drawn)
      for ball in result:
        if ball in expected_balls_copy:
          expected_balls_copy[ball] -= 1
      if all(value <= 0 for value in expected_balls_copy.values()):
        times_occurred += 1
    
    probability = times_occurred/num_experiments
    return(probability)