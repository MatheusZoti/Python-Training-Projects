import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length_input = input("Enter the desired password length: ")
    try:
        length = int(length_input)
        password = generate_password(length)
        print("Generated Password:", password)
        try_again()
    except ValueError:
        print("Please, enter a valid number.")
        main()


def try_again():
  _ = input("Want to try again? (y/n)")
  if _.lower() == "y":
    main()
  elif _.lower() == "n":
    exit()
  else:
    print("Invalid answer.")
    try_again()


# Run the program
main()