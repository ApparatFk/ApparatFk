print("\n\n")
diccionario = {"Mes":{"enero","febrero","marzo"},"Dia":{1,2,3}}
print(diccionario)

print (diccionario.get("juan",False)) #.get(key,value) busca valores de la key y si no la encuentra return value

rest = list(diccionario.values())
print (rest)

print (diccionario.keys())

"""val = input("buscar mes:\n>>>")
meses   = list(diccionario["Mes"])

mes= meses.index(val)
print (meses[mes],"encontrado")"""

print("_"*15+"0"+"_"*15+"\n\n")


