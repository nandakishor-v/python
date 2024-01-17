# Program to display calendar of the given month and year
import calendar
import bu

# To take year input from the user
yy = int(input("Enter year: "))

# Display the calendar for all months in the given year
for mm in range(1, 13):
    print(calendar.month(yy, mm))
