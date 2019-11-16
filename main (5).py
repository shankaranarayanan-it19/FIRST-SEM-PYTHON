'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def stars(x):
  for i in range (1,x+1):
    for j in range(1,i+1):
      print("*",end="")
    print("\r")

x=int(input("Enter the number of rows"))
stars(x)
