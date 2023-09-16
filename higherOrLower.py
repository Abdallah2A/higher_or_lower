from data.higherOrLower_data import data
import random
import os

def get_user_choice():
    """
    This function prompts the user for their choice and validates the input.

    Returns:
        int: user's choice (1 or 2)
    """
    while True:
        try:
            choice = int(input("Who Have more instgram followers:(1 or 2) "))
            if choice not in [1, 2]:
                raise ValueError("Invalid choice. Please enter 1 or 2.")
            return choice
        except ValueError as e:
            print(e)

def print_data(rand, data):
    """
    This function prints the data for the instgram account

    Args:
        rand (int): number of instgram account you need from the list
        data (list): list of instgram accounts
    """
    print(data[rand]["name"], end = " , ")
    print(data[rand]["description"], end = " , ")
    print(data[rand]["country"])

def get_instgram_value(data, rand):
    """
    This function returns the value of instgram followers for a given user

    Args:
        data (list): list of instgram accounts 
        rand (int): number to take its followers number from the list

    Returns:
        int: followers number
    """
    value = data[rand]["follower_count"]
    return value

def pick_random_number(data):
    """
    This function returns the random number in lenth of the given data list

    Args:
        data (list): list of instgram accounts 

    Returns:
        int: the random number in lenth of the given data list
    """
    rand = random.randint(0, len(data)-1)
    return rand

def compare(value1, value2, choice, my_score):
    """
    This function compares the two values and your choice and returns your score if you win or no by using score function
    and print my score after winning or losing using print score function

    Args:
        value1 (int): instgram followers for first account
        value2 (int): instgram followers for second account
        choice (int): your choice for who have more followers
        my_score (int): your score

    Returns:
        int: your new score
    """
    if (value1 >= value2 and choice == 1) or (value1 <= value2 and choice == 2):
        print("Right")
        my_score = score(my_score)
        os.system("cls")
        return my_score
    else:
        print("Wrong")
        print_score(my_score)
        return my_score

def score(my_score):
    """
    This function takes a your score and returns a score after winning by adding to it one
    
    Args:
        my_score (int): add your score

    Returns:
        int: new score
    """
    my_score += 1
    return my_score

def print_score(my_score):
    """
    This function prints score

    Args:
        my_score (int): you currently score
    """
    print(f"Your score is: {my_score}")

print("Welcome to higher or lower game!")
my_score = 0
old_score = -1
random_number = pick_random_number(data)

while my_score != old_score:
    print_score(my_score)
    old_score = my_score
    value1 = get_instgram_value(data, random_number)
    print_data(random_number, data)
    print("VS")
    random_number2 = pick_random_number(data)
    value2 = get_instgram_value(data, random_number2)
    print_data(random_number2, data)
    choice = get_user_choice()
    my_score = compare(value1, value2, choice, my_score)
    random_number = random_number2