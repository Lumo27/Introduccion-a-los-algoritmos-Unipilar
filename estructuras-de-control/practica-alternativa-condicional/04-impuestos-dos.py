estadoCivil = input("Indique su estado civil, soltero o casado: ").lower()
edad=int(input("Indique su edad: "))
ingresos=float(input("Indique sus ingresos mensuales:"))


if estadoCivil == "soltero" and edad > 16 and ingresos >= 1000:
    print("Usted debe tributar impuestos")
elif estadoCivil == "casado" and edad > 18 and ingresos >= 700:
    print("Usted debe tributar impuestos")
else:
    print("Usted no debe tributar impuestos")