# Escribir un programa que almacene la cadena de caracteres contraseña en
# una variable, pregunte al usuario por la contraseña e imprima por pantalla
# si la contraseña introducida por el usuario coincide con la guardada en la
# variable sin tener en cuenta mayúsculas y minúsculas.

password = input("Introduzca su contraseña")
password2= input("Vuelva a introducir la contraseña")

if password.lower() == password2.lower():
    print("Las contraseñas coinciden")
else:
    print("Error: las contraseñas no coinciden")