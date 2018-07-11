import math
import tkinter as tk
import random
from string import ascii_uppercase

# main game class I put this in a class to be able to add different tk.Frames in the future.
class mainGame():
    # the __init__ function is called whenever a class object is created.
    def __init__(self, parent):
        self.parent = parent # to be used later for other functions.
        self.width = 27 # used fot tk widgets.

        # starting the game
        self.chooseWord() # pick a word and generate the underscores.
        self.wrongCounter = 0

        # IMAGE LABEL
        # A tk.Label which holds an image of the current state of the hung man.
        self.img = tk.PhotoImage(file=f'images/{self.wrongCounter}.gif')
        self.imgLabel = tk.Label(self.parent, image=self.img)
        self.imgLabel.grid(row=0, column=0, columnspan=COLUMN_SPLIT)


        # GUESS WORD LABEL
        # A tk.Label which holds the word as underscores. (and with spaces in-between characters)
        # Example: C _ E _ _ T S

        # The actual word label witch holds the text.
        self.wordLabel = tk.Label(self.parent, text=self.text, width=self.width, font=('Source', 18, 'bold'),
                                  bg='black', fg='white', anchor=tk.CENTER)
        self.wordLabel.grid(row=1, column=0, columnspan=COLUMN_SPLIT, pady=5)

        # 26 buttons containing the alphabet
        self.buttons = []
        letters = list(ascii_uppercase)
        for index in range(len(letters)): # 0 ---> 25
            char = letters[index]  # A ---> Z
            button = tk.Button(self.parent, text=char, width=5, height=1, bg='black', fg='white',
                               relief=tk.GROOVE, command=lambda index=index, char=char: self.asciiButtonOnClick(index, char))

            # Finding the row and column (position) for each button.
            # The constant ROW is a buffer from the image label and word label
            # The constant COLUMN_SPLIT is how wide the image/word labels are (column span).
            # math.floor(num) rounds down the the nearest interger.
            # Since COLUMN_SPLIT is 9 and index has a max of 26 different values.

            # rounding down index/COLUMN_SPLIT would go from 0 ---> 2 (3 different rows). ROW is just a buffer.
            self.row = math.floor((index/COLUMN_SPLIT)+ROW)

            # Since I wanted 3 rows, and I have 26 buttons, COLUMN_SPLIT had to be 9, giving one buttons left over.
            # index % COLUMN_SPLIT would give the position until a new row is created.
            self.column = index % COLUMN_SPLIT

            # Add all each button to the grid and append them to a list of buttons.
            button.grid(row=self.row, column=self.column)
            self.buttons.append(button)

        # STATUS BUTTON
        # Used to tell the player if the won or lost.
        self.statusLabel = tk.Label(self.parent, font=('Source', 18, 'bold'), width=self.width, bg='black', fg='white',
                                    relief=tk.GROOVE)
        self.row += 1
        self.statusLabel.grid(row=self.row, column=0, columnspan=COLUMN_SPLIT, pady=5)

        # RESET BUTTON
        self.resetButton = tk.Button(self.parent, text='RESET', font=('Source', 18, 'bold'), width=self.width, bg='black', fg='white',
                                     relief=tk.GROOVE, command=self.reset)
        self.row += 1
        self.resetButton.grid(row=self.row, column=0, columnspan=COLUMN_SPLIT)

    def asciiButtonOnClick(self, index, char):
        self.buttons[index].configure(state='disabled') # Disable the button that was pressed

        wordIndexes = [] # list to hold the positions of the guessed letter in the word.
        if char in self.word:  # correct guess
            for charIndex in range(len(self.word)): # for each char in word:
                if char == self.word[charIndex]: # if the guessed letter is in word:
                    wordIndexes.append(charIndex) # append the index to the list.
            self.updateText(char, wordIndexes) # update the wordLabel if it needs to be updated.

            if not '_' in self.text: # you win as all letters have been revealed. (no more underscores)
                self.statusLabel.configure(text='You Win!')

        else:  # incorrect guess
            self.wrongCounter += 1
            self.changeImg(self.wrongCounter)

            if self.wrongCounter >= 10: # if 10 incorrect guesses: You lose!
                self.wordLabel.configure(text=self.word) # reveal the word.
                self.statusLabel.configure(text='You Lose!') # Tell the player.

                # disable all buttons at end of game
                for button in self.buttons:
                    button.configure(state='disabled')

    def updateText(self, char, charIndexes):
        for index in charIndexes:
            if index == len(self.textList)-1: # If it is the last character in the text
                self.textList[index] = char

            else: # else its not so a space has to be added to the character
                self.textList[index] = char + ' '

        self.text = ''.join(self.textList) # turn list into string
        self.wordLabel.configure(text=self.text) # update the wordLabel

    def changeImg(self, imgID): # imgID in this case is the wrongCounter.
        self.img = tk.PhotoImage(file=f'images/{imgID}.gif') # Open the image
        self.imgLabel.configure(image=self.img) # set the image to the imageLabel

    def chooseWord(self): # when starting or reseting a game: pick a word from words.txt
        with open('words.txt', 'r') as f:
            words = f.read().split('\n') # split into list at each newline character.
            f.close()
        # random.choice picks a random item from an iterable.
        self.word = random.choice(words).upper() # str().upper() converts the string to uppercase.

        self.textList = []
        for char in range(len(self.word)-1): # used to add a space after each underscore. (except for the last underscore)
            self.textList.append('_ ')
        self.textList.append('_')  # last underscore

        # str().join(iterable) merges the str in-between the items in the iterable into one string.
        # Since the str is empty, the empty string would be placed between each '_ ' and ' '. ['_ ', '_ ', '_ ', '_'] ---> '_ _ _ _'
        self.text = ''.join(self.textList)

    def reset(self): # called when resetButton is pressed.
        self.chooseWord() # pick a new word.

        self.wordLabel.configure(text=self.text) # update the wordLabel
        self.statusLabel.configure(text='') # update the statusLabel

        self.wrongCounter = 0 # reset counter
        self.changeImg(self.wrongCounter) # update image

        # enable all buttons at start of game
        for button in self.buttons:
            button.configure(state='normal')



COLUMN_SPLIT = 9 # Width of the grid.
ROW = 2 # A buffer used be the imageLabel and wordLabel, to give room for the alphabet buttons.

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Hangman - CoryEvans')
    root.resizable(False, False)
    gui = mainGame(root)
    root.mainloop()
