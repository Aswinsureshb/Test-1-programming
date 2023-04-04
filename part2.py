color1 = str(input("Enter the first primary color in lower case letters: "))
color2 = str(input("Enter the second primary color in lower case letters: "))

RED = "red"

BLUE = "blue"

YELLOW = "yellow"

if color1 != RED and color1 != BLUE and color1!= YELLOW:
    print("Error:Invalid Color1")
if color2 != RED and color2 != BLUE and color2!= YELLOW:
    print("Error invalid Color2")
elif color1 == color2:
    print("Error: The two colors you entered are same")
else:
    if color1 == RED and color2 == BLUE:
        print("purple")
    elif color1 == RED and color2 == YELLOW:
        print("orange")
    elif color1 == BLUE and color2 == RED:
        print("purple")
    elif color1 == BLUE and color2 == YELLOW:
        print("green")
    elif color1 == YELLOW and color2 == RED:
        print("orange")
    elif color1 == YELLOW and color2 == BLUE:
        print("green")
    else:
        print("invalid")
