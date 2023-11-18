print(f"-----------| CARRITO |-----------\n")
import os
tienda = {"tomate":0.8, 
          "cebolla":1.5, 
          "papa":8, 
          "ajo":0.15, 
          "aguacate":5.9}
l_cli={}


def factura(i):

    iva=i
    
    factura=0
    end = True
    c =True
    while end:       

        prod= input("Ingrese el articulo\n>>")
        prod=prod.lower()          

        if prod in tienda:

            kg= float(input("¿Cuantos Kg quere?\n>>"))

            if prod in l_cli:
                to=l_cli[prod]+kg
                l_cli[prod]=to
            else:
                l_cli[prod]=kg

            carrito = tienda[prod]*float(kg)
            factura += carrito
            total= factura*(iva*0.01)
            print(f"{int(factura)}Bsf.  IVA:{iva}% TOTAL: {round(total+factura,2)}Bsf.")
            

            while c==True:
                conf=input("¿desea agregar mas productos?(S/N)\n>>")
                if conf.lower() == "s":                    
                    end=True
                    break
                elif conf.lower()=="n":
                    end=False
                    break
                else:
                    continue
        else:
            print("no se encuentra el producto")
    os.system("cls")
    for i in l_cli:
        print(f"{i} {l_cli[i]}Kg {int(tienda[i]*l_cli[i])}Bsf.")
    print(f"\n{int(factura)}Bsf.  IVA:{iva}% TOTAL:{round(total+factura,2)}Bsf.")


factura(21)

