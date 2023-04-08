import copy
import random
# Consider using the modules imported above.

class Hat:

  # constructor
  def __init__(self, **kwargs):
    self.contents = list()
    for key,value in kwargs.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self, num_balls):
    # a list of all extracted balls
    balls_list = list()
    if num_balls > len(self.contents):
      balls_list = self.contents
    else:
      random_balls_list = random.sample(self.contents, num_balls)
      for ball in random_balls_list:
        balls_list.append(ball)
        self.contents.remove(ball)
    return balls_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  
  # number of times, where all conditions are correct
  count = 0
  for x in range(num_experiments):
    # a deep copy of hat
    hat_copy = copy.deepcopy(hat)

    # list of all drawn balls
    balls_drawn_list = hat_copy.draw(num_balls_drawn)
  
    # checking if all conditions are met or not
    condition_check = True
    for key in expected_balls.keys():
      if balls_drawn_list.count(key) < expected_balls[key]:
        condition_check = False
        break

    if condition_check: count += 1
     
  # calculating the probability
  probability = count/num_experiments
  return probability

