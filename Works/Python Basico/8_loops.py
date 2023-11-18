print("_"*20+"\n\n")

    ### WHILE ###
condition = 0

while condition < 4: #while condition is lower than 10    
    print (">>>",condition)
    condition += 2
else:
    print ("End while: ",condition)

while condition >=4:
    print (">>>",condition)
    condition += 20
    if condition > 50:
        print ("End while 2: ",condition) 
        break
else:
    print ("End while2: ",condition) 

    ### FOR ###
print("_"*10+"FOR"+"_"*10+"\n\n")

lista = [11,12,13,14,15]
set   = (21,22,23,24,25)
dict  = {31:"hola",32:"que",33:"bonito",34:"dia",35:"hoy"}

for element in dict.values():
   
    print(element)

for i in lista:
    print(i)
    