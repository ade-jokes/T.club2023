import random

def get_random_number():
    return random.randint(1, 10)

def guess_number(5):
    while True:
        try:
            guess = int(input("Guess the number between 1 and 10: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number.")
            break

if __name__ == "__main__":
    random_number = get_random_number()
    guess_number(random_number)
