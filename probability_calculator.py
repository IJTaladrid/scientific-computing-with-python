import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls_to_draw):
        if num_balls_to_draw >= len(self.contents):
            # If the number to draw is too large, return all balls
            # and empty the hat.
            all_balls = self.contents[:]
            self.contents.clear()
            return all_balls
        
        # Use random.sample to select balls without replacement.
        drawn_balls = random.sample(self.contents, num_balls_to_draw)
        
        # Remove the drawn balls from the hat's contents.
        for ball in drawn_balls:
            self.contents.remove(ball)
            
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_outcomes = 0
    for _ in range(num_experiments):
        temp_hat = copy.deepcopy(hat)
        drawn_balls = temp_hat.draw(num_balls_drawn)

        # Count the drawn balls
        drawn_balls_count = {}
        for ball in drawn_balls:
            drawn_balls_count[ball] = drawn_balls_count.get(ball, 0) + 1

        # Check if all expected conditions are met
        success = True
        for color, count in expected_balls.items():
            if drawn_balls_count.get(color, 0) < count:
                success = False
                break
        
        if success:
            successful_outcomes += 1

    return successful_outcomes / num_experiments

hat = Hat(black=6, red=4, green=3)

# Define the expected balls and experiment parameters
expected = {'red': 2, 'green': 1}
num_balls = 5
num_exp = 2000

# Calculate the probability
probability = experiment(
    hat=hat,
    expected_balls=expected,
    num_balls_drawn=num_balls,
    num_experiments=num_exp
)

# Print the result
print(f"The approximate probability is: {probability}")