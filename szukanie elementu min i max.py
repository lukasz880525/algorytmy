'''Załóżmy że mamy daną tablicę n-elementów i chcemy odnaleźć w niej
element minimalny (bądź maksymalny).'''
import random


def max(z):
    m=z[0]
    for t in z:       #pętla for przyjmuje wartości kolejnych komórek tablicy tab
        if t>m:
            m=t
    return m

def min(g):
    m=g[0]
    for k in g:
        if k<m:
            m=k
    return m

tab=[]      #utworzenie tablicy

for i in range(10):
    tab.append(random.randint(0,20))   #wylosowanie wartośći


print ("tablica: ",tab)           #wypisanie całej tablicy
print ("min: ",min(tab))
print ("max: ",max(tab))



'''
-------------------------
ALBO
-------------------------
'''



a=[3,3,2,5,4,6,1]

m=a[0]

for x in a:
    if m<x:
        m=x
print(m)

for y in a:
    if m>y:
        m=y
print(m)




'''
-----------------------------
ALBO
-----------------------------
'''

a=[3,3,2,5,4,6,1]

z=('wartosc min=',min(a),'wartosc max=',max(a))

print(z)







