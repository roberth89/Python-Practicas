# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés porcentual anual y el número de años,
# y retorne el capital obtenido en la inversión redondeado con dos decimales.

def calcularInteres(cantidadDinero, interesAnual, annos):
    resultado = round( cantidadDinero * (interesAnual / 100 + 1) ** annos,2)
    return resultado

cantidadDinero = float(input("Cantidad Dinero : "))
interesAnual = float(input("Interes Anual : "))
annos = int(input("Años : "))
print("Total: " + str(calcularInteres(cantidadDinero,interesAnual ,annos)))

 # Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. 
 # Escribir la función usando el bucle for anidado.
 
def superPosicion(lista1, lista2): 
    bandera = False
    for i in lista1:
        for j in lista2:
            if i == j:
                return True
    return bandera

lista1 = [1,3,4,5,6]
lista2 = [9,8,11,9,3]
print("Resultado superPosicion: " + str(superPosicion(lista1, lista2)))


