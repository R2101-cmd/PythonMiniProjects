import sys
balance=100
while True:
  print("Enter your account Number:")
  num=int(input(">"))
  while True:
    print("Enter Your Choice \n 1.Check Balance \n 2.Deposit \n 3.Withdraw \n 4.Exit")
    choice=int(input(">"))
    if choice==1:
      print("Your Current Balance:",balance)
    elif choice==2:
      print("You Selected to Deposit. Enter your ammount to deposit.")
      d=int(input(">"))
      balance += d  
      print("Amount Deposited")
    elif choice==3:
      print("Enter the ammount to withdraw.")
      w=int(input(">"))
      if w>=balance:
          print("Insufficiant Balance")
      else:
        balance=balance-w
        print("Ammount Withdrawn")
    elif choice==4:
      print("Thank You!")
      sys.exit()