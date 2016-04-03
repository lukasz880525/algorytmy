'''Załóżmy że mamy daną tablicę n-elementów i chcemy policzyć
ile razy występuje w niej element o wartości x'''



while True:
    wynik=0
    a=[1,2,3,4,2,1,5,2,2,2,2,1,1]
    print('wpisz szukaną liczbę:')

    liczba = int(input())

    for x in a:
        if x==liczba:
            wynik+=1
    print('liczba:' ,liczba,'wystepuje', wynik, 'razy')



