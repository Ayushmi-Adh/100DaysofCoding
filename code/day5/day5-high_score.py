#HIGH SCORE
student_scores = input("Input a list of student scores in a test: ").split(",")
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

max_score = 0
for marks in student_scores:
    if marks>max_score:
        max_score = marks

print(f"The highest score in the class is:{max_score}")
