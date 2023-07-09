import random

def main():
    target_number = random.randint(1, 100)

    while True:
        guess = get_guess_from_user()

        if guess == target_number:
            print("Congratulations! You guessed it correctly.")
            break
        elif guess < target_number:
            print("The number is higher. Try again.")
        else:
            print("The number is smaller. Try again.")

def get_guess_from_user():
    while True:
        try:
            guess = int(input("Please enter a number: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == '__main__':
    main()
