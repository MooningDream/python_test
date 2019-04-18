from sys import argv
from os.path import exists

script, from_file, to_file = argv

# print(f"Copying from {from_file} to {to_file}.")

# We couled do these two on one line, how?
# indata = open(from_file, encoding='utf-8', errors='ignore').read() # utf-8依然无法满足编码需求 使用ignore忽略

# print(f"The indata is {len(indata)} bytes long.") # 字符串中的{}需要在字符串之间使用一个f

# print(f"Does the output file exist? {exists(to_file)}.") # exists函数用于返回文件是否存在
# print("Ready, hit RETURN to continue, CTRL-C to abort.")
#input()

open(to_file, 'w').write(open(from_file, encoding='utf-8', errors='ignore').read())
# out_file.write(indata) # 将文件写入out_file

print("Alright, all done.")

# 最后关闭文