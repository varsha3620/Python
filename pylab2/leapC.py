import calendar
year=int(input("Enter the year to check:"))
if calendar.isleap(year):
	print(f"{year}is a leap year")
else:
	print(f"{year} is not a leap year")

