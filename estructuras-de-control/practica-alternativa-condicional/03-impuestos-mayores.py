print("Para tributar impuestos, debe ser mayor de 16, y ademas, ingresos iguales o superiores a 1000$ mensuales")

edad = int(input("Ingrese su edad en numeros:"))
ingresos= float(input("Ingrese sus ingresos mensuales: "))

if edad > 16 and ingresos >= 1000:
    print("Usted debe tributar impuestos")
else:
    print("Usted no debe tributar impuestos aun")
    