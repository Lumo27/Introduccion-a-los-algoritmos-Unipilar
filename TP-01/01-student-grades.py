examGrade = 0.0
totalGrades = 0.0
for x in range (0,58):
    print("Ingrese su nota, debe ser entre 0 y 10")
    examGrade= float(input("Nota: "))

    while examGrade < 0 or examGrade > 10:
            print("Error, la nota esta fuera de rango")
            print("Ingrese su nota, debe ser entre 0 y 10")
            examGrade= float(input("Nota: "))
    totalGrades= totalGrades + examGrade
    if examGrade < 4:
          print("Alumno desaprobado")
    elif examGrade >=4 and examGrade <7:
          print("Alumno a recuperatorio")
    else:
          print("Alumno aprobado")

print("El promedio final de las notas fue de: ", totalGrades/5)
    
