print(f"\n____________CONVERTIDOR A NUMEROS ROMANOS____________\n\n")

i=[]
#ingresar numero
n=388        


def diez(n): #1 al 9
    if n >0 and n <4:
        for f in range(n):
            i.append("I")      
    elif n ==4:
        i.append("I") 
        i.append("V")  
    elif n ==5:
        i.append("V")
    elif n >5 and n<9:
        i.append("V")
        for f in range(n-5):
             i.append("I")
    elif n==9:
        i.append("I")  
        i.append("X")     

def cincuenta(n): #10 al 49
    if n >=10 and n<=39:
        for f in range(pri):
            i.append("X")
    elif n >30 and n<50:
        if n >=40 and n <50:
            i.append("X")
            i.append("L")
    elif n>50 and n<60:
        i.append("L")
  
def cien(n): #50 al 99
    if n ==50:
        i.append("L")
    elif n> 59 and n<= 89:
        if n>=50 and n<=89:
            i.append("L")
        for f in range(pri-5):
            i.append("X")
    elif n>=90 and n<=99:
        i.append("X")
        i.append("C")

def treciento(n):   #100 al 399
    if n ==100:
        i.append("C")
    elif n>100 and n<=399:        
        for f in range(sec):
            i.append("C")


sec=int(str(n)[0])

if n>=100 and n< 399:
    treciento(n)
    if n>100 and n<400:
        n=n-sec*100

pri=int(str(n)[0]) 

if n >49 and n<100:  
    cien(n)

if n >9 and n <89: 
    cincuenta(n)

if n >10:
    n=n-pri*10

diez(n)

print(i)
