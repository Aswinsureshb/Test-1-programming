salary = int(input("Enter the salary in Euros: "))
country = str(input("Enter the country you want to migrate: "))


def convertSalary(salary, destination):
    if destination == "Canada":
        converted_salary = salary*1.47
       
    elif destination == "USA":
        converted_salary = salary*1.18
       
    elif destination == "Cambodia":
        converted_salary = salary*4440.91
       
    elif destination == "United Kingdom":
        converted_salary = salary * 0.64
        
    else:
        print("Invalid destination")
        return None
    
    def average_salary():
        
    
