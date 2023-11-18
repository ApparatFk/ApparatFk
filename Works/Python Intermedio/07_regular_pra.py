import re
abc= "esto es una cadena de texto y Textos en mayuscula y 0 numeros como 99"
abcda= "abcdefghijkmnlopqrstuvwxyz"

pattern= r"[tT]exto[ s]|mayuscula" #el pie "|" separa elementos como "esto y esto"
#es un patron donde busca la palabra "texto" con "t" o "T" y con o sin "s"
print (re.findall(pattern, abc))
print("\n")

todas=r"[aA-zZ]" #patron de letras mayusculas y minusculas
nume=r"[0-9]" #patron de solo numeros
print (re.findall(todas, abc))
print (re.findall(nume, abc))
print("\n")

todas=r"\d" #\d toma en cuenta solo numeros
print (re.findall(todas, abc))

todas=r"\D" #\d toma en cuenta todos las letras incluidas los espacios, mayusculas o minusculas
print (re.findall(todas, abc))


email="Ferrerj321@gmail.com"
emailm="jesus@gmail.com"

"""
^  = es el inicio
$  = es el final
\. = para que admita caracteres especiales que pueden ser tomados como metacaracteres
\d = solo numeros
\D = solo letras

www.regex101.com
"""
patron=r"^[aA-zZ0-9]+@['gmail']+\.[aA-zZ]+$" # patron para admirir gmail

print(re.findall(patron,email))




