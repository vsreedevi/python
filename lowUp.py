a="aaSSbbRE"
s=''
for x in a:
  if x.islower():
    s=s+x.upper()
  elif x.isupper():
    s=s+x.upper()
print s
