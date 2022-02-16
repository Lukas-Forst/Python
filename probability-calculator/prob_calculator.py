import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.contents = []
        for key, value in self.__dict__.items():
          if key != "contents":
            self.contents.extend([key]*int(str(value)))
          #print(type(value), value, key)
          
        #print(self.contents)

  def draw(self, amount):
    #@args amount signals the amount of balls drawn from the Hat.
    if amount >= len(self.contents):
      return self.contents
    else:
      return_list = []
      for draw in range(amount):
        choosen_item = random.choice(self.contents)
        self.contents.remove(choosen_item)	
        return_list.append(choosen_item)
      return return_list
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  
  #keep track of the times the right expected balls were drawn from the hat
  occurence_count = 0
  #count how often expected_balls are in drawn balls
  for experiments in range(num_experiments):
    counter = {}
    #deepcopy needs to be used, a shallow copy would remove all balls from the hat
    new_hat = copy.deepcopy(hat)
    
    #contains the balls drawn
    lst_1 = new_hat.draw(num_balls_drawn)

    for item in lst_1:
      if item not in counter:
        counter[item] = 0
      counter[item] += 1
    
    temp_count = 0
    
    for key, value in counter.items():
      if key in expected_balls:
        if expected_balls[key] <= counter[key]:
          temp_count += 1

    if temp_count == len(expected_balls):
      occurence_count +=1
    
  #
  #  drawn_balls = new_hat.draw(num_balls_drawn)
  print(occurence_count, num_experiments)


  probability = occurence_count/num_experiments
  return probability