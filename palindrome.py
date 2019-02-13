n=int(raw_input(""))
n1=n
rev=0
while(n1 !=0)
  rem=n1%10
  rev=rev*10+rem
if(n==rev):
  print("Yes")
else:
  print("No")
