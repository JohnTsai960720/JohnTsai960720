A=10
B=25
C=31
if A<B:
    T=A
    A=B
    B=T
if C>B:
    T=B
    B=C
    C=T
if A<B:
    T=A
    A=B
    B=T
print(A,B,C)
