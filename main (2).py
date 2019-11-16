'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def speed(x):
    if(x<=70):
        print("you are ok")
    else:
        a=x-70
        b=a/5
        if(b<=12):
            print("Your demerit score is",b)
        else:
            print("you are suspended")
s=int(input())
speed(s)

