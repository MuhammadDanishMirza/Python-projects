from time import *
import random


def calculate_net_wpm(input_text, typed_text, t1, t2):
    typed_word_list = typed_text.split()
    no_of_input_words = len(typed_word_list)
    time_in_seconds = t2 - t1
    time_in_minutes = time_in_seconds / 60
    gross_wpm = no_of_input_words / time_in_minutes

    input_word_list = input_text.split()

    error = 0

    if len(input_word_list) == len(typed_word_list):
        for i in range(len(input_word_list)):
            if input_word_list[i] != typed_word_list[i]:
                error = error + 1
    else:
        print("Enter correct text to determine your correct typing speed")

    Net_wpm = gross_wpm - error
    return round(Net_wpm)


def accuracy(input_text, typed_text):
    typed_word_list = typed_text.split()
    input_word_list = input_text.split()
    intersection_of_sets = set(typed_word_list) & set(input_word_list)
    accuracy = len(intersection_of_sets)
    accuracy = accuracy / len(input_word_list)
    return accuracy * 100


def main_function():
    text = [
        "Python is a versatile and high-level programming language known for its simplicity, readability, "
        "and extensive community support. Created by Guido van Rossum and first released in 1991, Python has gained "
        "widespread popularity for its ease of learning and use. It emphasizes code readability through its clear and "
        "expressive syntax, making it an ideal choice for both beginners and experienced developers.",
        "Machine learning is a subfield of artificial intelligence (AI) that focuses on developing algorithms and "
        "models that enable computers to learn from data and make predictions or decisions without explicit "
        "programming. Instead of being explicitly programmed to perform a task, a machine learning system uses "
        "statistical techniques to recognize patterns and improve its performance over time as it is exposed to more "
        "data.",
        "Artificial Intelligence (AI) refers to the development of computer systems that can perform tasks that "
        "typically require human intelligence. These tasks include problem-solving, learning, perception, "
        "language understanding, and decision-making. AI systems are designed to mimic human cognitive functions, "
        "and they can be classified into two main types: Narrow AI, which is designed for a specific task, "
        "and General AI, which would possess the ability to perform any intellectual task that a human being can.",
        "My name is muhammad danish mirza. I am 20 years old"]

    text1 = random.choice(text)
    print()
    print("----***Typing Speed Calcultor***----")
    print("If you did not enter space as shown in the string. Program will not give correct wpm and accuracy ")
    print()
    print(text1)
    print()
    time1 = time()
    Entered_text = input("Enter: ")
    time2 = time()
    t = time2 - time1
    print(f"WPM:{calculate_net_wpm(text1, Entered_text, time1, time2)}")
    print(f"Accuracy is {accuracy(text1, Entered_text)}")
    print(f"Time taken to write {round(t, 2)} seconds")


while True:
    a = input("Enter 'quit' to exit the program or press enter to continue: ")
    if a.lower() == "quit":
        break
    main_function()
