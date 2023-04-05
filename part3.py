def ask_for_user_input():
    salary = float(input("Enter your salary in Euros: "))
    destination = input("Enter the country you want to migrte to: " )
    return salary,destination

def is_it_a_valid_country(destination) :
    if destination == "Canada":
        return True
    elif destination == "USA":
        return True
    elif destination == "UK":
        return True
    elif destination == "Cambodia":
        return True
    else:
        return False

def convert_salary(salary,destination):
    if  destination == "Canada":
        return salary* 1.47
    elif destination == "USA":
        return salary* 0.83
    elif destination == "UK":
        return salary*0.64
    elif destination == "Cambodia":
        return salary* 4847.38 
    
def get_the_average_salary_for(destination):
    if  destination == "Canada":
        return 64000
    elif destination == "USA":
        return 56516
    elif destination == "UK":
        return 35423
    elif destination == "Cambodia":
        return 5649856
    
def compare_with_average(converted_salary,ave_salary):
    if converted_salary>ave_salary:
        return "rich"
    else :
        return "poor"
    

(salary,destination) = ask_for_user_input()
a_valid_country = is_it_a_valid_country(destination)

if a_valid_country:
    converted_salary = convert_salary(salary,destination)
    ave_salary = get_the_average_salary_for(destination)
    living_condition = compare_with_average(converted_salary,ave_salary)
    print(f"You will be {living_condition} in {destination} with a salary of {converted_salary:.2f}")
else:
    print("Invalid Country")
