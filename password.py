import random


lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special = "!@#$%&*~?+-"
numbers = "1234567890"
all = lower + upper + special + numbers
length = 10
password = "".join(random.sample(all,length))
print(password)