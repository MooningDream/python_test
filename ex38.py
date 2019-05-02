ten_things = "Apple Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ') # 以空格为规则来分割字符串
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"] # pop函数从最后一个元素开始递出

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding:",next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go:", stuff)

print("Let's do some thing with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop()) # 虽然有print 但是pop函数同样生效 len(stuff) -1
print(' '.join(stuff)) # 用空格拼接列表成字符串
print('#'.join(stuff[3:5])) # 用#拼接stuff[3]和stuff[4]

