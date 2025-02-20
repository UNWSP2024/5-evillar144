# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129
import random

def mathproblem(n1, n2):
    print("---Answer the question below---")
    print(f" {n1} + {n2} = ?????")
    tanswer = int(input("What is your answer?: "))
    answer = n1 + n2
    if answer == tanswer:
        print("---CONGRATULATION YOU DID IT---")
    else:
        print("---WRONG ANSWER---")
        print(f"The correct answer is: {answer}")



ran1 = (random.randint(1, 1000))
ran2 = (random.randint(1, 1000))
mathproblem(ran1, ran2)
# The program should allow the student to enter the answer.
# If the answer is correct, a message of congratulations should be displayed.
# If the answer is incorrect a message showing the correct answer should be displayed.
# The program must use a function that accomplishes part of the needed tasks.
