#AVERAGE HEIGHT
student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
for heights in student_heights:
    total_height += heights
print (total_height)

total_student = 0
for student in student_heights:
    total_student += 1

average = total_height/total_student

print(f"Average height rounded to the nearest whole number ={round(average)}")