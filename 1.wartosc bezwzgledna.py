'''Obliczanie wartość bezwzględnej danej liczby jest najprostszym przykładem
użycia algorytmu z decyzją. Dla danej liczby x wartość bezwzględna |x| wynosi:

 x jeżeli x ≥ 0,
 -x w przeciwnym wypadku.
'''
from decimal import Decimal

while True:
    print('wpisz liczbę:')
    x=int(Decimal(input()))
    if x>=0:
        wynik=x
    else:
        wynik=-x

    z=(('liczba: {0} = {1}').format(x,wynik))
    print(z)

'''
---------------------------------------------------
LUB
---------------------------------------------------
'''
def main():
 while True:
    print('wpisz liczbę:')
    x=int(Decimal(input()))
    if x>=0:
        wynik=x
    else:
        wynik=-x

    print((('liczba: {0} = {1}').format(x,wynik)))



if __name__ == "__main__":
    main()