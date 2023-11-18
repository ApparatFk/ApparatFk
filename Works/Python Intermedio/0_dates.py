print(f"-----------| DATES |-----------\n")

from datetime import datetime

now= datetime.now()
mio= datetime(2009,1,8)


def print_date(now):    
    print(f"Fecha: {now.day}/{now.month}/{now.year}")
  

def print_hour(now):
    print(f"hora:  {now.hour}:{now.minute}:{now.second}\n")



 
print_date(mio)
print_date(now)
print_hour(now)

print(datetime(2000,4,16,3,27,40,2))


if now.minute <= 16:
    print("es la hora 8)")
elif now.minute >=17:
    print("no es la hora :,(")


years_old= now-mio #calcule cuantos años tengo con  mi fecha de nacimiento 
print(f" tengo {years_old} de edad")   #||debe ser el mismo tipo de dato (fecha/fecha)(hora/hora)

años= years_old/365
print(f"tengo {str(años)[0]}{str(años)[1]} años de edad")#calculo pero mejor