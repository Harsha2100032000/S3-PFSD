n=int(input("enter range:"))
def isPalindrome(n,s=0):
 temp=n
 while n>0 :
  r=n%10
  s=(s*10)+r
  n=n//10
 if temp==s :
 	return True
 else :
  return False

for i in range (1,n):
	if isPalindrome(i):
		print(i)