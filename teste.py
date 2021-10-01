import random
z = 0
x = 0

while z != 21:
    z = 0
    nums = []
    for i in range(4):
        x = random.randint(1,6)
        nums.append(x)
        z += x

print(nums, " = ", z)