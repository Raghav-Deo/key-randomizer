#!/usr/bin/env python3


from Packages.main import Keyrandomizer  # importing the Keyrandomizer class

if __name__ == '__main__':  # Check to disallow importing
    Keyrandomizer.intro()  # simple introductory line
    key_randomizer = Keyrandomizer(input("Give your password here : "))  # Taking input to pass arguments to
    # constructor method and creating the object
    output = key_randomizer.password_randomizer()  # saving the output to output variable
    print(output+'\nThis is your key,this key will also be saved in a text file named as password.txt\nThanks for '
                 'using our tool !\n(Ignore the text shown below)')
    key_randomizer.process_randomized_audio()  # To play the audio file for process completion
    key_randomizer.password_saver()
    key_randomizer.password_saved_audio()  # To play the audio file for process completion
    quit()  # Quit program after completing the process
elif __name__ != '__main__':  # Check to disallow importing
    print("You are not allowed to run this program by importing it\nExiting!")  # Message to be shown if imported
