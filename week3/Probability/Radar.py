"""11. A radar unit is used to measure speeds of cars on a motorway. The speeds are
normally distributed with a mean of 90 km/hr and a standard deviation of 10 km/hr. Write a
program to find the probability that a car picked at random is travelling at more than 100 km/hr?"""


class Radar_Unit:

    def __init__(self):
        self.mean = 90
        self.standard_deviation = 10
        self.Normal_speed = 100
        self.z_area = 0.8413

    def random_speed(self):
        Z_value = (self.Normal_speed - self.mean) / self.standard_deviation
        print("Z_value is:", Z_value)
        print("probability that a car picked at random is travlling at more than 100km/hr:", Z_value - self.z_area)


obj = Radar_Unit()
obj.random_speed()
