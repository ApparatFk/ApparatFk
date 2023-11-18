""" SETS """

new_set = set()
secont_set = {}

print (type(new_set))  		#set
print (type(secont_set))  	#dictionary

secont_set = {"jesus", "ferrer",23}
new_set = {"pepito", "clavo","un clavito", 2000}

print (type(secont_set))	#set now
print (len(secont_set))

		### Un set siempre es desordenado y no se repiten datos ###
secont_set.add("alfredo")
print (secont_set)
secont_set.add("alfredo")
print (secont_set)
 
print ("jesus" in secont_set) #true

print ("_________________________0__________________________")
print (secont_set)

lista = list(secont_set)

print (type(lista))

union_list = (new_set.union(lista))  #practicar different/ upset etc
print (union_list)
print (type(union_list))
print ("_________________________0__________________________")















