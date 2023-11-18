import random
print("_"*20+"\n\n")


lista=[1,2,3,4,5,6,7,8,9,10]
liste=[]



def lista_agregada(num):

    for i in range(num):
        numero=random.randint(1,10)
        liste.append(numero)
    
    
    print(liste)

lista_agregada(10)








