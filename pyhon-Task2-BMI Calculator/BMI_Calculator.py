def bmi(w, h):
     return w / (h * h)

while True:
    while True:
        try:
            weight = float(input("Enter your weight(in KG) : "))
            while weight <= 0:
                print("Weight must be greater than 0.")
                weight = float(input("Enter your weight(in KG): "))
            height = float(input("Enter your height(in Meter) : "))
            while height <= 0:
                print("Height must be greater than 0.")
                height = float(input("Enter your height(in Meter) : "))
            break
        except ValueError:
            print("Enter a valid number not alphabet")

    BMI=bmi(weight, height)

    print ("\nYour Weight is ",weight)
    print ("Your Height is ",height)

    print(f"\nYour BMI is {BMI:.2f}")

    if BMI < 18.5:
        print("BMI Category : Underweight")
    elif BMI <= 24.9:
        print("BMI Category : Normal ")
    elif BMI <= 29.9:
        print("BMI Category : Overweight ")
    else:
        print("BMI Category : Obese ")

    repeat = input(
        "\nIf you want to calculate BMI again enter 'yes' or for exit enter 'no' : "
    ).lower()
    print("\n")
    while repeat not in ["yes", "no"]:
        print("Enter valid input")
        repeat = input(
            "If you want to calculate BMI again enter 'yes' or for exit enter 'no' :\n "
        ).lower()
    if repeat == "no":
        print("Thank you")
        break
