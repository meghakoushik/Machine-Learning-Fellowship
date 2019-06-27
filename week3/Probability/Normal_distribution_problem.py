"""10. X is a normally normally distributed variable with mean μ = 30 and standard
deviation σ = 4. Write a program to find
a. P(x < 40)
b. P(x > 21)
c. P(30 < x < 35)"""


class Normal_distributed():

    def __init__(self):
        self.num_one = 40
        self.mean = 30
        self.standard_deviation = 4
        self.total_area = 1
        self.num_two = 21
        self.num_three = 30
        self.num_four = 35
        self.z_1 = 0.9938
        self.z_2 = 0.0122
        self.z_3 = 0.8944

    # 1st problem:P(x < 40)
    def Z_value_first(self) :
        Z_value = (self.num_one - self.mean) / self.standard_deviation
        print("Z_value is =  ", Z_value)
        if Z_value <= 2.5 :
            print("area of left side:", self.z_1)

    # 2nd problem:P(x > 21)
    def Z_value_second(self):
        Z_value = (self.num_two - self.mean) / self.standard_deviation
        print("Z_value is = ", Z_value)
        if Z_value <= -2.25 :
            print("area of left side:", self.z_2)
            area = self.z_2 - self.total_area
            print("total area:", area)

    # 3rd problem: P(30 < x < 35)
    def Z_value_third(self) :
        Z_value_one = (self.num_three - self.mean) / self.standard_deviation
        print("Z_value_first is = ", Z_value_one)
        Z_value_two = (self.num_four - self.mean) / self.standard_deviation
        print("Z_value_second is = ", Z_value_two)
        if Z_value_one < 1.25 :
            area_half = 0.5
            print("area of left side:", self.z_3)
            total_area = self.z_3 - area_half
            print("total area:", total_area)


obj = Normal_distributed()

flag = True

print("1.program to find : P(x < 40) ")
print("2.program to find : P(x > 21). ")
print("3.program to find :  P(30 < x < 35)")
print("0. exit")

while flag :

    try :

        print('____________________________________')

        choice = int(input("Enter your choice"))

        if choice == 0 :
            flag = False

        elif choice == 1 :

            obj.Z_value_first()

        elif choice == 2 :
            obj.Z_value_second()

        elif choice == 3 :
            obj.Z_value_third()

        else :
            print("\nenter input within 1-3 choice")
    except Exception as e :
        print(e)
