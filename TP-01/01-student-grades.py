# En este ejercicio se abarca lo que pide el numero 1, y el numero 2.
examGrade = 0.0
totalGrades = 0.0
count1,count2,count3=0,0,0
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
          count1= count1 + 1 
    elif examGrade >=4 and examGrade <7:
          print("Alumno a recuperatorio")
          count2= count2 + 1
    else:
          print("Alumno aprobado")
          count3= count3 + 1

print("El promedio final de las notas fue de: ", totalGrades/5)
print("Resultados finales, desaprobados: ", count1, ", recuperatorios: ", count2, ", aprobados: ", count3)
