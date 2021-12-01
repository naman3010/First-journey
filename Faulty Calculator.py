print("enter what do you want in this: +,-,*,/,power")
input1 = input()
print("enter 1st number")
input2 = int(input())
print("enter 2nd number")
input3 = int(input())

if input2 == 44 and input3 == 9 and input1 == "+":
    print(144)
elif input2 == 56 and input3 == 4 and input1 == "/":
    print(85)
elif input2 == 24 and input3 == 3 and input1 == "*":
    print(2)
elif input1 == "+":
    print(input2 + input3)
elif input1 == "-":
    print(input2 - input3)
elif input1 == "*":
    print(input2 * input3)
elif input1 == "/":
    print(input2/input3)
elif input1 == "power":
    print(pow(input2, input3))