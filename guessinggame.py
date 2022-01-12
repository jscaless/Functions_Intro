import random  # input the randomint function is needed


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)  # No need to add break because return will break it
        else:
            print("Invalid entry, please enter an integer.")
            continue


highest = 100
answer = random.randint(1, highest)
print(answer)  # TODO: Remove after testing.
guess = 0  # initialise to any number that doesn't equal the answer
print("Please guess number between 1 and {}: ".format(highest))

while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        break
    if guess == answer:
        print("Good Job! You guessed the right answer!")
        break
    else:
        if guess < answer:
            print("Please guess higher, your answer was too low.")
        else:  # guess must be greater than answer
            print("Please guess lower, your answer was too high")
    continue
# guess = int(input())
#      print("Good Job! You guessed the right answer!")
#     break
# else:
#     print("Sorry, you did not guess correctly, please try again.")
# continue


# if guess < answer:
#     print("Please guess higher!")
#     print("Please guess again between 1 and 10: ")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you got it right!")
#     else:
#         print("Sorry, you have not guess correctly")
# elif guess > answer:
#     print("Please guess lower!")
#     print("Please guess again between 1 and 10: ")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you got it right!")
#     else:
#         print("Sorry, you have not guess correctly")
# else:
#     print("Look at you, sly dog, you got it right on the first time!")