large = None
smallest = None
while True:
    num = input("Enter a number: ")

    if num == "done" :
        break
    try:
        num1 = int(num)
    except:
        print("Invalid input")
        continue
    #print(num1)
    num1 = int(num)
    if large is None:
        large = num1
    if num1 > large :
        large = num1

    if smallest is None:
        smallest = num1
    elif num1 < smallest :
        smallest = num1

print("Maximum", large)
