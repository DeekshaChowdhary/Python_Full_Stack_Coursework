##-------------------PATTERNS-----------------------
'''
-Outer loop → for rows
-Inner loop → for columns

## Printing n*n stars in square shape
n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        print('*',end=' ')
    print()
O/P-

* * * * 
* * * * 
* * * * 
* * * * 

n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        print(row,end=' ')
    print()
O/P-
0 0 0 0 
1 1 1 1 
2 2 2 2 
3 3 3 3

n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        print(col,end=' ')
    print()
O/P-
0 1 2 3 
0 1 2 3 
0 1 2 3 
0 1 2 3 
    
n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        print((row+col)%2,end=' ')
    print()
O/P-
0 1 0 1 
1 0 1 0 
0 1 0 1 
1 0 1 0 

n=int(input("Enter the size: "))
for row in range(n):
    for col in range(row+1):
        print('*', end=' ')
    print()
O/P-
* 
* * 
* * * 
* * * * 

n=int(input("Enter the size: "))
for row in range(n,0,-1):          ## for row in range(n):
    for col in range(row):              # for col in range(n-row):
        print('*', end=' ')
    print()
O/P-
* * * * 
* * * 
* * 
* 

n=int(input("Enter the size: "))
for row in range(n):
    for spc in range(n-row-1):
        print(' ', end=' ')
    for col in range(row+1):
        print('*', end=' ')
    print()
O/P-
      * 
    * * 
  * * * 
* * * * 

n = int(input("Enter the size: "))
for row in range(n):
    for spc in range(row):
        print(' ', end=' ')
    for col in range(n-row):
        print('*', end=' ')
    print()
O/P-
* * * * 
  * * * 
    * * 
      * 
    
n = int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')     
    print()
O/P-
* * * * 
*     * 
*     * 
* * * * 

n = int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==n-3 :
            print('*', end=' ')
        else:
            print(' ', end=' ')     
    print()
O/P-
* * * * * 
*       * 
* * * * * 
*       * 
* * * * * 


n = int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i+j==n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')     
    print()
O/P-
* * * * * 
      *   
    *     
  *       
* * * * *


n = int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
O/P-
*       * 
  *   *   
    *     
  *   *   
*       *

n = 7
for i in range(n):
    if i <= n // 2:
        for j in range(i + 1):
            print('*', end=" ")
        print()
    else:
        for j in range(n - i):
            print('*', end=" ")
        print()

O/p-
*
* *
* * *
* * * *
* * *
* *
*








'''
