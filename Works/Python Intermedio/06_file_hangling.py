print("--------------| FILE HANDLING|--------------\n\n")





texto=open("Python Intermedio/fichero.txt","r+")


for i in texto.readlines():
    print(i)
texto.close()







