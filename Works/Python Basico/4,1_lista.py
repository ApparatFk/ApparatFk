cadena="holaa"

fin=cadena[::-1]

print (cadena)
print (fin)

"""  iterable[inicio:fin:paso]

que permite extraer una serie de elementos 
del iterable, comenzando por el numerado como 
inicio y terminando por el numerado como fin-1, 
aumentando de paso en paso.

Si omites inicio se empezará en el primer 
elemento del iterable, si omites fin se terminará 
en el último elemento del iterable.

Si el paso es negativo, el iterable se recorre 
"hacia atrás", y en ese caso los valores por 
defecto cuando se omite inicio y fin se invierten.

Así pues iterable[::-1] devuelve los elementos del 
iterable, comenzando por el último y terminando por 
el primero, en orden inverso a como estaban."""