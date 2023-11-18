

tablero=[" "," "," "," "," "," "," "," "," "]
ganar=None
def ver_tablero(t):
    print("-------| LA VIEJA |-------\n")
    print(" "*7,t[6],"|",t[7],"|",t[8],"\n",
          " "*5,"---|---|---", "\n",
          " "*6,t[3],"|",t[4],"|",t[5],"\n",
          " "*5,"---|---|---", "\n",
          " "*6,t[0],"|",t[1],"|",t[2],
         ) 
def play():
    global ganar
    ver_tablero(tablero)    
    for i in range(10):
        ganador()
        if ganar!="" and ganar!=None or i==9:
            if ganar =="X": 
                print ("ha ganado jugador 1 ",ganar)
                break
            elif ganar=="O":
                print ("ha ganado jugador 2 ",ganar)
                break
            elif i==9:    
                print("\n      >| EMPATE |<")
                break
        if i % 2 ==0:
            print('jugador 1  "X"')
            token="X"
            jugada(token)
        elif i%2==1:
            print('jugador 2  "O"')
            token="O"
            jugada(token)
def jugada(token):
    anoto= False
    while anoto ==False:        
        try:
            posicion=(int(input(">>>")))
            if posicion <1 or posicion>9:
                continue
        except Exception:
            continue
         
        if tablero[posicion-1] ==" ":
            anoto = True  
        elif tablero[posicion-1] !=" ":
            print("posicion ocupada")

    tablero[posicion-1]=token
    ver_tablero(tablero)
def ganador():

    vertical()
    horizontal()
    diagonal()
def vertical():
    global ganar
    if tablero[6]==tablero[7]==tablero[8] !=" ":
        ganar=tablero[6]
    elif tablero[3]==tablero[4]==tablero[5] !=" ":
        ganar=tablero[3]
    elif tablero[0]==tablero[1]==tablero[2] !=" ":
        ganar=tablero[0]
def horizontal():
    global ganar
    if tablero[6]==tablero[3]==tablero[0] !=" ":
        ganar=tablero[6]
    elif tablero[7]==tablero[4]==tablero[1] !=" ":
        ganar=tablero[7]
    elif tablero[8]==tablero[5]==tablero[2] !=" ":
        ganar=tablero[8]
def diagonal():
    global ganar
    if tablero[6]==tablero[4]==tablero[2] !=" ":
        ganar=tablero[6]
    elif tablero[0]==tablero[4]==tablero[8] !=" ":
        ganar=tablero[0] 
play()



