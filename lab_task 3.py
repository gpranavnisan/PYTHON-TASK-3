#1.print numbers from 1-10 using forloop:
'''for i in range(1,11):
    print(i)

#2.multiplication table of a number:
a=int(input("enter a number:"))
for i in range(1,11):
    print(a,"*",i,"=",a*i)
   
#3.print even numbers from 1-50:
for i in range(2,51,2):
    print(i)

#4.print factorial of a number:
a=int(input("enter a number:",))
b=1
for i in range(1,a+1):
    b*=i
print("":b)


#5.to check whether the number is palindrome or not using while loop:
a=int(input("enter a number:",))
b=0
t=a
while t>0:
    d=t%10
    b=(b*10)+d
    t=t//10
print(b)
if a==b:
    print("the number is a palindrome")
else:
    print("the number is not a palindrome")


#6.to print
    *
    **
    ***
    ****:
for i in range(1,5):
    for j in range(i):
        print("*",end="")
    print()

#7.to print even numbers from 2 to 21:
for i in range(2,21,2):
    print(i)

#8.to print 1 to 10 using while loop:
i=1
while i<=10:
    print(i)
    i+=1

#9.to print numbers from 1 to 20:
i = 1
while i<=20:
    print(i)
    i+=1
'''
#10.to print numbers from 10 to 1 using while loop:
i = 10
while i>=1:
    print(i)
    i-=1









