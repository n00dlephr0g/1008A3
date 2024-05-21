from mode2 import *

a = Land("A", 400, 100)
b = Land("B", 300, 150)
c = Land("C", 100, 5)
d = Land("D", 350, 90)
e = Land("E", 300, 100)


sites = [a,b,c,d,e]

total = 100
sending = 100


a=scoremergesort(sites,total,sending)

for site in a:
    print(site.score(total, sending))




