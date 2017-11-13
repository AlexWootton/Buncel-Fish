import os
import random
import sys
from translation import Dictionary

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_logo():
    print(u'''

               Welcome to

    ____                             __
   / __ ) __  __ ____   _____ ___   / /
  / __  |/ / / // __ \ / ___// _ \ / /
 / /_/ // /_/ // / / // /__ /  __// /
/_____/ \__,_//_/ /_/ \___/ \___//_/
         ______ _        __
        / ____/(_)_____ / /_
       / /_   / // ___// __ \ ™
      / __/  / /(__  )/ / / /
     /_/    /_//____//_/ /_/


  Numero Uno in unversal translators

''')

def debunce():
    dict_file = "custom_dict.csv"
    dictionary = Dictionary(dict_file)
    languages = dictionary.languages
    word = None
    origin = None
    destination = None
    translation = None
    while True:
        clear_screen()
        print_logo()
        if not word:
            word = input("Buncism: ")
            if word == "":
                print("You need to provide a buncism to debunce")
                input("\npress ENTER to continue\n")
                word = None
                continue
        clear_screen()
        print_logo()
        try:
            translation = dictionary.translate(word, 'Buncish', 'English')
            if isinstance(translation, str):
                print("'{}' is '{}'".format(word, translation))
            elif isinstance(translation, list):
                print("A direct match couldn't be found for '{}'".format(word))
                print("Here are some near matches:")
                print("\n".join(translation))
            if input("\nDebunce again? [Y/n]: ").lower() == "n":
                print("\nCome back soon!\n")
                sys.exit()
        except ValueError as err:
            print(err)
            input("\npress ENTER to continue\n")
        break

def translate():
    done = False
    dict_file = "default_dict.csv"
    dictionary = Dictionary(dict_file)
    languages = dictionary.languages
    word = None
    origin = None
    destination = None
    translation = None
    while not done:
        clear_screen()
        print_logo()
        if not word:
            word = input("Word to translate: ")
            if word == "":
                print("You need to provide a word to translate")
                input("\npress ENTER to continue\n")
                word = None
                continue
        clear_screen()
        print_logo()
        if not origin:
            origin = input("Translate from: ").capitalize()
            if origin not in languages:
                print("Looks like that's not a supported language.")
                print("You can choose from the following:")
                print("{}".format("\n".join(languages)))
                input("\npress ENTER to continue\n")
                origin = None
                continue
        clear_screen()
        print_logo()
        if not destination:
            destination = input("Translate to: ").capitalize()
            if destination not in languages:
                print("That's not a supported language.")
                print("You can choose from the following:")
                print("{}".format("\n".join(languages)))
                input("\npress ENTER to continue\n")
                destination = None
                continue
        clear_screen()
        print_logo()
        try:
            translation = dictionary.translate(word, origin, destination)
            print("The {} word '{}' is '{}' in {}".format(origin, word,
                                                          translation,
                                                          destination))
            if input("\nTranslate another word? [Y/n]: ").lower() == "n":
                running = False
                done = True
        except ValueError as err:
            print(err)
            input("\npress ENTER to continue\n")
        break

def main():
    running = True
    clear_screen()
    print_logo()
    input("        press ENTER to start")
    while running:
        #translate()
        debunce()

main()
