import math

a = input("Inserire 1 per calcolare il volume del cubo o 2 per calcolarlo della sfera: ")

if a==0:
   print "Inserisci un valore diverso da 0"

elif a==1:
   b = input("Stai calcolando il volume del cubo, inserisci il valore di un lato: ")
   print "Il volume del cubo e' uguale a", b*b*b

elif a==2:
   c = input("Stai calcolando il volume di della sfera, inserisci il valore del raggio: ")
   print "Il volume della sfera e' uguale a", (math.pi*4.0*(c*c*c))/3.0 
