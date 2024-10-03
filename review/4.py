# def my_function():
#     yield 1
#     yield 2
#     yield 3
    
# x = my_function()
# print(next(x))
# print(next(x))
# print(next(x))


# def get_data_from_file(file_name):
#     with open(file_name, "r") as file:
#         return file.read().strip().split("\n")
    
# all_words = get_data_from_file("words.txt")
# user_input = input("enter something: ")
# sorted_input = sorted(user_input)
# simmilar_words = []

# for word in all_words:
#     if sorted_input == sorted(word) and user_input != word:
#         simmilar_words.append(word)
# print(simmilar_words)



# x = lambda a : a + 10
# print(x(123))
# print(type(x))
# import os

# user_input = input("enter: ")
# eval(user_input)
import os
# eval("os.system('cls')")
# s = """import pygame
# screen = pygame.display.set_mode((100,200))
# running = True
# """
# exec(s)
# import os
# command = input("enter a command: ")
# command = 'os.system('+f'"{command}"'+')'
# exec(command)


# x = input("enter a number: ")
# if x == '':
#     raise "salaam"
# y = int(input("enter a number: "))
# print(x + y)

# t = lambda  x: "even" if x % 2 == 0 else "odd"

# print(t(4))