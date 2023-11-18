


class Personaje():
    def __init__(self,name,healt=100,atack=25,mana=30):  #estadisticas base del personaje
        self.chr=name.upper()
        self.hp=healt
        self.atk=atack
        self.mn=mana
        self.exp=0
        self.lvl=1
        self.req=50
        

    def lvl_up(self):        #subir de nivel     
        if self.exp >= self.req:
            self.hp = 100     #aqui curo al personaje
            self.mn = 30

            self.exp-=self.req #le subo las estadisticas cuando sube de nivel
            self.req+=25
            self.hp+=15*self.lvl
            self.atk+=5*self.lvl
            self.mn+=25*self.lvl
            self.lvl+=1
            print(f"  LVL {self.lvl}+\n {self.chr}\nHP   |{self.hp}\nATK  |{self.atk}\nMANA |{self.mn} \nEXP {self.exp}|{self.req} ")

    def resume(self):  #resumen de estadisticas del  personaje
        print(f"{self.chr} HP {self.hp} MANA {self.mn}")


    def ataque(self,enemy): #accion de atacar al enemigo
        enemy.hp-= self.atk-enemy.arm
        print(f"{self.chr} atacó a enemy -{self.atk-enemy.arm}")

    def curar(self):  #accion de curar al personaje
        if self.mn >=25:
            self.mn-=25
            self.hp+=70
            print(f"{self.chr} Se curó +70")

    def magia(self,enemy): #accion de usar magia de ataque al enemigo
        if self.mn>=30:
            self.mn-=30
            enemy.hp-=80
            print(f"{self.chr} Uso magia  Enemy -80")



class Enemy():  #estadisticas base del enemigo
    def __init__(self,healt=125,atack=15,armor=10):
        self.hp=healt
        self.atk=atack
        self.arm=armor
        self.exp=50

    def ataque(self,pj):    #ataque del enemigo al personaaje
        pj.hp-=self.atk
        print(f"enemy atacó a {pj.chr} -{self.atk}")


    def resume(self):   #resumen de estadisticas del enemigo
        print(f"ENEMY   HP {self.hp}")
    


def win(enemy,char): #determina quien gana y sube de nivel si es necesario
    if enemy.hp <=0:
        char.exp+=enemy.exp  #si gana personaje le suma exp
        char.lvl_up()        #si tiene la exp suficiente sube de nivel
        return print(f"{char.chr} WINs")
    if char.hp <=0:
        return print(f"ENEMY WINs")
        


def combate (char,enemy):  #inicia combate
    while char.hp > 0 and enemy.hp > 0:
        print("-----------| RPG |-----------\n")
        char.resume()
        enemy.resume()

        try:
            accion = int(input("1. Atacar\n2. Curarte\n3. Magia\n>>")) #selecciona accion a realizar
        except Exception:
            continue
        if accion ==1:  #si accion 1 ataca
            char.ataque(enemy)
            enemy.ataque(char)
        elif accion==2: #si accion 2 se cura
            
            if char.mn <25:
                print("no hay mana")
            else:
                char.curar() 
                enemy.ataque(char)
        elif accion==3: #si accion 3 usa magia
            if char.mn<30:
                print("no hay mana")
            else:
                char.magia(enemy)
                enemy.ataque(char)
        else:
            continue
    
char=Personaje("Julio") #creo un personaje con un nombre
enemy=Enemy()   #creo un enemigo
enemy2=Enemy()  #creo otro enemigo
enemy3=Enemy()  #creo otro enemigo
enemy4=Enemy()  #creo otro enemigo

combate(char,enemy)  #combate con enemigo 1
print("-----------| RPG |-----------\n")      
win(enemy,char) 

combate(char,enemy2) #combate con enemigo 2
print("-----------| RPG |-----------\n")      
win(enemy2,char) 

combate(char,enemy3) #combate con enemigo 3
print("-----------| RPG |-----------\n")      
win(enemy3,char) 

combate(char,enemy4) #combate con enemigo 4
print("-----------| RPG |-----------\n")      
win(enemy4,char) 

    




