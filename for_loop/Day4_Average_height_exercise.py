student_heigts = input("Enter comma sep values: ").split(",")
count = 0
sum = 0

for n in range(0, len(student_heigts)):
    student_heigts[n] = int(student_heigts[n])
    sum += n
    count += 1

average_heights = sum / count
print(f"Average height is : {average_heights}")
