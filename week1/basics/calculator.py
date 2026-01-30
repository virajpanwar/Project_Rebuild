#Simple Calculator using Functions
print("\033[H\033[J", end="")
def sum(a, b):
    c = a+b
    print(f"The sum of {a} and {b} is {c}")
def diff(a, b):
    c = a-b
    print(f"The difference of {a} and {b} is {c}")
def prod(a, b):
    c = a*b
    print(f"The product of {a} and {b} is {c}")
def div(a, b):
    a = float(a)
    b=float(b)
    c = a/b
    print(f"The division of {a} and {b} is {c}")
def rem(a, b):
    c = a%b
    print(f"The remainder after division {a} and {b} is {c}")
def pow(a, b):
    c = a**b
    print(f"{a} to the power {b} is {c}")

user_inp = input("SIMPLE CALCULATOR:\nChoose the operation you want to perform\n1. Sum of 2 numbers\n2. Difference of 2 numbers\n3. Product of 2 numbers\n4. Remainder of 2 numbers\n5. Power of a numbers\n")
try:
    user_inp = float(user_inp)
except:
    print("Not a number!")

inp_a = input("\nEnter the first number: ")
inp_b = input("Enter the second number: ")
try:
    inp_a = float(inp_a)
    inp_b = float(inp_b)
except:
    print("Not a number!")

if user_inp == 1:
    sum(inp_a, inp_b)
if user_inp == 2:
    diff(inp_a, inp_b)
if user_inp == 3:
    prod(inp_a, inp_b)
if user_inp == 4:
    rem(inp_a, inp_b)
if user_inp == 5:
    pow(inp_a, inp_b)