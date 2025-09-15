num1 = int(input("Ingrese primer numero:"))
print(num1)
num2 = int(input("Ingrese segundo numero:"))
print(num2)

if (num1 == 0 or num2 == 0) :  
    print("Error: alguno de los dos numeros es cero")
else:
    print("El resultado de la division es:", (num1 / num2))