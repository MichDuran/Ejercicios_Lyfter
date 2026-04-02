# Dada n cantidad de notas de un estudiante, calcular:
# Cuantas notas tiene aprobadas (mayor a 70).
# Cuantas notas tiene desaprobadas (menor a 70).
# El promedio de todas.
# El promedio de las aprobadas.
# El promedio de las desaprobadas.

grade_counter = 1
current_grade = 0
number_of_grades_approved = 0
number_of_grades_failed = 0
average_of_grades_approved = 0
average_of_grades_failed = 0
total_grade_average = 0

total_number_of_grades = int(input("Ingrese la cantidad de notas: "))
while grade_counter <= total_number_of_grades:
    current_grade = float(input(f"Ingrese la nota {grade_counter}: "))
    #total_grade_average += current_grade
    if current_grade < 70:
        number_of_grades_failed = number_of_grades_failed + 1
        average_of_grades_failed = average_of_grades_failed + current_grade
    else:
        number_of_grades_approved = number_of_grades_approved + 1
        average_of_grades_approved = average_of_grades_approved + current_grade
    total_grade_average = total_grade_average + (current_grade / total_number_of_grades)
    grade_counter = grade_counter + 1

if number_of_grades_failed > 0:
    average_of_grades_failed = average_of_grades_failed / number_of_grades_failed
if number_of_grades_approved > 0:
    average_of_grades_approved = average_of_grades_approved / number_of_grades_approved
print(f"El estudiante tiene esta cantidad de notas desaprobadas: {number_of_grades_failed}")
print(f"Este es el promedio de notas desaprobadas: {average_of_grades_failed:.2f}")
print(f"El estudiante tiene esta cantidad de notas aprobadas: {number_of_grades_approved}")
print(f"Este es el promedio de notas aprobadas: {average_of_grades_approved:.2f}")
print(f"Este es el promedio total de notas: {total_grade_average:.2f}")
