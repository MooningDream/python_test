def list_append(numbers,num, gap):
    i =0
    while i < num:
        print(f"At the top i is {i}.")
        numbers.append(i)

        i += gap
        print("Numbers now", numbers)
        print(f"At the bottom i is {i}.")

    print("The numbers:")
    print(numbers)

num = int(input("The number is :"))
gap = int(input("The gap is :"))
numbers = []

list_append(numbers, num, gap)

print("The real numbers is ", numbers)