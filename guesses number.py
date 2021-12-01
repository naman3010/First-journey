i = 0
n = 18
print("enter your number")

while(i<10):
    input1 = int(input())
    print("you've", 10-i,  "guesses left")
    i = i+1
    if input1 > 18:
        print("your number is", input1-18, "more ahead")
    elif input1 < 18:
        print("your number is", 18-input1, "less behind")
