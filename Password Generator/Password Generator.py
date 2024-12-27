import random
import string
import time

restart = 1

while restart == 1:
    def generate_password(length):
        # Define the character sets
        all_characters = string.ascii_letters + string.digits + string.punctuation
        
        # Randomly choose characters from the combined character set
        password = ''.join(random.choice(all_characters) for _ in range(length))
        
        return password

    # Ask the user for the length of the password
    try:
        length = int(input("Enter the length of the password: "))
        if length < 6:
            print("Password length should be at least 6 characters for security.")
        else:
            password = generate_password(length)
            print("Your generated password is:", password)
            time.sleep(1)
            restart = (input("Do you want to go again? Yes/No ")).lower()

            if restart == 'yes':
                restart = 1
                print ("Restarting program.")
                time.sleep(1)

            elif restart == 'no':
                restart = 0
                
            else:
                print("Invalid Input. Exiting Program") 
                break

    except ValueError:
        print("Please enter a valid number for the length.")
