import numpy as np

# Generate an array of student IDs
student_id = np.arange(1, 41)

# Generate array of city with a normal distribution
city = np.random.normal(5, 3, 40).round().astype(int)
city = np.clip(city, 1, 5).astype(int)

# Generate arrays of grades for homework and final exam with a normal distribution and mean of 80, and standard deviation of 30
hw1 = np.random.normal(80, 30, 40).round().astype(int)
hw2 = np.random.normal(80, 30, 40).round().astype(int)
hw3 = np.random.normal(80, 30, 40).round().astype(int)
hw4 = np.random.normal(80, 30, 40).round().astype(int)
final_exam = np.random.normal(80, 30, 40).round().astype(int)

# Clip the values outside the range of 1 to 100
hw1 = np.clip(hw1, 1, 100)
hw2 = np.clip(hw2, 1, 100)
hw3 = np.clip(hw3, 1, 100)
hw4 = np.clip(hw4, 1, 100)
final_exam = np.clip(final_exam, 1, 100)

# Combine the arrays into a 2-D array
data = np.column_stack((student_id, city, hw1, hw2, hw3, hw4, final_exam))

# Save the array to a CSV file
np.savetxt("grades.csv", data, delimiter=",", header="student_id,city,hw1,hw2,hw3,hw4,final_exam", comments="", fmt='%d')

