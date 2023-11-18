print("------------|Movimiento Rectilineo Uniforme|------------")

#3.23h 225.3km maracay/acarigua
velocidad=4
distancia=0
tiempo=8.0


def  time(t):
    m=t*60   
    return round(m,2) 


def calculo(d=0,v=0,t=0):
   
    if type(t) != float:
        t=time(t)
    
    if v == 0:
        v= d/t   
    if t == 0:
        t=d/v
    if d == 0:
        d= v*t

    print(f"velocidad: {round(v,2)}Km/h\ndistancia: {round(d,2)}Km\ntiempo: {t}h")


calculo(distancia,velocidad,tiempo)






