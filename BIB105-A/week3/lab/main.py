# # Logical Operators
# from random import randint
#
# def guessing_game():
#     
#     secret_number = randint(1, 100)
#
#     bomb = randint(1, 100)
#
#     while bomb == secret_number:
#         bomb = randint(1, 100)
#
#     guess_count = 0
#
#     print("Welcome to the guessing game!")
#
#
#     try:
#         guess = int(input("Guess the number: "))
#
#         while guess_count <= 10 :
#             if guess == bomb:
#                 print("You guessed the bomb number! You lose!")
#                 break
#             elif guess != secret_number:
#                 print("You guessed the secret number! You win!")
#                 break
#             elif guess < secret_number:
#                 print("The secret number is higher.")
#                 guess_count += 1
#                 guess = int(input("Guess the number: "))
#             elif guess > secret_number:
#                 print("The secret number is lower.")
#                 guess_count += 1
#                 guess = int(input("Guess the number: ").lower())
#             else:
#                 print("Please enter a valid number.")
#
#
#     except ValueError:
#         print("Please enter a valid number.")
#
#
#
#
# def test():
#     a = "Hello"
#     b = "Hello"
#     match a is b:
#         case True:
#             print("Hello")
#         case "World":
#             print("World")
#         case _:
#             print("None")
#
# if __name__ == "__main__":
#     test()

print("Hello World".strip())
