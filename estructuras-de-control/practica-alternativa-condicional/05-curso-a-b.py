# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al
# sexo y el nombre. El grupo A está formado por las mujeres con un nombre
# anterior a la M y los hombres con un nombre posterior a la N y el grupo B
# por el resto. Escribir un programa que pregunte al usuario su nombre y
# sexo, y muestre por pantalla el grupo que le corresponde.


name = input("Indique su nombre: ").lower()
gender = input("Indique su sexo (M para masculino, F para femeninio): ").lower()

if gender == "f" and name[0] < "m":
    print("Usted pertenece al grupo A")
elif gender == "m" and name[0] > "n":
    print("Usted pertenece al grupo A")
else: 
    print("Usted pertenece al grupo B")