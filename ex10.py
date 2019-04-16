tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
blackslash = "I'm \\a\\ cat."

fat_cat = """
i'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(blackslash)
print(fat_cat)

alarm = "There is a car comes away.{}"
print(alarm.format("\a\a\a\a\a"))
x = "\a\a\a\a\a"
alram2 =  f"There is a car comes away.{x}"
print(alram2)
