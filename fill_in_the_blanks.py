import sys
import string

# defining the lists that we will needed along the whole game and acrose most function
sentences = ["__1__ stands for __2__ Text Markup Language, it's the base prgramming language of the web and it's made up of __3__ and these are writen as __4__\n", "__1__ is a stylesheet language stands for __2__ Style __3__ used to describe the presentation of a document written in __4__\n", "__1__ is an __2__ oriented __3__ programming language it also supports __4__ and packages\n"]
answers = [
["html", "hyper", "elements", "tags"],
["css", "cascading", "sheets", "html"],
["python", "object", "high-level", "modules"]]

def greeting(players_name):
    """prints the greeting screen with the name of the players
    input: players name
    output: greeting sentence"""
    print "\nGreat! Welcome, " + players_name + ". The purpose of this game is to fill in the blanks for all the sentences provided."


players_name = raw_input("What is your name?\n")
greeting(players_name)
accepted_levels = ["easy", "medium", "hard"]
level = raw_input("So let's choose a level : easy, medium, hard\n")

#a while loop to force the user to choose from the available levels only
while level not in accepted_levels:
    level = raw_input("Please choose from the available levels : easy, medium, hard\n")

print "You've chosen the %s level. \nnow lets get started."%level

attempts = input("Please write down how many attempts you need\n")

def difficulty_for_level(level):
    """a function to return the level as an integer to use it acrose the code"""
    return 0 if level=="easy" else (1 if level=="medium" else 2)
difficulty = difficulty_for_level(level)

answers_number = len(answers[1]) if level=="easy" else (len(answers[2]) if level=="medium" else len(answers[2]))

def start_game(attempts,sentences,answers,difficulty):
    """after choosing the level this function checks for the sentence needed for
    the right level and checks for the correct answers for that level.
    inputs:the attempts that the user sets, a list of the sentences for all the levels, and the answers list, the difficulty as an integer
    outputs:it doesn't have any specific thing to return but it works for the terminal and to check the answers"""
    cycle_count = 0
    least_number_of_attempts = 0;
    while cycle_count < answers_number:
        if attempts == least_number_of_attempts:
            print "Sorry, you lose!"
            sys.exit()
        given_answer = raw_input(sentences[difficulty]).lower()
        while given_answer == "":
            print "you cant leave this field empty please write in the right answer."
            given_answer = raw_input(sentences[difficulty]).lower()
        if given_answer == answers[difficulty][cycle_count]:
            sentences[difficulty] = string.replace(sentences[difficulty], "__%d__" %(cycle_count+1) , given_answer)
            print "Correct answer!"
            if cycle_count == answers_number-1 :
                print "Congratulations you won :)"
            cycle_count += 1
        else:
            attempts -= 1
            print "Wrong answer! Try again! you have %d attempts left"%attempts


start_game(attempts,sentences,answers,difficulty)
