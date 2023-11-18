
var= lambda  num_1, num_2 : num_2*(num_1+ num_2)




def suma(var_1, num_1,num_2):
    total=1
    for i in range(var_1):
        total*=var(num_1,num_2)
        print(total)
    
suma(3,2,5)
print(var(2,2))