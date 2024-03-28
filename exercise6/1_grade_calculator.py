student_score = int(input("enter your score: "))
 
if(student_score >= 90) and (student_score <= 100):
    print("Your grade is A")
elif(student_score >= 80) and (student_score <= 89):
    print("Your grade is B")
elif(student_score >= 70) and (student_score <= 79):
    print("Your grade is C")
elif(student_score >= 60) and (student_score <= 69):
    print("Your grade is D")
elif(student_score >= 0) and (student_score <= 59):
    print("Your grade is E")
else:
    print("invalid score, please input your score correctly")
