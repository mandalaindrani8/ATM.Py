try:
    marks = float(input("Enter marks (0-100): "))

    if 0 <= marks <= 100:
        if marks >= 90:
            grade = "A+"
        elif marks >= 80:
            grade = "A"
        elif marks >= 70:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        elif marks >= 50:
            grade = "D"
        else:
            grade = "F"

        print("Grade:", grade)
    else:
        print("Error: Marks must be between 0 and 100.")

except ValueError:
    print("Error: Please enter a valid number.")