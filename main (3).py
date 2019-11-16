'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def oddeven(x):
  for i in range(x+1):
    if(i%2==0):
      print(i,"is EVEN")
    else:
      print(i,"is ODD")
  
x=int(input("Enter the number"))
oddeven(x)

