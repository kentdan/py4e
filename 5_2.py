largest = None
smallest = None
num = 0
while True:
    num = raw_input("Enter a number: ")
    if num == "done": break
    try:
        num = int(num)
    except:
        print ("Invalid input")
        continue
    if smallest is None:
        smallest = num
    elif num < smallest :
        smallest = num
    if largest is None:
        largest = num
    elif num > largest:
        largest = num

print("Maximum is", largest)
print ("Minimum is",smallest)

#Enter 7, 2, bob, 10, and 4 and done
