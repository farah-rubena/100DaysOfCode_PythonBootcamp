accum = 0
for num in range(0, 101, 2):
    accum += num

print(accum)

# Solution 2

accum = 0
for n in range(101):
    if n % 2 == 0:
        accum += n

print(accum)
