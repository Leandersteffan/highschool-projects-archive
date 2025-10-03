a=1
b=0
c=0      
while 0<1: #unendlich:0<1,bis Zahl:a<x+1,Zahl:(oben a=x und hier die Whileschleife entfernen)
    b=a
    while not b==1:
        if b % 2 == 0:
            b=b/2
            c=c+1
        else:
            b=b*3+1
            c=c+1
    print(a,"#",c)
    if c>=1000: #irgendwelche Regeln wann gestoppt werden soll
        break
    a=a+1
    c=0


