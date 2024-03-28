student_score = int(input("enter your score: "))

if(student_score <= 100):
    print("Your grade is A")
elif(student_score <= 89):
    print("Your grade is B")
elif(student_score <= 79):
    print("Your grade is C")
elif(student_score <= 69):
    print("Your grade is D")
elif(student_score <= 59):
    print("Your grade is F")
else:
    print("invalid score, please input your score correctly")