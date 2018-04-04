# A list of replacement words to be passed in to the play game function.
parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN", "NAME", "VERB", "OCCUPATION", "ADJECTIVE"]

# The following are some test strings to pass in to the play_game function.
quiz_easy = "Hi, my name is NAME and I really like to VERB PLURALNOUN. I'm also a OCCUPATION at PLACE."
quiz_medium = """PERSON! What is PERSON going to do with all these ADJECTIVE PLURALNOUN? Only a registered
OCCUPATION could VERB them."""
quiz_hard = "What a ADJECTIVE day! I can VERB the day off from being a OCCUPATION and go VERB at PLACE."

# Checks if a word in parts_of_speech is a substring of the word passed in.
def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

# Plays a full game of mad_libs. A player is prompted to replace words in ml_string,
# which appear in parts_of_speech with their own words.
def play_game(ml_string, parts_of_speech):
    replaced = []
    ml_string = ml_string.split()
    for word in ml_string:
        replacement = word_in_pos(word, parts_of_speech)
        if replacement != None:
            user_input = raw_input("Type in a: " + replacement + " ")
            word = word.replace(replacement, user_input)
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced

def get_game_difficulty():
    difficulties = ['easy', 'medium', 'hard']
    prompt = "To begin, select a difficulty (easy, medium, or hard): "

    chosen_difficulty = raw_input(prompt).lower()
    while chosen_difficulty not in difficulties:
        print "The options are easy, medium, or hard"
        chosen_difficulty = raw_input(prompt).lower()
    
    return chosen_difficulty

def start_game():
    print "Welcome to the quiz!"
    game_difficulty = get_game_difficulty()
    test = ""
    if game_difficulty == "easy":
        test = quiz_easy
    elif game_difficulty == "medium":
        test = quiz_medium
    elif game_difficulty == "hard":
        test = quiz_hard
    print play_game(test, parts_of_speech)
    print "done " + game_difficulty

start_game()
