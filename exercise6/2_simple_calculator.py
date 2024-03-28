score1 = int(input("Enter the first number: "))
operator = input("Enter the operator(+, -, *, /): ")
score2 = int(input("Enter the second number: "))

def calculator(score1, score2, operator):
    if operator == '+':
        return score1 + score2
    elif operator == '-':
        return score1 - score2
    elif operator == '*':
        return score1 * score2
    elif operator == '/':
        return score1 / score2

print("the result is =", calculator(score1, score2, operator))