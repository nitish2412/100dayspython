# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
total_height=0
for height in student_heights:
  total_height+=height
#num_students=len(student_heights)
num_students=0
for student in student_heights:
  num_students+=1
avg_height=round(total_height/num_students)
print(f"total height = {total_height}")
print(f"number of students = {num_students}")
print(f"average height = {avg_height}")



