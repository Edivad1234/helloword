#Questo programma risolve le equazioni di primo grado (ax+b=0)

import math

a = input ("ax=")
#Valore della x

b = input ("b=")
#Termine noto

if a==0:
#Se il valore della x e' 0 l'equazione e' impossibile    
     print "L'equazione e' impossibile"

elif a==0 and b==0:
    print "L'equazione e' sempre verificata"

elif b==0:
    print "x = 0"
else :
    soluzione = -float (b)/float (a)
    print "La soluzione e'", soluzione 
