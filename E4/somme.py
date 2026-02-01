from cmath import sqrt
import sys
def sum(n):
    sums=0
    for i in range(0,n):
        sums=sums+i
    return sums
def sumrad(n):
    sumr=0
    for i in range(0,n):
        sumr=sumr+sqrt(n)
    return sumr
def sumprod(n):
    sump=0
    prod=1
    for i in range(0,n):
        sump=sump+i
        prod=prod*i
    return prod, sump
def pow(n,a=1):
    suma=0
    for i in range(0,n):
        suma=suma+i**a
    return suma
sys.path.append('/home/samu1019/MCF/MCF/E4')