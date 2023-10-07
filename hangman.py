#Program Description: Word guessing game similar to hangman where the user has to guess a randomly chosen word letter by letter.
#                     Game ends when the user guesses the entire word or makes 10 wrong guesses.
#Date created: 01/24/2021
#Date last modified: 05/19/2021
#Python Version: 3.0

#text colors for printing
class colors:
    green = '\033[32m' 
    red = '\033[31m'
    purple = '\033[35m'
    blue = "\033[34m"
    cyan = '\033[36m'
    reset = '\033[m'
#color code credits: https://www.instructables.com/Printing-Colored-Text-in-Python-Without-Any-Module/

#list of words
word_list = ['able', 'about', 'account', 'acid', 'across', 'addition', 
    'adjustment', 'advertisement', 'after', 'again', 'against', 'agreement', 
    'almost', 'among', 'amount', 'amusement', 'angle', 'angry', 'animal', 
    'answer', 'apparatus', 'apple', 'approval', 'arch', 'argument', 'army', 
    'attack', 'attempt', 'attention', 'attraction', 'authority', 'automatic', 
    'awake', 'baby', 'back', 'balance', 'ball', 'band', 'base', 'basin', 'basket', 
    'bath', 'beautiful', 'because', 'before', 'behaviour', 'belief', 'bell', 
    'bent', 'berry', 'between', 'bird', 'birth', 'bite', 'bitter', 'black', 
    'blade', 'blood', 'blow', 'blue', 'board', 'boat', 'body', 'boiling', 
    'bone', 'book', 'boot', 'bottle', 'brain', 'brake', 'branch', 'brass', 
    'bread', 'breath', 'brick', 'bridge', 'bright', 'broken', 'brother', 
    'brown', 'brush', 'bucket', 'building', 'bulb', 'burn', 'burst', 'business', 
    'butter', 'button', 'cake', 'camera', 'canvas', 'card', 'care', 'carriage', 
    'cart', 'cause', 'certain', 'chain', 'chalk', 'chance', 'change', 'cheap', 
    'cheese', 'chemical', 'chest', 'chief', 'chin', 'church', 'circle', 'clean', 
    'clear', 'clock', 'cloth', 'cloud', 'coal', 'coat', 'cold', 'collar', 'colour', 
    'comb', 'come', 'comfort', 'committee', 'common', 'company', 'comparison', 
    'competition', 'complete', 'complex', 'condition', 'connection', 'conscious', 
    'control', 'cook', 'copper', 'copy', 'cord', 'cork', 'cotton', 'cough', 'country', 
    'cover', 'crack', 'credit', 'crime', 'cruel', 'crush', 'current', 'curtain', 
    'curve', 'cushion', 'damage', 'danger', 'dark', 'daughter', 'dead', 'dear', 
    'death', 'debt', 'decision', 'deep', 'degree', 'delicate', 'dependent', 'design', 
    'desire', 'destruction', 'detail', 'development', 'different', 'digestion', 
    'direction', 'dirty', 'discovery', 'discussion', 'disease', 'disgust', 'distance', 
    'distribution', 'division', 'door', 'doubt', 'down', 'drain', 'drawer', 'dress', 
    'drink', 'driving', 'drop', 'dust', 'early', 'earth', 'east', 'edge', 'education', 
    'effect', 'elastic', 'electric', 'engine', 'enough', 'equal', 'error', 'even', 
    'event', 'ever', 'every', 'example', 'exchange', 'existence', 'expansion', 
    'experience', 'expert', 'face', 'fact', 'fall', 'false', 'family', 'farm', 'father', 
    'fear', 'feather', 'feeble', 'feeling', 'female', 'fertile', 'fiction', 'field', 
    'fight', 'finger', 'fire', 'first', 'fish', 'fixed', 'flag', 'flame', 'flat', 
    'flight', 'floor', 'flower', 'fold', 'food', 'foolish', 'foot', 'force', 'fork', 
    'form', 'forward', 'fowl', 'frame', 'free', 'frequent', 'friend', 'from', 'front', 
    'fruit', 'full', 'future', 'garden', 'general', 'girl', 'give', 'glass', 'glove', 
    'goat', 'gold', 'good', 'government', 'grain', 'grass', 'great', 'green', 'grey', 
    'grip', 'group', 'growth', 'guide', 'hair', 'hammer', 'hand', 'hanging', 'happy', 
    'harbour', 'hard', 'harmony', 'hate', 'have', 'head', 'healthy', 'hear', 'hearing', 
    'heart', 'heat', 'help', 'high', 'history', 'hole', 'hollow', 'hook', 'hope', 'horn', 
    'horse', 'hospital', 'hour', 'house', 'humour', 'idea', 'important', 'impulse', 
    'increase', 'industry', 'insect', 'instrument', 'insurance', 'interest', 'invention', 
    'iron', 'island', 'jelly', 'jewel', 'join', 'journey', 'judge', 'jump', 'keep', 'kettle', 
    'kick', 'kind', 'kiss', 'knee', 'knife', 'knot', 'knowledge', 'land', 'language', 'last', 
    'late', 'laugh', 'lead', 'leaf', 'learning', 'leather', 'left', 'letter', 'level', 
    'library', 'lift', 'light', 'like', 'limit', 'line', 'linen', 'liquid', 'list', 'little', 'living', 
    'lock', 'long', 'look', 'loose', 'loss', 'loud', 'love', 'machine', 'make', 'male', 'manager', 
    'mark', 'market', 'married', 'mass', 'match', 'material', 'meal', 'measure', 'meat', 'medical', 
    'meeting', 'memory', 'metal', 'middle', 'military', 'milk', 'mind', 'mine', 'minute', 'mist', 
    'mixed', 'money', 'monkey', 'month', 'moon', 'morning', 'mother', 'motion', 'mountain', 'mouth', 
    'move', 'much', 'muscle', 'music', 'nail', 'name', 'narrow', 'nation', 'natural', 'near', 
    'necessary', 'neck', 'need', 'needle', 'nerve', 'news', 'night', 'noise', 'normal', 'north', 
    'nose', 'note', 'number', 'observation', 'offer', 'office', 'only', 'open', 'operation', 
    'opinion', 'opposite', 'orange', 'order', 'organization', 'ornament', 'other', 'oven', 'over', 
    'owner', 'page', 'pain', 'paint', 'paper', 'parallel', 'parcel', 'part', 'past', 'paste', 
    'payment', 'peace', 'pencil', 'person', 'physical', 'picture', 'pipe', 'place', 'plane', 'plant', 
    'plate', 'play', 'please', 'pleasure', 'plough', 'pocket', 'point', 'poison', 'polish', 'political', 
    'poor', 'porter', 'position', 'possible', 'potato', 'powder', 'power', 'present', 'price', 'print', 
    'prison', 'private', 'probable', 'process', 'produce', 'profit', 'property', 'prose', 'protest', 
    'public', 'pull', 'pump', 'punishment', 'purpose', 'push', 'quality', 'question', 'quick', 'quiet', 
    'quite', 'rail', 'rain', 'range', 'rate', 'reaction', 'reading', 'ready', 'reason', 'receipt', 
    'record', 'regret', 'regular', 'relation', 'religion', 'representative', 'request', 'respect', 
    'responsible', 'rest', 'reward', 'rhythm', 'rice', 'right', 'ring', 'river', 'road', 'roll', 'roof', 
    'room', 'root', 'rough', 'round', 'rule', 'safe', 'sail', 'salt', 'same', 'sand', 'scale', 'school', 
    'science', 'scissors', 'screw', 'seat', 'second', 'secret', 'secretary', 'seed', 'seem', 'selection', 
    'self', 'send', 'sense', 'separate', 'serious', 'servant', 'shade', 'shake', 'shame', 'sharp', 'sheep', 
    'shelf', 'ship', 'shirt', 'shock', 'shoe', 'short', 'shut', 'side', 'sign', 'silk', 'silver', 'simple', 
    'sister', 'size', 'skin', 'skirt', 'sleep', 'slip', 'slope', 'slow', 'small', 'smash', 'smell', 
    'smile', 'smoke', 'smooth', 'snake', 'sneeze', 'snow', 'soap', 'society', 'sock', 'soft', 
    'solid', 'some', 'song', 'sort', 'sound', 'soup', 'south', 'space', 'spade', 'special', 
    'sponge', 'spoon', 'spring', 'square', 'stage', 'stamp', 'star', 'start', 'statement', 
    'station', 'steam', 'steel', 'stem', 'step', 'stick', 'sticky', 'stiff', 'still', 'stitch', 
    'stocking', 'stomach', 'stone', 'stop', 'store', 'story', 'straight', 'strange', 'street', 
    'stretch', 'strong', 'structure', 'substance', 'such', 'sudden', 'sugar', 'suggestion', 
    'summer', 'support', 'surprise', 'sweet', 'swim', 'system', 'table', 'tail', 'take', 
    'talk', 'tall', 'taste', 'teaching', 'tendency', 'test', 'than', 'that', 'then', 
    'theory', 'there', 'thick', 'thin', 'thing', 'this', 'thought', 'thread', 'throat', 
    'through', 'through', 'thumb', 'thunder', 'ticket', 'tight', 'till', 'time', 'tired', 
    'together', 'tomorrow', 'tongue', 'tooth', 'touch', 'town', 'trade', 'train', 
    'transport', 'tray', 'tree', 'trick', 'trouble', 'trousers', 'true', 'turn', 
    'twist', 'umbrella', 'under', 'unit', 'value', 'verse', 'very', 'vessel', 'view', 
    'violent', 'voice', 'waiting', 'walk', 'wall', 'warm', 'wash', 'waste', 'watch', 
    'water', 'wave', 'weather', 'week', 'weight', 'well', 'west', 'wheel', 'when', 
    'where', 'while', 'whip', 'whistle', 'white', 'wide', 'will', 'wind', 'window', 
    'wine', 'wing', 'winter', 'wire', 'wise', 'with', 'woman', 'wood', 'wool', 'word', 
    'work', 'worm', 'wound', 'writing', 'wrong', 'year', 'yellow', 'yesterday', 'young']
    #random word list credit: https://github.com/Xethron/Hangman 

#function to select a word randomly from the word list
def select_random_word(w_list):
   import random
   rand_word = random.choice(w_list) 
   return rand_word

#function to play game with the randomly selected word
def play_hangman(word, game_count=0, win_count=0, loss_count=0):
    #game_count, win_count, and loss_count initialized to 0 if parameters are not passed 
    #game count is incremented by one for the next game
    game_count += 1
    print("")           #formatting
    print(colors.cyan + "Game Number:", str(game_count) + colors.reset)
    print(colors.cyan + "Guess word with length:", len(word)*"_ " + colors.reset)
    guess_word = ""
    progress = len(word)*"_ "
    correct_letters = []
    all_letters = []
    wrong_count = 0
    #user gets 10 wrong guesses
    #while loop will continue until number of wrong guesses remains less than 10
    while wrong_count < 10:
        guess_letter = input(colors.blue + "Enter a letter you think is in this word: " + colors.reset)
        all_letters.append(guess_letter)
        #set variable guess_word to the correct word
        guess_word = word
        if guess_letter in word:
        #if the guessed letter is in the word
            #add letter to correct_letts list
            correct_letters.append(guess_letter)
            for x in word:
                #if the letter in the word has not been guessed yet, the letter will be replaced with a dash in guess_word
                if x not in correct_letters:
                    guess_word = guess_word.replace(x,"_ ") 
            progress = guess_word 
            #if all the letters in the word have been guessed
            if guess_word == word:
                print(word)
                #ask user if they would like to continue playing
                ask_next_game(game_count, win_count, loss_count, win=True)
                break
        else:
            #letter guessed was incorrect, increment wrong_count by 1
            wrong_count = wrong_count + 1
            print(colors.red + "The letter", guess_letter, "is not in this word." + colors.reset)
            if wrong_count == 10:
                #maximum number of wrong guesses reached
                #ask user if they would like to continue playing
                ask_next_game(game_count, win_count, loss_count, word, win=False)
                continue
            else:
                print("You have", 10 - wrong_count, "chances left.")
        #print the user's progress (dashes are replaced with correctly guessed letters)
        print(progress)
        print("")           #formatting
        print("You have guessed these letters:", all_letters)

#function to print game stats
def print_game_stat(game_count, win_count, loss_count, last_game=None):
    if last_game is None:
        #not the last game, user would like to keep playing so print the current stats
        print(colors.blue + "Number of games played:", str(game_count) + colors.reset)
        print(colors.green + "Wins:", str(win_count) + colors.reset)
        print(colors.red + "Losses:", str(loss_count) + colors.reset)
    elif last_game is True:
        #user is done playing, print the win percentage and performance
        if game_count > 0:
            win_percent = (win_count/game_count)*100
            print("")           #formatting
            print(colors.green + "Your win percentage:", str(win_percent) + colors.reset)
            if win_percent >= 80: 
                print(colors.green + "You are AMAZING!" + colors.reset)
            elif win_percent >= 60:
                print(colors.green + "You are good!" + colors.reset)
            else:
                print(colors.green + "You need to practice more." + colors.reset)
        print(colors.cyan + "Thanks for playing! :)" + colors.reset)    


#function asks user if they would like to play again
def ask_next_game(game_count, win_count, loss_count, word=None, win=None):
    if win is True:
        win_count += 1
        print(colors.green + "CONGRATS!!! You have guessed the word!" + colors.reset)
        print_game_stat(game_count, win_count, loss_count)
    elif win is False:
        loss_count += 1
        print(colors.red + "You LOSE :(. The correct word was", word + "." + colors.reset)
        print_game_stat(game_count, win_count, loss_count)
    print("")
    play_again = input(colors.cyan + "Play again? Yes = Y or No = N:" + colors.reset)
    if play_again.upper() == "Y" or play_again.upper() == "YES":
        print(colors.green + "Let's play again!" + colors.reset)
        selected_word = select_random_word(word_list)
        #calling play_hangman to play again, passing game counts,  win counts, and loss counts
        play_hangman(selected_word, game_count, win_count, loss_count)
    elif play_again.upper() == "N" or play_again.upper() == "NO":
        print_game_stat(game_count, win_count, loss_count, last_game=True)
    else:
        #user input for play_again is invalid so asking again if they want to continue playing
        print(colors.red + "Invalid input." + colors.reset)
        ask_next_game(game_count, win_count, loss_count)

#main function
def main():
    selected_word = select_random_word(word_list)
    #calling play_hangman for the first time (did not pass game counts,  win counts, and loss counts)
    play_hangman(selected_word)

#main function call
main()
