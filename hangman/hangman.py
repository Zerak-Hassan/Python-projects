#Zerak
import random
import sys
try:#handles any errors to do with the word list
    #get the words
    f=open("word_list.txt", "r")
    words=f.readlines()
    f.close()
    #pick a random word
    num_words=len(words)
    word=(words[random.randrange(num_words)]).strip()
    word=word.lower()#makes non-case-sensitive
    #now to make the hangman guessing loop
    answer=list("_"*len(word))
except:
    print("Something is wrong with the word_list.\nHave you added words?")
    sys.exit()
guesses=[] #list that will contain all the letters guessed
x=5 #sets lives
while x >= 0: #Only run when have lives
    if "".join(answer) == word: #checks if answer is found
        break
    else:
        pass
    guess=input("".join(answer)+"\n"+"You have: "+str(x+1)+" guesses remaining.\n")#shows player the correctly guessed letters & the number of guesses that they have left
    guess=guess.lower()#makes non-case-sensitive
    try: # used a try except to handle no input from user
        for i in guesses:
            if guess[0]==i:
                print("You've already guessed",guess[0])#creates an error message if user has already guessed a letter
                raise IndexError("already guessed")
            else:
                pass
        correct = False
        n=-1
        for letter in word:#checks every letter in the word
            n += 1
            if guess[0] == letter:#case that guess is correct
                answer[n] = guess[0]
                correct = True
            else:
                pass
        if correct == False:#the case that letter is worng
            print("Incorrect.")
            x -= 1
        else:
            print("Correct")
        guesses=guesses+list(guess[0])#adds letter to guessed letters
    except IndexError:
        print("Your input was invalid.")
if x == -1:
    print("You lose.")#if the player runs out of lives
    print("The word was: "+word)
else:
    print("You win.")#if all the letters are guessed correctly 