#Questo programma risolve le equazioni di primo grado (ax+b=0)

import math

a = input ("ax=")
#Valore della x

b = input ("b=")
#Termine noto

if a==0:
#Se il valore della x e' 0 l'equazione e' impossibile    
     print "L'equazione e' impossibile"

elif b<0:
#In questo caso il termine noto e' minore di 0, quindi e' un numero negativp
     print ("X="),-b
     print ("  "), a

elif b>0:
#In questo caso il termine noto e' maggiore di 0, quindi e' un numero positivo
    print ("X="),b
    print ("  "),a     
