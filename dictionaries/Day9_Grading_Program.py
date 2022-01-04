student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}


for name in student_scores:
    if student_scores[name] == 100:
        student_scores[name] = "Outstanding "
    elif student_scores[name] > 81:
        student_scores[name] = "Exceeds Expectations"
    elif student_scores[name] > 71:
        student_scores[name] = "Acceptable"
    else:
        student_scores[name] = "Fail"

print(student_scores)
