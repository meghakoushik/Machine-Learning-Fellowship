class Util:

    def accept_size(self):
        n = int(input("enter value number"))
        return n

    def CreateList(self, size):
        list_value = []
        for i in range(size):
            values = int(input("enter value"))
            list_value.append(values)
        return list_value

    def accept_languages(self, size):
        list_value = []
        for i in range(size):
            values = input("enter language name")
            list_value.append(values)
        return list_value

    def accept_popularity(self, size):
        list_value = []
        for i in range(size):
            values = float(input("enter value"))
            list_value.append(values)
        return list_value

    def CheckInt(self, value):
        try:
            int(value)
            return True
        except Exception:
            return False