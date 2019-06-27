"""9. In a particular pain clinic, 10% of patients are prescribed narcotic pain killers.
Overall, five percent of the clinics patients are addicted to narcotics (including pain killers and illegal substances).
 Out of all the people prescribed pain pills, 8% are addicts. If a patient is an addict, write a program to find the
  probability that they will be prescribed pain pills?"""
from week3.Utility.Utility_probability import Util


class PainPills(Util):
    obj = Util

    def __init__(self):
        self.pain_killers = 0.1           # 10% of patients are prescribed narcotic pain killers
        self.addicted = 0.05              # five percent of the clinics patients are addicted to narcotics
        self.addict_getting_pills = 0.08  # all the people prescribed pain pills, 8% are addicts

    def probability(self):
        probability_result = obj.prescribed_pain_pills(self.pain_killers, self.addicted, self.addict_getting_pills)
        print("Probability of that prescribed pain pills:", probability_result)


# creates object of class
obj = PainPills()
# calling method by using class object
obj.probability()
