import random



def aleatorio(cant):
    numeros=[]
    for i in range(cant):
        na=random.randint(1,6)
        numeros.append(na)
    return numeros

def suma (cant):
    suma=0
    numeros=aleatorio(cant)
    print(numeros)
    for i in range(cant):
        suma+= numeros[i]

    print(suma)


suma(3)

def sum_ten(value_superior):

    def sum_values(values):
        return values + value_superior
    return sum_values

guardado= sum_ten(10)
print(guardado(5))
print(sum_ten(1)(2))


lista=[2,5,10,25,30]

    #MAP        Recorre cada uno de los valores y aplica una funcion
def multiplicar(value):
    return value*2
print(list(map(multiplicar,lista)))

    #FILTER     Recorre cada uno de los valores y filtra valores

def mayor_ten(value): #funcion valor >10 == True
    if value >10:
        return True
    return False

def mayor_t(value): #funcion valor>10 == True => implicito (mejor)
    return value>10

print   (list(filter(mayor_ten,lista)))  #con funcion normal
print   (list(filter(mayor_t,lista)))   #con funcion mejorada
print   (list(filter(lambda value:value>10,lista))) #con lambda

    #REDUCE     opera entre los valores que va recorriendo y luego entre  el siguiente
from functools import reduce

liste=[1,2,3,3]

def sum_values(value_1,value_2):
    return value_1*value_2


print(reduce(sum_values,liste))