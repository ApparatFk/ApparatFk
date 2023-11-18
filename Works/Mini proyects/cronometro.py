import os
import time

hor,minu,sec=2,0,30

while True:
    sec-=1
    time.sleep(0.1)    
    if sec ==-1:
        minu-=1
        sec=59
    if minu==-1:
        hor-=1
        minu=59
    os.system("cls")
    print (f"{hor}:{minu}:{sec}")
    if hor<=0 and minu<=0 and sec<=0:
        break