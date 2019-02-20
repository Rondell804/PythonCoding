# A list of replacement words to be passed in to the play game function.
blanks  = ["__1__", "__2__", "__3__", "__4__", "__5__", "__6__", "__7__", "__8__"]
basketball_answers = ["Dribble", "Hoop", "Dunk", "Pointers", "10"]
football_answers = ["Touchdown", "Goal", "Quarterback", "Punter"]
Soccer_answers = ["Goal", "Shot", "Soccer", "Shorts"]
#  some test strings to pass in to the play_game function.
test_string1 = """Basketball is a great sport! I have to __1__ while running down the court.
Next, to score a point I have make the ball go into the basketball __2__ everytime. Another
way to score can be to jump and perform a slam __3__ . The Oakland Warriors are known for
shooting 3 __4__ . A regualtion basketball rim is __5__ feet."""
test_string2 = """Football is a great sport! A __1__ is how a team scores 6 points. Next,
 to score an extra point, the team kicks a field __2__ between the goal post. The __3__ is the player that throws the football.
 The __4__ is known to kick the ball on 4th down."""
test_string3 = """Soccer is an ok sport! A __1__ is how a team scores 1 point. Another
 way to score is a penalty __2__ between the goal post. This sport uses a __3__
 ball to play the game. Proper clothing is to wear a tee-shirt and
 __4__ to play comfortably."""

# Checks if a word in blanks is a substring of the word passed in.
def word_in_pos(word, blanks):
    for pos in blanks:
        if pos in word:
            return pos
    return None

def attempt_ans(user_ans, a_ans, chk_word, count_dwn, new_ans):
    while user_ans != a_ans[chk_word]:
        if count_dwn != 1:
            count_dwn = count_dwn - 1
            #The user has 3 tries for the correct answer
            print("Incorrect, try again. You have " + str(count_dwn) + " Attempts left" )
            user_ans = raw_input("Type in a: " + new_ans + " ")
        else:
            print "\n" "You have failed the test :("
            # After the 3 tries the user will see this string and program will exit
            exit()

def game_function(new_string, answer):
    replaced = []
    chk_word = 0
    for word in new_string:
        replacement = word_in_pos(word, blanks)
        if replacement != None:
            user_input = raw_input("Type in a: " + replacement + " ")
            #Where the countdown starts.
            counter = 4
            #Checks to see if the user's input is correct and if not try again.
            attempt_ans(user_input, answer, chk_word, counter, replacement)
            chk_word = chk_word + 1
            #chk_word will check for the next word to index for the user to answer
            #prints the list into a string also joins them together when passed through
            print fin_sent(replacement, user_input, word, new_string, replaced)
        else:
            replaced.append(word)
    return "\n" + "You Have Passed The Test! Great Job!!!"

#Function will allow the user to choose a game of their liking
def pick_Game():
    dif_type = '' #Empty string
    while not (dif_type == 'Basketball' or dif_type == 'Football' or dif_type == 'Soccer'):
        print("\n" + "Do you want to be tested on Basketball, Football, or Soccer?")
        dif_type = raw_input()
        #Corrects the user to choose a game that is listed
        while not (dif_type == 'Basketball' or dif_type == 'Football' or dif_type == 'Soccer'):
            print "\n" "Incorrect Input Try Again"
            print("\n" + "Do you want to be tested on Basketball, Football, or Soccer?")
            dif_type = raw_input()
    return dif_type

def fin_sent(new_word, user_say, my_word, a_string, a_list):
    #5 outputs - replacement / user_input / word / ml_string / replaced
    my_word = my_word.replace(new_word, user_say)
    a_list.append(my_word)
    a_string.index(new_word) + 1
    ext_sent = a_string.index(new_word) + 1
    new_sent = a_string[ext_sent:]
    #joins the indexed list with the rest of the full string
    return "\n"+ "\n" + " ".join(a_list) + " " + " ".join(new_sent)
#Function starts the game that was choosen by the user
def play_ball(a_sport):
    replaced = []
    if a_sport == "Basketball": #Prints the string and list associated with the Game Chosen
        ml_string = test_string1.split()
        list_of_answers = basketball_answers
        print  "\n" + test_string1 + "\n"#Passes in the list, answers to the game, and string for the game
        my_game = game_function(ml_string, list_of_answers)
    if a_sport == "Football": #Prints the string and list associated with the Game Chosen
        ml_string = test_string2.split()
        list_of_answers = football_answers
        print  "\n" + test_string2 + "\n" #Passes in the list, answers to the game, and string for the game
        my_game = game_function(ml_string, list_of_answers)
    if a_sport == "Soccer": #Prints the string and list associated with the Game Chosen
        ml_string = test_string3.split()
        list_of_answers = Soccer_answers
        print  "\n" + test_string3 + "\n" #Passes in the list, answers to the game, and string for the game
        my_game = game_function(ml_string, list_of_answers)
    return my_game

def playAGame(pic_game):
    print play_ball(pic_game)
#game_function(pic_game)
#pic_game = pick_Game
choose_game = pick_Game()
print playAGame(choose_game)
