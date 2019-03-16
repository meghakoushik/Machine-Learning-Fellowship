#program to count the number occurrence of a specific character in a string.

Text_character = "programming"
count = 0

for j in Text_character:
    if j == 'm':
        count = count + 1

# printing result
print("Count of m in programming is :" + str(count))

