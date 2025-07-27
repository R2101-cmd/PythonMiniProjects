print("Mini Calculator")
a=int(input("Enter num1:"))
b=int(input("Enter num2:"))
while True:
  print("Add(1), Subtract(2),Multiply(3),Division(4)")
  n=int(input('>'))
  if n==1:
    sum=a+b
    print(sum)
    break
  elif n==2:
    sub=a-b
    print(sub)
    break
  elif n==3:
    mul=a*b
    print(mul)
    break
  elif n==4:
    div=a//b
    print(b)
    break
  else: 
    break  