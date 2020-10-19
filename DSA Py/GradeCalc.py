def simpleGrdaeCalc(grades):
    points = {"A+": 4.0, "A": 4.0, "A-": 3.67, "B+": 3.33, "B": 3.0, "B-": 2.67,
              "C+": 2.33, "C": 2.0, "C-": 1.67, "D+": 1.33, "D": 1.0, "F": 0.0}

    number_of_courses = 0
    total_points = 0
    for grade in grades:
        if grade not in points:
            print(f'Unknown Grade {grade} being ignored')
        else:
            number_of_courses += 1
            total_points += points[grade]
    if number_of_courses > 0:
        return total_points / number_of_courses


print(simpleGrdaeCalc(['A+', 'A-', 'A-']))
