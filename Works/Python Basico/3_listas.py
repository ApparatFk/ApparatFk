#listas

lista_1 = ["jesus","alfredo","ferrer","arambulet", 23.0 , "jesus", "jesus alfredo",23] 	#manera 1 de hacer lista
lista_2	= list()																		#manera 2 de hacer lista

lista_2 = ["pepito", "clavo", "un", "clavito" , 33]


print (type(lista_1))#tipo
print (type(lista_2))

lista_1.append("jose") #agregar
print (lista_1)
print (lista_2)
print ("--------------------0--------------------")

var_1	= 23		#ingresar el valor a buscar

elemento 	=	lista_1.index(var_1)  # Index dice donde esta el valor
el_return	=	lista_1.pop(elemento) # pop elimina y retorna el valor

print (el_return)
print (lista_1)

if lista_1.count(var_1) !=0: #count cuenta elementos
	print ("hay" ,lista_1.count(var_1) ,"objetos llamados", '"',var_1,'"' )
	#del lista_1[0] #del elimina el primer elemento que se encuentre por los parametros ingresados
	
else:
	print ("no hay elementos que se llamen", var_1)

print ("--------------------0--------------------")



