# https://docs.google.com/document/d/1VhCj6IDwRyRHqGYcM5X7NsbKrDKd5Cs87OrP4TeCPhw

import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("grades.csv", delimiter=",", skip_header=1)

cities = {
    1: "Tel Aviv",
    2: "Eilat",
    3: "Jerusalem",
    4: "Haifa",
    5: "Beer Sheva",
}

# a
num_students = data.shape[0]
print("Number of students:", num_students)

# b
final_exam_scores = data[:, -1]
# print(final_exam_scores)
average = np.mean(final_exam_scores)

print("Average final exam score:", average)

# print("Average final exam score:", np.mean(data[:, 6]))

final_exam_scores = data[:, -1]
homework_scores = data[:, 2:-1]
# print(homework_scores)

# c. What is the highest final test score and what is the lowest?
highest_final_exam_score = np.max(final_exam_scores)
lowest_final_exam_score = np.min(final_exam_scores)
print("Highest final exam score:", highest_final_exam_score)
print("Lowest final exam score:", lowest_final_exam_score)

# d. What is the average of the four homework assignments for all students?
# print(homework_scores)
average_homework_scores = np.mean(homework_scores, axis=0)
print("Average homework scores:", average_homework_scores)
print("Average homework scores total:", np.mean(homework_scores))

# axis 0 rows
# axis 1 cols
# e. Add a new column to the average homework scores of each student (row)
# print(homework_scores)
average_homework_scores_each_student = np.mean(homework_scores, axis=1)
# print(average_homework_scores_each_student)
average_homework_scores_each_student_col = np.reshape(average_homework_scores_each_student, (num_students, 1))
data = np.hstack([data, average_homework_scores_each_student_col])

# f. Add a new column of final grade in the course that will be composed as follows:
# Final exam grade - 90%
# homework scores (for each student) - 10%
final_grades = 0.9 * final_exam_scores + 0.1 * average_homework_scores_each_student
final_grades = np.reshape(final_grades, (num_students, 1))
data = np.hstack((data, final_grades))
#
# # g. What is the average of the final grades of the course?
average_final_grade = np.mean(final_grades)
print("Average final grade:", average_final_grade)
#
# # h. Who is the student with the highest final grade?
FINAL_GRADE_COL_INDEX = data.shape[1] - 1
# highest_final_grade = data[:, -1].max()
highest_final_grade = data[:, FINAL_GRADE_COL_INDEX].max()
highest_student_id_and_city = data[data[:, -1] == highest_final_grade, :2]
student_id = highest_student_id_and_city[0, 0]
city_id = highest_student_id_and_city[0, 1]
print(f"The student with the highest final grade is student with id {student_id} from {cities[city_id]}")

MIN_GRADE_TO_PASS = 60
#
# # i. Print all the lines of those who passed the course (passer - final score of 60)
passers = data[data[:, -1] >= MIN_GRADE_TO_PASS]
print("Students who passed the course with there final grade:")
print(passers[:, 0:9:8])
# print(passers[:, [0, 8]])

#
# # j. Print the amount of the number of people who fail the course
# failers = data[data[:, -1] < MIN_GRADE_TO_PASS]
# print(f"\nNumber of students who failed the course: {len(failers)}")


# # k. Print all the students and their city who received a final grade above the average
course_avg = data[:, FINAL_GRADE_COL_INDEX].mean()
students_above_avg = data[data[:, FINAL_GRADE_COL_INDEX] > course_avg]
print("\nStudents above average:")
for s in students_above_avg:
    print(f"{int(s[0])} from {cities[s[1]]}: {s[-1]}")
#
# # l. Show each city the average grades of its students
cities_avg = {}

print("\nAll cities averages:")
for city_id, city_name in cities.items():
    current_city = data[data[:, 1] == city_id]
    avg_city = current_city[:, FINAL_GRADE_COL_INDEX].mean()
    cities_avg[city_id] = avg_city
    print(f"{city_name}: {avg_city}")
#
# # m. presented the name of the city with the highest average scores
cities_data = np.column_stack((list(cities_avg.keys()), list(cities_avg.values())))
# print(cities_data)
highest_average_scores_city=cities_data[:, 1].max()
top_city = cities_data[cities_data[:, 1] == highest_average_scores_city]
# top_city = cities_data[cities_data[:, 1] == cities_data[:, 1].max()]
top_city_id = top_city[0, 0]
print(f"The city with the highest average is: {cities[top_city_id]}")
#
# n. graph
plt.bar(cities.values(), cities_avg.values())
plt.yticks(range(0, 101, 10))
plt.grid(axis="y")
plt.show()
