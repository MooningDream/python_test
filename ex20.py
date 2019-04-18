from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0) # 读取文件的开头 以byte为单位

def print_a_line(line_count, f):
    print(line_count, f.readline(), end='') # readline 自带一个\n 指定end后可解决

current_file = open(input_file) # 遭遇编码问题时 可在open函数中设置 encoding='utf-8', errors='ignore'

print("First let's print the whole file:")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)