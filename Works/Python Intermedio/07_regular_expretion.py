print("----------------| Expresiones regulares |--------------\n")


import re


abc= "expresiones regulares son comandos para validar cadenas de texto Expresiones"
cba= "las expresiones no regulares"


# match solo busca en primera posicion
print(re.match("las expresiones regulares", cba))
print(re.match("las expresiones regulares", abc))
print(re.match("cadenas de texto", abc))
print("\n")


match= re.match("expresiones regulares", abc)
start, end= match.span() #span busca el rango encontrado 
print(match)
print(start,end)
print (abc[start:end])

# formas de hacer el "si no" : not(match == None)  : match != None : match is not None
if match is not None:
    print (abc[start:end])
print("\n")


# search funciona igual a match pero puede buscar en cualquier posicion
search =re.search("expresiones", abc)
start,end=search.span()
print(abc[start:end])
print("\n")


#findall encuentra todas las posibles opciones en una lista por tanto no posee atributo span
findall = re.findall("expresiones", abc)
vc= len(findall)
print(findall, vc)
for i in range(vc-1):
    if vc > 1:
        findall.remove(findall[0])
print(findall)
print("\n")

#split separa cadenas de textos como elementos de una lista separandolos por un parametro
split= re.split(" ",abc)
index= split.index("para") #busco elemento de la lista con el index
print(split)

if "expresiones" in split:
    print(split[index])


#sub substituye elementos en una cadena de texto
print(re.sub("[e|E]xpresiones","EXPRESIONES", abc)) 
# el "[|]" puede elegir uno o el otro para la condicion