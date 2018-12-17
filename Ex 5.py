largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    try:
        num = float(num)
    except:
        print("Invalid input")

    if num == "done" :
        break
    if num > largest:
        largest = num

    elif num < smallest:
        smallest = num

print("Maximum", largest)
