'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def sum1(x):
    add=0
    for i in range (x+1):
        if((i%3==0)or(i%5==0)):
            add=add+i
    print(add)
x=int(input("Enter the number"))
sum1(x)


