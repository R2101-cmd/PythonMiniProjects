odd=0
even=0
n=int(input())
i=0
while i<n:
  i+=1
  a=int(input())
  if a%2==0:
    even+=1
  else:
    odd+=1
print("even: %s odd: %s"%(odd,even))