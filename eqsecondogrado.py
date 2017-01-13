import math

a = input ("ax^2=")
#Coefficente della x^2
b = input ("bx=")
#Coefficente della x
c = input ("c=")
#Termine noto

if a==0 and b==0 and c==0:
    print "Non e' valida."

elif a==0 and b==0:
    print c ,"=0"

elif a==0:
    r= float(c)/float(b)*(-1.0)
    print "x=",r

else:
    delta = pow(b, 2) - 4.0*(a*c)

    if delta<0 :
               print "L'equazione con delta minore di 0, e' impossibile"

    else:    
        soluz=((-b)+math.sqrt(delta))/(2.0*a)
        soluz2=((-b)-math.sqrt(delta))/(2.0*a)
        print "Le soluzioni sono, x1=", soluz, "e x2=", soluz2

