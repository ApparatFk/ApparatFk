            ### Ejercicio 1 ###
"""divisa = {'euro':'€', 'dollar':'$', 'yen':'¥'}

pre= input("Elija una divisa:\n>>>")
print(divisa[pre])"""

            ### Ejercicio 2  ###


"""nam =   input("Nombre:\n>>>")
age =   input("Edad:\n>>>")
dir =   input("Dirreccion:\n>>>")
tel =   input("Telefono:\n>>>")

datos ={"Nombre":nam,"Edad":age,"Direccion":dir,"Telefono":tel}

print (
    datos["Nombre"],"tiene",
    datos["Edad"],"años, y vive en",
    datos["Direccion"],"y su numero de telefono es",
    datos["Telefono"]
    )"""

            ### Ejercicio 3  ###


"""fruit_price  =   {"Platano":1.35,"Manzana":0.80,"Pera":0.85,"Naranja":0.70}

fruit = input("Fruta:\n>>>")
fruit = fruit.capitalize()

if fruit in fruit_price.keys():
    
    kg = int(input("¿Cuantos kg quiere?:\n>>>"))

    total= fruit_price[fruit] * kg

    print(kg,"Kg de ",fruit," son ",total,"$")
else:
    print("no se encuentra el producto")"""

            ### Ejercicio 4  ###
"""
mes={
    1:"Enero",2:"Febrero",3:"Marzo",4:"Abril",5:"Mayo",
    6:"Junio",7:"Julio",8:"Agosto",9:"Septiembre"
    ,10:"Octubre",11:"Noviembre",12:"Diciembre"
}

serch   =   input("Fecha en formato dd/mm/aaaa:\n>>>")
serch   =   serch.split("/")

print(serch[0],mes[int(serch[1])],serch[2])"""

            ### Ejercicio 5  ###

"""asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5, "Historia": 7}

cant= len(asignaturas)
asignatura  = list(asignaturas.keys())
valores     = list(asignaturas.values())
total       =   0

for i in range(cant):

    print (asignatura[i]," tiene ",valores[i]," creditos")
    total += valores[i]

print("el total de todas sus asignaciones es: ",total)"""

            ### Ejercicio 6  ###

"""persona     = {}
continuar   = True

while continuar:
    con         = True
    clave = input('¿Qué dato quieres introducir? ')
    valor = input(clave + ': ')
    persona[clave] = valor
    print(persona)
    while con == True:
        conf  = input('¿Quieres añadir más información (s/n)? ')
        if conf == "s":
            continuar = True
            con       = False
        elif conf == "n":
            continuar = False
            con       = False
        else:
            print("responda s/n")

print ("end")"""





