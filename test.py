import random
import openpyxl
from datetime import datetime

print(" Welcome to Python 1 on 1 ")
input()

# Sample questions and answers
questions = [
    {
        "question": '''
        What is the output of the following code?

        print(3 + 2 * 2)''',
        "choices": ["7", "10", "5", "12"],
        "answer": "7"
    },
    {
        "question": "Which of the following data types is mutable(can be modified after creation)?",
        "choices": ["int", "float", "string", "list"],
        "answer": "list"
    },
    {
        "question": "What is the correct way to define a function in Python?",
        "choices": ["func my_function():", "function my_function():", "def my_function():", "define my_function():"],
        "answer": "def my_function():"
    },
    {
        "question": "What does the 'len()' function return for a list?",
        "choices": ["The number of elements", "The sum of elements", "The first element", "The average of elements"],
        "answer": "The number of elements"
    },
    {
        "question": "Which operator is used for exponentiation in Python?",
        "choices": ["^", "**", "*", "//"],
        "answer": "**"
    },
    {
        "question": "What is the correct way to create a list in Python? ",
        "choices": ["list =[1,2,3]", "list = list(1,2,3)", "list = 1,2,3", "list = (1,2,3)"],
        "answer": "list =[1,2,3]"
    },
    {
        "question":
            ''' What is the output of the following code?  

            name = 'Jennifer'
            Print(name[1:-1]) ''',
        "choices": ["NameError: name 'Print' is not defined", "ennife", "Jennifer", "nnife"],
        "answer": "ennife"
    },
    {
        "question": '''
        What type of variable would the following variable be identified as? 
        rating = 2.4''',
        "choices": ["int", "float", "string", "boo"],
        "answer": "float"
    },
    {
        "question": " What is the correct way to convert a string variable to an int variable?",
        "choices": ["int(birth_year)", "in_(birth_year)", "int[birth_year]", "int{birth_year}"],
        "answer": "int(birth_year)"
    },
    {
        "question": 'What will len("Hello, World!") return',
        "choices": ["12", "11", "13", "10"],
        "answer": "13"
    },
    {
        "question": "What is the correct way to comment a single line of code in Python?",
        "choices": ["// Comment", "# Comment", "/* Comment*/", "<!-- Comment --!>"],
        "answer": "#Comment"
    },
    {
        "question":
            '''what would be the output of the following code?
            a = "I like pie"
            b = "I don't like pie"

            if a == b:
            print ("They are equal")

            else:
            print("Not equal")
            ''',
        "choices": ["They are equal", "Not equal", "b", "a"],
        "answer": " Not equal"
    },
    {
        "question": "What year was Python released in ?",
        "choices": ["1991", "1986", "2004", "1997"],
        "answer": "1991"
    },

]


def get_feedback():
    while True:
        feedback = input("Would you like to provide feedback? (yes/no): ")
        if feedback.lower() == "yes":
            user_feedback = input(" Please enter your feedback:")
            return user_feedback
        elif feedback.lower() == "no":
            return None
        else:
            print("Invalid response. Please enter 'yes' or 'no'.")


def save_feedback_to_excel(user_name, feedback):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Feedback"

    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append(["User Name", "Feedback", "Date"])
    sheet.append([user_name, feedback, current_date])

    workbook.save("data/feedback.xlsx")


def provide_feedback_after_challenge(user_name):
    feedback = get_feedback()
    if feedback is not None:
        save_feedback_to_excel(user_name, feedback)
        print("Thank you for your feedback!")


def provide_feedback_without_challenge(user_name):
    print("Since you're not taking the challenge, ")
    feedback = get_feedback()
    if feedback is not None:
        save_feedback_to_excel(user_name, feedback)


def calculate_grade(score, total_questions):
    percentage = (score / total_questions) * 100

    if 90 <= percentage <= 100:
        return "Congratulations your score was " + str(int(percentage)) + " you got an A"
    elif 80 <= percentage < 90:
        return "Not bad, your score was " + str(int(percentage)) + " you got a B"
    elif 70 <= percentage < 80:
        return "C's get degrees, your score was a " + str(int(percentage)) + " you got a C"
    elif 60 <= percentage < 70:
        return "Seems you may need a refresher, your score was " + str(int(percentage)) + " you received a D"
    else:
        return "It happens, your score was " + str(int(percentage)) + " you received an F"


def close_system():
    print("Closing the system. Thank you!")
    exit()  # This will exit the entire program


def run_challenge():
    while True:
        user_name = input("Please enter your name: ")

        while True:
            assessment_participation = input("Would you like to test your Python knowledge? (yes/no): ")
            if assessment_participation.lower() in ["yes", "no"]:
                break
            else:
                print("Invalid response. Please enter 'yes' or 'no'.")

        if assessment_participation.lower() == "yes":
            print(''' 

            Let the Knowledge Check BEGIN!!

            This assessment will ask you 13 questions to test your Python knowledge 

            Best of Luck 

            ''')
            score = 0
            for question in random.sample(questions, len(questions)):
                print(question["question"])
                for idx, choice in enumerate(question["choices"], start=1):
                    print(f"{idx}. {choice}")

                while True:
                    user_answer = input("Select your answer (1-4): ")
                    if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
                        break
                    else:
                        print("Invalid input. Please enter a number between 1 and 4.")

                user_choice = question["choices"][int(user_answer) - 1]
                if user_choice == question["answer"]:
                    score += 1

            total_questions = len(questions)
            grade = calculate_grade(score, total_questions)
            print(f"Your grade: {grade}")

            # Prompt for feedback after the assessment
            provide_feedback_after_challenge(user_name)

            # Check if feedback was provided
            if provide_feedback_after_challenge(user_name) is not None:
                print("Thank you for your feedback!")

            redo = input("Do you want to redo the challenge? (yes/no): ")
            if redo.lower() != "yes":
                while True:
                    response = input(
                        "Would you like to close the system or start from the beginning? (close/beginning): ")
                    if response.lower() == "close":
                        close_system()
                    elif response.lower() == "beginning":
                        print("Starting from the beginning...")
                        break
                    else:
                        print("Invalid response. Please enter 'close' or 'beginning'.")

            elif redo.lower() != "no":
                print("Thank you!")
                break

        elif assessment_participation.lower() == "no":

            # Prompt for feedback without the assessment
            provide_feedback_without_challenge(user_name)

            while True:
                response = input("Would you like to close the system or start from the beginning? (close/beginning): ")
                if response.lower() == "close":
                    close_system()
                elif response.lower() == "beginning":
                    print("Starting from the beginning...")
                    break
                else:
                    print("Invalid response. Please enter 'close' or 'beginning'.")
        else:
            print("Invalid response. Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    run_challenge()
