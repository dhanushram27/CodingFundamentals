def leap_year(year):
    if (year%400 == 0) or (year%4 ==0 and year%100 != 0):
        return "its an LeapYear"
    else:
        return "Its Not an Leapyear"

user = int(input("Enter The Year : "))
print(leap_year(user))
