print("_"*20+"\n\n")

num_one,num_two = 5,"1"




try:
    print(num_one + num_two)

except TypeError as e: #solo se ejecuta el except si es TypeError    
    print(f"Type Error: {e}")#capturo el error en e

except ValueError: #solo se ejecuta el except si es TypeError
    print("Value Error")

except Exception: #capturar error general
    print("Exception")


else:#esto se produce igual si no se ejecuta except
    print("todo correcto")

finally:#se ejecuta siempre
    print("finally")













