n=input("")
n1=n
rem=0
res=0
while(n !=0):
  rem=n1%10
  res=res+(rem*rem*rem)
  n1=n1/10
if(n ==res):
  print "yes"
else:
  print "No"
