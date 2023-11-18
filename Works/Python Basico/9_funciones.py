print("_"*20+"\n\n")


def function(var_1,var_2):
    return var_1+var_2

call=function(2,2)
print(call)


nombre      ="jesus"
apellido    ="Ferrer"

def jesus(surname,name,alias="Apparat"):
    usuario= (f"{name} {surname} {alias}")
    return usuario

call=jesus(nombre,apellido,"ApparatFK")
print(call)

def multiple (*text):
    print(text)


multiple("hola","mundo","jejej")
