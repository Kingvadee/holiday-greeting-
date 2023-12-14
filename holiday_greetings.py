# holiday_greetings.py
from art import *
import random

def get_user_input():
    print("Compliments Champ!\nYou made it to the end of the year 2023.\n Congrats! ")
    user_name = input("Please enter your name: ")
    return user_name

def get_random_holiday_theme():
    holiday_themes = ["Christmas"]
    return random.choice(holiday_themes)

def generate_greeting(user_name, holiday_theme):
    greeting = text2art(f"Happy {holiday_theme}, {user_name}!")
    return greeting

def main():
    print("Welcome to the Holiday Greetings Generator!")
    user_name = get_user_input()
    holiday_theme = get_random_holiday_theme()
    greeting = generate_greeting(user_name, holiday_theme)
    print(greeting)

if __name__ == "__main__":
    main()

