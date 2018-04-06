# The user has 5 attempts to correctly guess
number_to_win = 5

# The following are the possible strings for the quiz pass in to the start_game function.
quiz_easy_text = "Roses are __1__, violets are __2__," \
                "\nsugar is __3__, and so are __4__."
quiz_easy_answers = ["red", "blue", "sweet", "you"]

quiz_medium_text = "Sing with me, sing for the __1__" \
                "\nSing for the laughter, sing for the __2__" \
                "\nSing with me, just for __3__" \
                "\nMaybe tomorrow, the good Lord will take you __4__"
quiz_medium_answers = ["years", "tears", "today", "away"]

quiz_hard_text = "The __1__  don't like __2__" \
                "\nRocking the __3__  \n__4__ the Casbah"
quiz_hard_answers = ["Shareef", "it", "Casbah", "Rock"]

quiz_data = {
    "easy": (quiz_easy_text, quiz_easy_answers),
    "medium": (quiz_medium_text, quiz_medium_answers),
    "hard": (quiz_hard_text, quiz_hard_answers)}


# Returns corresponding text and answers
def get_quiz_data(chosen_difficulty):
    return quiz_data[chosen_difficulty]


# Tracks if the input corresponds with answers
def word_index(word, answers):
    counter = 0
    for pos in answers:
        if pos == word:
            return counter
        counter = counter + 1
    return None


# Prints the selected quiz, tracks inputs and number of wrong attempts
def get_answer(quiz_text, quiz_answers, question_number, wrong_attempts):
    print quiz_text
    current_question = "__" + str(question_number + 1) + "__"
    while True:
        user_input = raw_input("\nType in a " + current_question + ":")
        word_pos = word_index(user_input, quiz_answers)
        if word_pos == question_number:
            quiz_text = quiz_text.replace(current_question, user_input)
            return (quiz_text, wrong_attempts)
        else:
            print "\nWrong answer, you have " + str(number_to_win - 1 - wrong_attempts) + " attempt left"
            wrong_attempts = wrong_attempts + 1
        if wrong_attempts >= number_to_win:
            return (quiz_text, wrong_attempts)


# Function returns true if user finished game in less than number_to_win wrong attempts
def finish_the_game(quiz_text, quiz_answers):
    question_wording = quiz_text
    wrong_attempts = 0
    question_number = 0
    for answer in quiz_answers:
        question_wording, wrong_attempts = get_answer(question_wording, quiz_answers, question_number, wrong_attempts)
        if wrong_attempts >= number_to_win:
            return False
        question_number = question_number + 1
    print question_wording
    return True


# Asks the user to select a difficulty for the game
def get_game_difficulty():
    difficulties = ['easy', 'medium', 'hard']
    prompt = "Select a difficulty (easy, medium, or hard):"

    chosen_difficulty = raw_input(prompt).lower()
    while chosen_difficulty not in difficulties:
        print "The options are easy, medium, or hard"
        chosen_difficulty = raw_input(prompt).lower()

    return chosen_difficulty


# Plays a full quiz game. A player is prompted to guess the words correctly,
def start_game():
    print "Welcome to the quiz!\n"
    game_difficulty = get_game_difficulty()

    quiz_text, quiz_answers = get_quiz_data(game_difficulty)
    won = finish_the_game(quiz_text, quiz_answers)
    if won == True:
        print "\nYou have won!"
    else:
        print "\nYou have lost."

start_game()