'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def fizz(x):
    if(x%3==0)and(x%5==0):
        print("fizzbuzz")
    elif(x%3==0)and(x%5!=0):
        print("fizz")
    elif(x%5==0)and(x%3!=0):
        print("buzz")
x=int(input("Enter the number"))
fizz(x)
