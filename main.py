# encoding and decoding
import random

# message encoding

def encoding(message):
    words = message.split()
    coded_message = []
    for word in words:
        if len(word)>3:
            random_characters = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k=3))
            coded_word = random_characters + word[1:] + word[0] + random_characters
            coded_message.append(coded_word)
        else:
            coded_message.append(word[::-1])
    return ' '.join(coded_message)

# message decoding

def decoding(message):
    words = message.split()
    decoded_message = []
    for word in words:
        if len(word)>6:
            decoded_word = word[3:-3]
            decoded_word = decoded_word[-1] + decoded_word[:-1]
            decoded_message.append(decoded_word)
        else:
            decoded_message.append(word[::-1])
    return ' '.join(decoded_message)

# Ask user what he wants to do

question = input("Please enter what you want to do? (encode/decode): ").lower()

if question == "encode":
    message = input("Please enter what you want to encode: ")
    coded_message = encoding(message)
    print(f"Coded message: {coded_message}")
elif question == "decode":
    message = input("Please what you want to decode: ")
    decoded_message = decoding(message)
    print(f"Decoded message: {decoded_message}")
else:
    print("Please enter valid value")
            












# print('''
#         ---------Welcom to kbc, You will be asked some kind questions------------.
#         ---------You will win money if you answer correct.-----------------------''')
# questions = ["Who is founder of Pakistan?", "Who recommend the name of Pakistan?", "In Which month Quaid E Azam was born?"]
# for question in questions:
#     print(questions[0])
#     answer = input("Answer: ").lower()
#     if answer == "quaid":
#         print("Excelent! You won 500 rupees")
#         want_continue = input("Do you want to continue? ").lower()
#         if want_continue == "yes":
#             print(questions[1])
#             answer = input("Answer: ").lower()
#         else:
#             print("Thanks for participating")
#             break
#     if answer == "rehmat ali":
#         print("Excellent you won 1000 rupees")
#         want_continue = input("Do you want to continue? ").lower()
#         if want_continue == "yes":
#             print(questions[2])
#             answer = input("Answer: ").lower()
#         else:
#             print("Thanks for participating")
#             break
#     if answer == "december":
#         print("Excellent you won 1500 rupees. Game has ended")
#         break
#     else:
#         print("Sorry, Your asnwer is wrong. Try next time")
#         break
# import this

# print("Fabonacci Series")
# num = int(input("Enter number: "))
# def fabo_series(num):
#     a,b = 0,1
#     fabo = []
#     for _ in range(num):
#         fabo.append(a)
#         a, b = b, a+b
#     return fabo
# print(fabo_series(num))

# print("Find Factorial")
# number = int(input("Enter number: "))
# def factorial(number):
#     if number == 0:
#         return 1
#     elif number == 1:
#         return 1
#     else:
#         return number * factorial(number-1)
# print(factorial(number))

# import math
# n = int(input("Enter n: "))
# print(math.factorial(n))
# n_set = set()
# print(type(n_set))

# numb = int(input("Enter number: "))
# print(f"Table of {numb}")
# for i in range(1, 11):
#     print(f"{numb} X {i} = {numb * i}")
