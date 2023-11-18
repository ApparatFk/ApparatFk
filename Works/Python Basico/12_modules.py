print("-----------| MODULOS |-----------\n")
import module                 # Modulo completo|      debo llamarlos:             module."funcion"()
from module import Operacion

#from module import suma,resta # Modulo especifico|    ya puedo llamarlo normal:   funcion()

Operacion.suma(1,2)

#suma(8,4)      sin la clase
#resta(10,5)    sin la clase

module.Operacion.suma(7,3)
module.Operacion.resta(9,3)

 
from module import Operacion as s   #le coloco el nombre que quiero con "as"

s.suma(8,5)

import math

print (math.pow(2,3))