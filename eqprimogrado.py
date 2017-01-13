#Questo programma risolve le equazioni di primo grado (ax+b=0)

import math

a = input ("ax=")
#Vadella x

b = input ("b=")
#Terminenoto

if a==0 and b==0:
    print "L'equazione e' sempre verificata"

elif a==0:
   print "L'equazione e' impossibile"

else :
    soluzione = -float (b)/float (a)
    print "La soluzione e'", soluzione 
