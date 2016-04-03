
'''Zadanie polega na stworzeniu funkcji, która zwraca tzw wartość equilibrium
(oznaczymy jako i) dla danej tablicy. Jest to numer  indeksu tej tablicy,
dla którego suma wartości o indeksach mniejszych od „i” jak i większych od „i” jest taka samą.'''



def eqindexMultiPass(s):
    return [i for i in range(len(s)) if sum(s[:i]) == sum(s[i+1:])]

print (eqindexMultiPass([3,1, 2, 5, 3, 2,1]))




'''drugi sposób'''



def eqindexMultiPass(s):
    for i in range(len(s)):
        if sum(s[:i])==sum(s[i+1:]):
            return i

print (eqindexMultiPass([3,1, 2, 5, 3, 1,2]))



'''trzeci sposób'''


def it ( A ):

    dl = len(A)
    sum = 0
    prev = 0

    for i in A:
        sum += i
    for i in range(dl):
        if i==0:
            sumL=0
        else:
            prev += A[i-1]
            sumL=prev
        if i == dl - 1:
            sumR = 0
        else:
            sumR = sum - A[i] - prev
        if sumL == sumR:
            return i
    return -1

print(it([3,2,5,3,2]))



