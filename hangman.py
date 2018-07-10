import math
import tkinter as tk
import random
from string import ascii_uppercase


class mainGame():
    def __init__(self, parent):
        self.parent = parent

        self.chooseWord()

        self.won = False

        # IMAGE LABEL
        self.wrongCounter = 0
        self.img = tk.PhotoImage(file=f'images/{self.wrongCounter}.gif')
        self.imgLabel = tk.Label(self.parent, image=self.img)
        self.imgLabel.grid(row=0, column=0, columnspan=COLUMN_SPLIT)


        # GUESS WORD LABEL
        self.textList = []
        for char in range(len(self.word)-1):
            self.textList.append('_ ')
        self.textList.append('_')
        self.text = ''.join(self.textList)

        self.wordLabel = tk.Label(self.parent, text=self.text, width=25, font=(
            'Source', 18, 'bold'), bg='black', fg='white', anchor=tk.CENTER)
        self.wordLabel.grid(row=1, column=0, columnspan=COLUMN_SPLIT)

        self.buttons = []
        letters = list(ascii_uppercase)
        for index in range(len(letters)):
            char = letters[index]
            button = tk.Button(self.parent, text=char, width=5, height=1, bg='black', fg='white',
                            relief=tk.GROOVE, command=lambda index=index, char=char: self.asciiButtonOnClick(index, char))

            button.grid(padx=2, pady=2, row=math.floor((index/COLUMN_SPLIT)+ROW), column=index % COLUMN_SPLIT)
            # print(f'{char} - {math.floor((index/COLUMN_SPLIT)+ROW)}, {index%COLUMN_SPLIT}')

            self.buttons.append(button)

        self.resetButton = tk.Button(self.parent, text='RESET', font=('Source', 18, 'bold'), width=25, bg='black', fg='white',
                                     relief=tk.GROOVE, command=self.reset)
        self.resetButton.grid(row=5, column=0, columnspan=COLUMN_SPLIT, pady=20)

    def asciiButtonOnClick(self, index, char):
        if not self.won:
            self.buttons[index].configure(state='disabled')

            wordIndexes = []
            if char in self.word:  # correct guess
                for charIndex in range(len(self.word)):
                    if char == self.word[charIndex]:
                        wordIndexes.append(charIndex)
                self.updateText(char, wordIndexes)

                if not '_' in self.text: # you win
                    self.wordLabel.configure(text='You Win!\n' + self.text)
                    self.won = True

            else:  # incorrect guess
                self.wrongCounter += 1

                self.changeImg(self.wrongCounter)
                if self.wrongCounter >= 10:
                    self.wordLabel.configure(text='You Lose!\n' + self.word)

    def updateText(self, char, charIndexes):
        for index in charIndexes:
            if index == len(self.textList)-1:
                self.textList[index] = char
            else:
                self.textList[index] = char + ' '

        self.text = ''.join(self.textList)
        self.wordLabel.configure(text=self.text)

    def changeImg(self, imgNum):
        self.img = tk.PhotoImage(file=f'images/{imgNum}.gif')
        self.imgLabel.configure(image=self.img)

    def chooseWord(self):
        with open('words.txt', 'r') as f:
            words = f.read().split('\n')
            f.close()
        self.word = random.choice(words).upper()

    def reset(self):
        self.chooseWord()

        self.textList = []
        for char in range(len(self.word)-1):
            self.textList.append('_ ')
        self.textList.append('_')
        self.text = ''.join(self.textList)
        self.wordLabel.configure(text=self.text)

        self.wrongCounter = 0
        self.changeImg(self.wrongCounter)

        for button in self.buttons:
            button.configure(state='normal')

        self.won = False



COLUMN_SPLIT = 9
ROW = 2
if __name__ == '__main__':
    root = tk.Tk()
    root.title('Hangman - CoryEvans')
    # root.geometry('600x600+0+0')
    gui = mainGame(root)
    root.mainloop()
