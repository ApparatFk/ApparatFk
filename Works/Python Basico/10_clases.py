print("_"*20+"\n\n")



class CharOne:
    def __init__(self, name,surname,alias="sin alias"):#alias tiene dato por defecto
        self.full_name=f"{name} {surname} ({alias})"
    
    def walk(self): #llamada a datos propios atravez de "self"
        print(f"{self.full_name} esta caminando")



persona= CharOne("jesus","Ferrer")  #la variable persona             =>  ahora es la clase
print(persona.full_name)            #llamada a variable constructora =>  atravez de la variable clase
persona.walk()                      #llamada a funcion de la clase   =>  atravez de la variable clase


persona_2 = CharOne("Juan","miguel",alias="Koko")
print(persona_2.full_name)          #Creo una 2da persona sin modificar el 1ero
print(persona.full_name)