"""5. In my town, it's rainy_para one third of the days. Given that it is rainy_para, there will be heavy
traffic with probability 12, and given that it is not rainy_para, there will be heavy traffic with probability
14. If it's rainy_para and there is heavy traffic, I arrive late for work with probability 12. On the other
hand, the probability of being late is reduced to 18 if it is not rainy_para and there is no heavy traffic.
In other situations (rainy_para and no traffic, not rainy_para and traffic) the probability of being late is 0.25.
You pick a random day."""
from week3.Utility.Utility_probability import Util


class Rainy_Town(Util):

    def __init__(self):

        self.obj1 = Util()
        self.rainy_para = 1 / 3
        self.rainy_with_Traffic = 1 / 2
        self.rainy_withTraffic_late = 1 / 2
        self.rainy_withTraffic_Nolate = 1 / 2

        self.rainy_with_NoTraffic = 1 / 2
        self.rainy_with_NoTraffic_late = 1 / 4
        self.rainy_with_NoTraffic_Nolate = 3 / 4

        self.not_rainy = 2 / 3
        self.not_rainy_with_Traffic = 1 / 4
        self.not_rainy_with_Traffic_late = 1 / 4
        self.not_rainy_with_Traffic_Nolate = 3 / 4

        self.not_rainy_with_NoTraffic = 3 / 4
        self.not_rainy_with_NoTraffic_late = 1 / 8
        self.not_rainy_with_NoTraffic_Nolate = 7 / 8

    "1. What is the probability that it's not raining and there is heavy traffic and I am not late?"

    def rainy(self):
        print("probability that no raining, heavy traffic,not late:", self.obj1.NoRainy_Traffic_NoLate(self.not_rainy, self.not_rainy_with_Traffic, self.not_rainy_with_Traffic_Nolate))
        # print("\n probability that it's not raining and there is heavy traffic and I am not late :", probability)

    "2. What is the probability that I am late?"

    def late(self):
        rainy_withTraffic_late = self.rainy_para * self.rainy_with_Traffic * self.rainy_withTraffic_late
        rainy_with_NoTraffic_late = self.rainy_para * self.rainy_with_NoTraffic * self.rainy_with_NoTraffic_late
        not_rainy_with_Traffic_late = self.not_rainy * self.not_rainy_with_Traffic * self.not_rainy_with_Traffic_late
        not_rainy_with_NoTraffic_late = self.not_rainy * self.not_rainy_with_NoTraffic * self.not_rainy_with_NoTraffic_late

        result = rainy_withTraffic_late + rainy_with_NoTraffic_late \
                 + not_rainy_with_Traffic_late + not_rainy_with_NoTraffic_late

        print("probability that I am late:", result)
        return result

    "3.Given that I arrived late at work, what is the probability that it rained that day?"

    def rain_that_day(self):
        rainy_withTraffic_late = self.rainy_para * self.rainy_with_Traffic * self.rainy_withTraffic_late
        rainy_with_NoTraffic_late = self.rainy_para * self.rainy_with_NoTraffic * self.rainy_with_NoTraffic_late
        prob_late = obj.late()

        print("probability that it rained that day:", rainy_withTraffic_late + rainy_with_NoTraffic_late / prob_late)


obj = Rainy_Town()
obj.rainy()
obj.late()
obj.rain_that_day()