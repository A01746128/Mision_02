#Miguel Castillo Ordaz
#Calcula el costo total de una comida en un restaurante
Análisis:
    
E: Escribe el costo total de la comida.
S: El subtotal, la propina, el IVA, el total a pagar.
E/S: Agregar el 13% de propina al total de la comida, agregar el 16% de IVA a la comida, hacer la suma total del producto.

Algoritmo:

subtotal= int(input("Teclea total a pagar de la comida: "))
productouno= subtotal*.13
productodos= subtotal*.16
pt= productouno + productodos + subtotal
print(“El costo total de la comida es: (subtotal) Propina: %d2d IVA: %02d%2d Total a pagar %03%2d”  % (productouno,productodos,pt)) 
