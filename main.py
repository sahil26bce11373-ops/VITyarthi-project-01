import random
import string
def make_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    pw = ""
    for _ in range(length):
        pw += random.choice(chars)
    return pw
print("-" * 30)
print("   Password Generator")
print("-" * 30)
while True:
    print("\n1. Make a password")
    print("2. Quit")
    choice = input("Pick one: ")
    if choice == "2":
        print("Bye!")
        break
    elif choice == "1":
        try:
            n = int(input("How long should it be? "))
        except ValueError:
            print("That's not a number, try again.")
            continue
        # anything shorter than 4 is too easy to guess
        if n < 4:
            print("Needs to be at least 4 characters.")
        else:
            print("Your password:", make_password(n))
    else:
        print("Not a valid option.")