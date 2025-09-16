# Un sistema de biblioteca permite prestar libros a los estudiantes:
#  Se repite el siguiente menú:
# 1. Prestar libro (restar 1 del stock).
# 2. Devolver libro (sumar 1 al stock).
# 3. Consultar stock.
# 4. Salir.
#  Validar que no se presten libros si el stock es 0.
#  Al final, mostrar cuántos préstamos y devoluciones se realizaron.

actualStock= 5
borrowedBooks= 0
returnedBooks= 0

print("En la biblioteca hay, ", actualStock, " libros de matematicas disponibles.")
action= "" 
while action!= "4":
    print("Ingrese la accion que desea realizar: ")
    print("1. Prestar libro")
    print("2. Devolver libro")
    print("3. Consultar stock")
    print("4. Salir")
    action= input("Accion: ")
    if action== "1":
        if actualStock>0:
            actualStock-=1
            borrowedBooks+=1
            print("Libro prestado con exito.")
        else:
            print("No hay libros disponibles para prestar.")
    elif action== "2":
        actualStock+=1
        returnedBooks+=1
        print("Libro devuelto con exito.")
    elif action== "3":
        print("En la biblioteca hay, ", actualStock, " libros de matematicas disponibles.")
    elif action== "4":
        print("Saliendo del sistema...")
    else:
        print("Accion no valida, intente nuevamente.")
