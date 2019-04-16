print("How old are you?", end=' ')
age = int(input())
print("How tall are you?", end=' ')
height = input()
print("How much do you weight?", end=' ')
weight = input()

print("You are {} years old, {} cms tall and {} kgs weight.".format(age+1, height, weight))
print(f"You are {age} years old, {height} cms tall and {weight} kgs weight.") # 注意这个f