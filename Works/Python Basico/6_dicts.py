
""" DICT """
dict_1  = dict()
dict_2  = {}
dict_3  = {"sillas":{"azul","roja","verde"}}

dict_1 = {"Nombres":"jesus","Apelldos":"Ferrer","Edad":23}
dict_2 = {"lenguajes":{"python", "HTML","CSS","javaScript"} ,"Ciudad" : {"acarigua","Araure"}}


print("----------------------------------------0--------------------------------\n")
print ("dict 1:",dict_1)
print ("dict 2:",dict_2)
print ("dict 3:",dict_3)
print("----------------------------------------0--------------------------------")


print (dict_2["lenguajes"]) #acceder a datos por indice
dict_1["Personas"] = "Juan" #agregar indices y sus valores
print(dict_1)

print ( dict_2.values(),"\n\n")

