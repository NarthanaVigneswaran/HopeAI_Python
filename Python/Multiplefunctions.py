class Multiplefunctions:
    def subfields():
        sub_fields = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print("Sub-fields in AI are:")
        for field in sub_fields:
            print(field)

    def oddeven():
        num = int(input("Enter a number: "))
        if (num % 2) == 0:
            print(f"{num} is an Even number")
        else:
            print(f"{num} is an Odd number")

    def EligibilityForMrg():
        Gender = input("Your Gender: ")
        age = int(input("Your age: "))
        if (Gender == "Male" and age >= 21):
            print("YOU ARE ELIGIBLE")
        elif (Gender == "Female" and age >= 18):
            print("YOU ARE ELIGIBLE")
        else:
            print("NOT ELIGIBLE")

    def percentage():
        mark1 = int(input("Subject1 = "))
        mark2 = int(input("Subject2 = "))
        mark3 = int(input("Subject3 = "))
        mark4 = int(input("Subject4 = "))
        mark5 = int(input("Subject5 = "))
        Total = mark1 + mark2 + mark3 + mark4 + mark5
        print("Total:", Total)
        perc = (Total / 500) * 100
        print("Percentage:", perc)

    def Triangle():
        Height = int(input("Height: "))
        Breadth = int(input("Breadth: "))
        formula1 = "(Height * Breadth) / 2"
        area = (Height * Breadth) / 2
        print(f"Area formula: {formula1}")
        print(f"Area of Triangle: {area}")

        Height1 = int(input("Height1: "))
        Height2 = int(input("Height2: "))
        Breadth1 = int(input("Breadth1: "))
        formula2 = "Height1 + Height2 + Breadth1"
        perimeter = Height1 + Height2 + Breadth1
        print(f"Perimeter formula: {formula2}")
        print(f"Perimeter of Triangle: {perimeter}")
