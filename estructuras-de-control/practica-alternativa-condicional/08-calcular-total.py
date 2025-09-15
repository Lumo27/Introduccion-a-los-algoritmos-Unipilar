# Escribir un programa que calcula el valor total que debe pagar una persona
# para ingresar junto con su grupo familiar o amigos, sabiendo que menores
# de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5000,
# si es mayor de 18 años, 10000 y mayores de 65 años entran gratis.

edad = int(input("Indique su edad: "))
if edad < 4 or edad >= 65:
        print("Entras gratis.")
elif 4 <= edad <= 18:
        print("Debes pagar $5000.")
else:  
        print("Debes pagar $10000.")
