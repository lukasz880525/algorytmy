'''mamy daną tablicę n-elementów i chcemy obliczyć ich sumę.'''



def main():
    
    wynik=0
    print('podaj ilosc elementów listy')
    ilosc=int(input())

    for x in range(ilosc):
        print ("Podaj wartość elementu numer {0}: ")
        x = int(input())
        wynik=wynik+x
        print (wynik)
    return -1

if __name__== '__main__':
    main()



'''
----------------------------------
ALBO
---------------------------------
'''


wynik=0

for i in range(5):
    if i >=1:
        wynik=wynik+i

print(wynik)



'''
-------------------------------------------
ALBO
-----------------------------------------

'''


a=[1,2,3,4,5]

x=sum(a)
print(x)

