from mode2 import *
from data_structures.heap import MaxHeap

a = Land("A", 400, 100)
b = Land("B", 300, 150)
c = Land("C", 100, 5)
d = Land("D", 350, 90)
e = Land("E", 300, 100)


sites = [a,b,c,d,e]

total = 100

for site in sites:
    site.set_available(total)

a=MaxHeap.heapify(sites)





print(a.get_max())
print(a.get_max())
print(a.get_max())
print(a.get_max())
print(a.get_max())




