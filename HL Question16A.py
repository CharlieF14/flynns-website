# Question 16(a)
# Student Name: Charlie Flynn

def username():
    teacherName = input("Please enter your username: ")
    print("Welcome", teacherName,",", "to the student result calculator.")

username()

student_name=input("Please enter the students name: ")
student_score=float(input("Please enter the students mark: "))
exam_total = float(input("Please enter the total test marks: "))

gradeCategory = 0

score_as_a_percentage=float((student_score/exam_total)*100)
score_as_a_percentage = round(score_as_a_percentage,1)

if score_as_a_percentage >= 80:
    gradeCategory = "A"
elif score_as_a_percentage < 80 and score_as_a_percentage >= 60:
    gradeCategory = "B"
else:
    gradeCategory = "C"

print(student_name,"scored",score_as_a_percentage,"%. They got a", gradeCategory)



