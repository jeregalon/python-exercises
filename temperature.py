# example of exceptiong handling

while 1:
    try:
        temperature = float(input('Enter current temperature: '))

        if temperature > 0:
            print("Above zero")
        elif temperature < 0:
            print("Below zero")
        else:
            print("Zero")
    except ValueError:
        print("You must enter a number")