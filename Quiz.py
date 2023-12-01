import sys

print('----------------------------------------------------------')
print(" Welcome to Python 1 on 1 ")
print('----------------------------------------------------------')

input()

while True:
    participation = input("Would you like to test your Python knowledge? (yes/no): ")
    if participation.lower() in ["yes", "no"]:
        break
    else:
        print("Invalid response. Please enter 'yes' or 'no'.")

if participation.lower() == "yes":
    print('''
    Overview
    This is a simple console-based Quiz game that tests the player's knowledge of Python programming.
    The quiz has a total of 13 questions.

    Let the Quiz BEGIN!!

    Best of Luck 
    ''')
else:
    print("Thank you. Come again.")
    sys.exit()


input()

# -----------------------
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -----------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG! ")
        return 0
# -----------------------

def display_score(correct_guesses, guesses):
    print("------------------------------")
    print("RESULTS")
    print("------------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("You received a: "+str(score)+"%")

# -----------------------
def play_again():

    response = input("Would you like to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -----------------------

questions = {
'''What is the output of the following code?

        print(3 + 2 * 2)''': "A",
"Which of the following data types is mutable(can be modified after creation)?: ": "D",
"What is the correct way to define a function in Python?: ": "C",
"What does the 'len()' function return for a list?: ": "A",
"Which operator is used for exponentiation in Python?: ": "B",
"What is the correct way to create a list in Python?: ": "A",
'''What is the output of the following code?  

            name = 'Jennifer'
            Print(name[1:-1]) ''': "B",
"What type of variable would the following variable be identified as?:  rating = 2.4": "B",
"What is the correct way to convert a string variable to an int variable?: ": "A",
"What will len('Hello, World!') return?: ": "C",
"What is the correct way to comment a single line of code in Python?: ": "B",
'''what would be the output of the following code? 
            a = "I like pie"
            b = "I don't like pie"

            if a == b:
            print ("They are equal")
            else:
            print("Not equal")
            ''': "B",
"What year was Python released in?: ": "A"
}

options = [["A. 7", "B. 10", "C. 5", "D. 12"],
          ["A. int", "B. float", "C. string", "D. list"],
          ["A. func my_function():", "B. function my_function():", "C. def my_function():", "D. define my_function():"],
          ["A. The number of elements", "B. The sum of elements", "C. The first element", "D. The average of elements"],
          ["A. ^", "B. **", "C. *", "D. //"],
          ["A. list =[1,2,3]", "B. list = list(1,2,3)", "C. list = 1,2,3", "D. list = (1,2,3)"],
          ["A. NameError: name 'Print' is not defined", "B. ennife", "C. Jennifer", "D. nnife"],
          ["A. int", "B. float", "C. string", "D. boo"],
          ["A. int(birth_year)", "B. in_(birth_year)", "C. int[birth_year]", "D. int{birth_year}"],
          ["A. 12", "B. 11", "C. 13", "D. 10"],
          ["A. // Comment", "B. # Comment", "C. /* Comment*/", "D. <!-- Comment --!>"],
          ["A. They are equal", "B. Not equal", "C. b", "D. a"],
          ["A. 1991", "B. 1986", "C. 2004", "D. 1997"]]

new_game()

while play_again():
    new_game()

print("Thank you,come again")




