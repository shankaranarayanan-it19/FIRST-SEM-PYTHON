'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def prime(x):
  count=0
  for i in range(1,x+1):
    for j in range(1,x+1):
      if(i%j==0):
        count=count+1
    if (count==2):
      print(i)
    count=0
a=int(input())
prime(a)

