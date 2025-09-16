# Se realiza una encuesta de satisfacción a clientes hasta que se ingrese la palabra "fin".
#  Cada cliente califica del 1 al 5.
#  Recorrer las respuestas para contar cuántas son 4 o 5 (clientes satisfechos).
#  Clasificar: 1–2 = “malo”, 3 = “regular”, 4–5 = “bueno”.
#  Al final, mostrar: cantidad total de clientes, cantidad de satisfechos, y porcentaje de
# satisfacción, cantidad de no satisfechos y porcentaje de no satisfechos

calificacion = ""
print("Ingrese calificacion sobre su satisfaccion, (1-5) o 'fin' para terminar:")
calificacion= input("Calificacion: ")
while calificacion!= "fin" and calificacion<6 and calificacion>0:
    calificacion= int(calificacion)
    if calificacion<3:
        count_bad +=1
    if calificacion==3:
        count_regular +=1
    if calificacion>3:
        count_good +=1
    count_total_clients +=1
print("Cantidad total de cleintes: ", count_total_clients)
print("Cantidad de clientes satisfechos: ",count_good)
print("Porcentaje de clientes satisfechos: ",(count_good/count_total_clients)*100,"%")
print("Cantidad de clientes no satisfechos: ",count_bad+count_regular)
print("Porcentaje de clientes no satisfechos: ",((count_bad+count_regular)/count_total_clients)*100,"%")


