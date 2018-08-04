# Hangman

A game for my computer science project.

This is made using the module [tkinter](https://wiki.python.org/moin/TkInter)

A word is selected randomly from the file `words.txt`.

All states (images) of the hung man are in the folder `images`.

<br>

## Functions and Variables

### Global
```
import math (math.floor) is used to calculate the positions for the ascii buttons.
import tkinter as tk #GUI stuff.
import random (random.choice) is used to pick a random word.
from string import ascii_uppercase is used for the ascii buttons.
WIDTH is used by tk widgets.
COLUMN_SPLIT is used by the tk widgets to space widgets across the grid.
ROW is a buffer used by mainGame to give room for the ascii buttons.
FONT is used by tk widgets to configure their font.

wordSet is used for picking a category. It is a tk.StringVar object.
```

### In class Controller(tk.Tk):

```
__init__() creates a container which holds both MainMenu and MainGame frames.
switchToFrame() brings a frame forward.
wordSetTrace() is a function called when the wordSet is changed. It called the reset function of the MainGame frame.
Variables:
    self.mainFrame holds both MainMenu and MainGame frames
```

### In class MainMenu(tk.Frame):
```
__init__() is called whenever a MainGame class is created. It is responsible for creating and displaying the buttons of that frame.
Variables:
    self.startButton is a button which calls controller.switchToFrame(MainGame). To start the game.
    self.wordSetLabel is a label which holds the text "Word list to use:".
    self.wordSetMenu is a tk.OptionMenu (dropdown menu) which allows the user to pick different wordSet(s).
```

### In class MainGame(tk.Frame):

```
__init__() is called whenever a MainGame class is created. It is responsible for creating and displaying the buttons of that frame.
Variables:
    self.width is used for the tk Labels
    self.wrongCounter is used to keep track of incorrect guesses and for picking images.
    self.imgLabel is the tk.Label widget for dissplaying the image of the hung man.
    self.wordLabel holds self.word in its hidden state.
    self.buttons is a list [A-Z] of buttons for player input.
        self.row & self.column hold the grid position of each button.
        Each button calls asciiOnButtonClick() with the character as a parameter.
    self.statusLabel shows the current state of the game and is changed to "You Win/Lose!"
    self.resetButton is the button which calls the function reset().


asciiButtonOnClick() is called whenever the player presses a button. It is used to find what characters should be revealed (based on the input), if any.
Variables:
    wordIndexes holds the positions of correct guesses.

updateText() is used to update self.textList with the new character(s) that the player guess. It is called by asciiOnButtonClick().

changeImg() is used to update the image of the hung man. It loads the .gif image of the current state of the hungman into the imgLabel. changeImg() is used by asciiOnButtonClick() and reset().

chooseWord() is used to pick a random word from words.txt and store the word in self.word. It is used by __init__() and reset().

reset() is used to reset the game at any point. It chooses a new word and resets all buttons and labels to default.
```

<br>

## TODO / IDEAS

#### Tasks I have completed will be ~~crossed out~~.

~~Automaticaly reset the main game when the wordSet is changed by the tk.OptionMenu.~~

~~I want to add a main menu to my program. And for that I'll add a new branch on github.~~

~~With this I can add in different categories:~~
* Names
* ~~Food~~
* Dinosaurs

~~Add colour feedback for asciiButtons (Change colour of letters [green/red] on button press).~~
