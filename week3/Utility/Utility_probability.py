class Util :
    """ 1. Write a program to find probability of drawing an ace from pack of cards"""

    def ace_cards(self, ace, cards) :
        Probability_result = ace / cards
        return Probability_result

    "----------------------------------------------------------------------------"

    """2. Write a program to find the probability of drawing an ace after drawing a king on
        the first draw"""

    def ace_king(self, king, new_cards) :
        probability_king = king / new_cards
        return probability_king

    "-------------------------------------------------------------------------------"

    """3. Write a program to find the probability of drawing an ace after drawing an ace on
        the first draw"""

    def ace_ace(self, new_cards, cards) :
        Ace_result = cards / new_cards
        return Ace_result
    "-------------------------------------------------------------------------------"

    """4.You toss a fair coin three times write a program to find following:
        A). What is the probability of three heads, HHH?"""

    def count_probHHH(self, len_Probabilities, HHH_Probabilities) :
        HHH_Result = HHH_Probabilities / len_Probabilities
        return HHH_Result

    """B) What is the probability that you observe exactly one heads?"""

    def One_HHH(self, len_Probabilities, length_OneHead) :
        prob_oneH = length_OneHead / len_Probabilities
        return prob_oneH

    """C) Given that you have observed at least one heads, what is the probability
         that you observe at least two heads?"""

    def at_least_one(self, Probabilities, len_Probabilities) :
        count_TTT = Probabilities.count('TTT')
        print("\n count of TTT", count_TTT)
        one_Head = (len_Probabilities - count_TTT) / len_Probabilities
        return one_Head

    def at_least_two(self, Probabilities, len_Probabilities) :
        list = [ ]
        for temp in Probabilities :
            count = 0
            for char in temp :
                if char == 'H' :
                    count += 1
            if count >= 2 :
                list.append(temp)
        len_atleastOne = len(list)
        print("\n Two Head ", len_atleastOne)
        result = len_atleastOne / len_Probabilities
        return result
    "--------------------------------------------------------------------------------------"
    """5 A)What is the probability that it's not raining and there is heavy traffic and I
         am not late?"""

    def NoRainy_Traffic_NoLate(self, not_rainy, not_rainy_with_Traffic, not_rainy_with_Traffic_Nolate) :
        probability = not_rainy * not_rainy_with_Traffic * not_rainy_with_Traffic_Nolate
        return probability
