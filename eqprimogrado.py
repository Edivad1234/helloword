#Questo programma risolve le equazioni di primo grado (ax+b=0)

import math

a = input ("ax=")
#Valore della x

b = input ("b=")
#Termine noto

if a==0:
#Se il valore della x e' 0 l'equazione e' impossibile    
     print "L'equazione e' impossibile"
else:

        if a % b==0:
             x = a/-b
             print ("X="),x 
        
        else: 
          if (a%2==0) and (b%2==0):
             a = a/2
             b = b/2 
             print ("X="),-a
             print ("   "),b
           
          
          elif (a%3==0) and (b%3==0):
                a = a/3
                b = b/3
                print ("X="),-a
                print ("   "),b
             
          
          elif (a%5==0) and (b%5==0):
                      a = a/5
                      b = b/5
                      print ("X="),-a
                      print ("   "),b
               
