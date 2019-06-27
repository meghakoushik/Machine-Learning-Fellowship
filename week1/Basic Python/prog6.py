# program to calculate number of days between two dates
# date class is import from the datetime module
from datetime import date
first = date(2014, 7, 2)           # FIRST DATE
second = date(2014, 7, 11)         # SECOND DATE
diff = second-first                # DIFFERENCE BETWEEN TWO DATE
print(diff.days)                   # PRINT DAYS BETWEEN TWO DAYS