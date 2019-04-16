from sys import argv
# read the WYSS section for how to run this
script, first, second, thrid = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your thrid variables is:", thrid)

script_1 = input("The script called? ")
print(script == script_1)