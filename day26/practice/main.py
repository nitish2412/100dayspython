import random
import pandas

numbers = [1, 2, 3]
# new_numbers = [new_item for item in list ]
new_numbers = [n+1 for n in numbers]
print(numbers)
print(new_numbers)

# list
# range
# string
# tuple

name = "Angela"
letter_list = [letter for letter in name]
print(name)
print(letter_list)

range_list = [n*2 for n in range(1,10)]
print(range_list)


# conditional list comprehension
# new_list = [new_item for item in list if Test ]

names = ["Alex", "seema", "Naulesh", "Jitendra", "Jitesh"]

short_name = [name for name in names if len(name) < 6]
short_name_upper = [name.upper() for name in names if len(name) < 6]
print(names)
print(short_name)
print(short_name_upper)

# dictionary comprehension

# new_dict = {new_key: new_value for item in list if test}
# new_dict = {new_key: new_value for (key,value) in dict.items() if test}

student_score = {student: random.randint(1,100) for student in names}
print(student_score)
passed_student = {student: score for (student, score) in student_score.items() if score > 50}
print(passed_student)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
# for (key,value) in student_data_frame.items():
#    print(key)

# Loop through Data frame.
for (index, row) in student_data_frame.iterrows():
    # print(index, row)
    print(row.student, row.score)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
