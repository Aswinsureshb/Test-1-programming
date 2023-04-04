month = int(input("Enter the month in numeric form: "))
day = int(input("Enter the day in numeric form: "))
year = int(input("Enter the year as two numerical digits: "))

if month>12 or month<1:
    print("Error: Invalid Month Input")
elif day>30 or day<1:
    print("Error: Invalid Day Input")
elif year>99 or year<10:
    print("Error: Invalid Year Input")
else:
    print("Success: Congratulations! you entered the correct date.")
    print("The date is {}/{}/{}".format(month,day,year))


