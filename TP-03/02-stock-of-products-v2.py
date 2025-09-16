# Se desea procesar la información de los productos de una fábrica de galletitas, para ello se
# lee de cada producto, su nombre, peso en gramos
#  Se sabe que el último producto, que NO se procesa, es “ZZZZZ”
#  Se desea obtener la siguiente información:
# o La cantidad de productos.
# o El peso promedio
count = 0
print("Ingrese el nombre del producto (Para finalizar ingrese 'ZZZZZ'): ")
product= input("Nombre del producto: ")
while product != "ZZZZZ":
    count += 1
    weight= int("Ingrese el peso redondo del producto")
    totalWeight += weight
    product=input("Ingrese el nombre de otro producto (Para finalizar ingrese 'ZZZZZ'): ")
print("La cantidad de productos es: ", count)
print("El peso promedio es: ", (totalWeight/count))
