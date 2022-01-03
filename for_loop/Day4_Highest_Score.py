student_scores = input("Enter comma sep marks as values: ").split(",")
highest_score = 0

for score in range(len(student_scores)):
    student_scores[score] = int(student_scores[score])
    if highest_score < student_scores[score]:
        highest_score = student_scores[score]

print(f"The highest score is: {highest_score}")
