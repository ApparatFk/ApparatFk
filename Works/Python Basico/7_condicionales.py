print("_"*20+"\n\n")


condition_t = True

if condition_t:
    print ("boolean is: ",condition_t)

condition = 5*5

if condition >= 10 and  condition <= 20:
    print ("condition is ecual to : ",int(condition))

elif condition == 25:
    print ("elif is ecual to : ",int(condition))
else:
    print("condition is`nt on the parameters")

string = ""

if string:
    string = bool(string)
    print("True? ",string)
else:
    string = bool(string)
    print("False? ",string)

if not string:
    string = bool(string)
    print("secont if: ",string)