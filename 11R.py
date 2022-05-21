#genertae divisor of number
def divisor() :
    n= int(input('enter no : '))
    for i in range(1,n+1):
        if n%i == 0:
            print(i)\
#output
'''4321
432
21
1'''
for i in range(1,5):
    for j in range(5,i,-1):
        print(j)
    else:
        print()

#for factorial od no.
def fact():
    n=int(input('enter no : '))
    fact=1
    a=1
    while a <= n :
        fact*=a
        a+=1
    print(fact)


#for palindrome : no palindrome or not
n=int(input('enter no. : '))
res=0
while n>0:
    rem=n%10
    res=rem+res*10
    n=n//10
if res==n:
    print("p")
else:
    print("not p")


#fibonacci:e.g. .. 0 1 1 2 3 5 8 13...
a=0
b=1
n=int(input('enter no of terms : '))
print(a,b,end=',')
for i in range(2,n):
    c=a+b
    print(c,end=',')
    a=b
    b=c

#OUTPUT
'''
A
AB
ABC
ABCD
'''
n=int(input('enter no. : '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(j+64),end=' ')
    print( )

'''WARNING FIX PROGRAM WRONG'''
'''WARNING FIX PROGRAM WRONG'''
#output
'''
   *
  ***
 *****
'''
n=int(input('enter no. : '))
for i in range(1,n+1,2):
    print(' '*(n-i-1)+'*'*i)
'''WARNING FIX PROGRAM WRONG'''
'''WARNING FIX PROGRAM WRONG'''
