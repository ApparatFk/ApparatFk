print(f"-----------| CHALLENGE |-----------\n")
import random

def fizzbuzz():
    for i in range(1,21):
        if i %3==0 and i%5==0:
            print(f"fizzbuzz")
            continue
        elif i % 3 == 0:
            print("fizz")
            continue
        elif i%5==0:
            print("buzz")
            continue
        print(i)

def anagram(w_1,w_2):

    if w_1.lower() == w_2.lower():
        print("es la misma palabra")
    elif sorted(w_1.lower()) == sorted(w_2.lower()):
        print("es un anagrama")
    else:
        print("no es anagrama")

def fibonacci():

    prev=0
    next=1
  
    for i in range(50):

        print(prev)
        fib=prev+next
        next=prev
        prev=fib
        if prev >= 50:
            break
        
def primo(num):
    a=0
    for i in range(num+1):
        if i > 1:
            if num % i ==0: 
                a +=1
    if a >=2:
        print("no es primo")
    elif a==1:
        print("es primo")       

def iva():

    compra = {tomates:0.8, cebolla:1.5, papas:8, ajo:0.15, aguacate:5.9}


    print(compra)
   
    


