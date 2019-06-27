from week4.Python_matplotlib.Utility.matplotlib_Utility import Util


class Multiline_matplotlib:

    def __init__(self):
        self.obj = Util()

    def draw_line(self):
        flag = True
        print("5.program to plot two or more lines on same plot with suitable legends of each line.")
        print("6.program to plot two or more lines with legends, different widths and colors.")
        print("7.program to plot two or more lines with different styles")
        print("8.program to plot two or more lines and set the line markers.")
        while flag :
            try :

                print("______________________________________")
                choice = int(input("Enter your choice"))

                if choice == 0:
                    flag = False

                elif choice == 5:
                    size = int(input("Enter the number for first line"))
                    x1_axis = self.obj.list_creation(size)
                    print(x1_axis)
                    y1_axis = self.obj.list_creation(size)
                    print(y1_axis)
                    size = int(input("Enter the number for second line"))
                    x2_axis = self.obj.list_creation(size)
                    print(x2_axis)
                    y2_axis = self.obj.list_creation(size)
                    print(y2_axis)
                    self.obj.draw_multiple_line(x1_axis, y1_axis, x2_axis, y2_axis)

                elif choice == 6:
                    size = int(input("Enter the number for first line"))
                    x1_axis = self.obj.list_creation(size)
                    print(x1_axis)
                    y1_axis = self.obj.list_creation(size)
                    print(y1_axis)
                    size = int(input("Enter the number for second line"))
                    x2_axis = self.obj.list_creation(size)
                    print(x2_axis)
                    y2_axis = self.obj.list_creation(size)
                    print(y2_axis)
                    self.obj.different_colors(x1_axis, y1_axis, x2_axis, y2_axis)

                elif choice == 7:
                    size = int(input("Enter the number for first line"))
                    x1_axis = self.obj.list_creation(size)
                    print(x1_axis)
                    y1_axis = self.obj.list_creation(size)
                    print(y1_axis)
                    size = int(input("Enter the number for second line"))
                    x2_axis = self.obj.list_creation(size)
                    print(x2_axis)
                    y2_axis = self.obj.list_creation(size)
                    print(y2_axis)
                    self.obj.different_style(x1_axis, y1_axis, x2_axis, y2_axis)

                elif choice == 8:
                    size = int(input("Enter the number for first line"))
                    x1_axis = self.obj.list_creation(size)
                    print(x1_axis)
                    y1_axis = self.obj.list_creation(size)
                    print(y1_axis)
                    size = int(input("Enter the number for second line"))
                    x2_axis = self.obj.list_creation(size)
                    print(x2_axis)
                    y2_axis = self.obj.list_creation(size)
                    print(y2_axis)
                    size = int(input("Enter the number for third line"))
                    x3_axis = self.obj.list_creation(size)
                    print(x3_axis)
                    y3_axis = self.obj.list_creation(size)
                    print(y3_axis)
                    self.obj.line_marker(x1_axis, y1_axis, x2_axis, y2_axis)

                else:
                    print("enter valid choice")
            except Exception as e:
                print(e)


obj = Multiline_matplotlib()
obj.draw_line()
