print(f"-----------| LIST COMPREHETION |-----------\n")



my_list=[12,45,87,65,24,87]     #metodh 1
print(my_list)


for_list=[i for i in my_list]   #metodh 2
print(for_list)


range= range(8)                 #metodh 3
print(list(range))




def funcion(nume):    
    return nume+2

prueba= [funcion(i) for i in range]
print(prueba)