'''
Załóżmy że mamy daną tablicę n-elementów i chcemy
odnaleźć w niej element x'''

import random


def linear_search():

    print('losowanie tablicy')

    L=[]
    for z in range(10):
        L.append(random.randint(0,20))
        print(L)


    print('wprowadz szukana liczbe')
    y=int(input())


    i=0

    while True:

        if y == L[i]:
            print('liczba',y,'znajduje się pod indexem:',i)
            return i
        i = i + 1


        if L==y:
            return y


print(linear_search())



'''

LUB:

'''



L=[1,2,3,6,7,8,4]
y=3
left=0
right=111111111
i = left

def linear_search():  # def linear_search(L, left, right, y):

    i = left
    while i <= right:
        if y == L[i]:
            return i
        i = i + 1
    return None

print(linear_search())




'''
LUB:
'''




import random



import random

def Szukaj(tab, element):
    i=0
    for o in tab:                  #o przyjmuje wartości każdego kolejnego elementu tablicy
        if o==element:             #jeśli znajdzie, zwraca i
            return i
        i+=1                       #dodaje do i 1
    return -1                      #jeśli nie znajdzie, zwraca -1


tab=[]                             #utworzenie tablicy
for i in range(10):
    tab.append(random.randint(0,20)) #wylosowanie wartośći

print (tab)

szukaj=[]                            #utworzenie tablicy elementów, które ma znaleźć
for i in range(5):
    szukaj.append(random.randint(0,20))

for w in szukaj:
    index=Szukaj(tab, w)
    if index>=0:
        print ("Element "+str(w)+" znaleziono na indeksie: "+str(index))
    else:
        print ("Element "+str(w)+ ' nie został znaleziony')















