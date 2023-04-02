# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
sum = 0
count = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
    sum = sum + student_heights[n]
    count = count + 1

average = sum / count
print (round(average))