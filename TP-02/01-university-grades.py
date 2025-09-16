# 1) Registro de Calificaciones en una Universidad
# Se registran notas de estudiantes hasta que se ingrese -1.
#  Por cada estudiante, leer 3 notas y calcular su promedio.
#  Si el promedio ≥6, contar como aprobado.
#  Al final, mostrar cantidad de estudiantes evaluados, promedio general del curso, y porcentaje
# de aprobados.
count=0
examGrade=0
examGrade1=0
examGrade2=0
examGrade3=0
average=0
averageGeneral=0
countApproved=0
print("Registro de calificaciones para la universidad, para finalizar ingrese -1")

examGrade= float(input("Para evaluar, ingrese un numero distinto a -1"))
while examGrade != -1:
    count = count + 1 
    examGrade1= float(input("Primera nota: "))
    examGrade2= float(input("Segunda nota:"))
    examGrade3= float(input("Tercer nota"))
    average = (examGrade1 + examGrade2 + examGrade3) / 3
    averageGeneral = averageGeneral + average
    if average >= 6: 
        print("Alumno aprobado")
        countApproved= countApproved + 1
    else:
        print("Alumno desaprobado")
    examGrade= float(input("Para ingresar un nuevo alumno, ingrese un numero distinto a -1"))
if count > 0 :
    averageGeneral = averageGeneral / count
    print("La cantidad de alumnos evaluados fue: ",count)
    print("La cantidad de alumnos aprobados fue: ",countApproved)
    print("El promedio general del curso fue: ", averageGeneral)
    print("El promedio de aprobados fue: ", ((countApproved*100)/count))
else:
    print("Error, no se ingreso ningun alumno, fin del programa")