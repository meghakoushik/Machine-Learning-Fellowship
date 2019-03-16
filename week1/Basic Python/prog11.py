# Program to check whether a file exist
# using file handling concept
try:
    f = open('myfile.txt')
    f.close()

except FileNotFoundError:
    print("File Not exist")
