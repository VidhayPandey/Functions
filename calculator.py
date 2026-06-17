def add(P,Q):
  return  P+Q

def subtract(P,Q):
  return P-Q

def multiply(P,Q):
  return P*Q

def divide(P,Q):
  return P/Q
while True:
    print("Please select an operation.")
    print("a. Addition")
    print("b. Subtraction")
    print("c. Multiplication")
    print("d. Division")

    choice=input("Please Enter Your Choice (a/b/c/d) (type e to exit): ")

    if choice=="e":
      print("Goodbye!")
      break

    else:
        num1= int(input("Enter the first number: "))
        num2= int(input("Enter the second number: "))

        if choice=="a":
         print(f"{num1} + {num2} = {add(num1,num2)}")

        elif choice=="b":
         print(f"{num1} - {num2} = {subtract(num1,num2)}")

        elif choice=="c":
         print(f"{num1} * {num2} = {multiply(num1,num2)}")

        elif choice=="d":
         print(f"{num1} / {num2} = {divide(num1,num2)}")

        else:
         print("Invalid Input!")