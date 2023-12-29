# 📖 Gradebook project.
# Using lists to organize subjects and grades.
# José Anderson Ramos Aquino.

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ['physics', 'calculus', 'poetry', 'history']

grades = [98, 97, 85, 88]

gradebook = [['physics', 98], ['calculus', 97], ['poetry', 85], ['history', 88]]
print(gradebook)

# Append 'computer science' and 'visual arts'. 
gradebook.append(['computer science', 100])
gradebook.append(['visual arts', 93])
print()
print(gradebook)

# Add 5 points to visual arts grade.
gradebook[-1][-1] += 5
print()
print(gradebook)

# Remove the numerical grade for visual arts.
gradebook[2].remove(gradebook[2][-1])
print()
print(gradebook)

# Add 'Pass' to visual arts.
gradebook[2].append('Pass')
print()
print(gradebook)

# Concatenate the last semester with the current one.
full_gradebook = last_semester_gradebook + gradebook

print()
print(full_gradebook)
