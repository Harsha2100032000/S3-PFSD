n=int(input("Enter number to be verified:"))
temp=n
s=0
while(n>0):
    r=n%10
    s=s*10+r
    n=n//10

if(temp==s):
    print(temp," is a palindrome")
else:
    print(temp," isn't a palindrome")