ex_num = 1

while ex_num == 1 :
    print("write two numbers and sign like \n2\n3\n* ")
    first = float(input())
    second = float(input())
    sign = input()

    if sign == "+":
        print(first + second)
    elif sign == "-":
        print(first - second)
    elif sign == "*":
        print(first * second)
    elif (sign == "**") or (sign == "^"):
        print(first ** second)
    elif (sign == "/") and (second != 0):
        print (first / second)
    elif (sign == "//") and (second != 0) :
        print(first **(1 / second))


    if ((second == 0) and (sign == "/")) or ((second == 0) and (sign == "//")):
        print ("division by zero. Let's try again.")

    print ("write '1' to continue\nwrite '0' to exit")
    ex_num = int(input())