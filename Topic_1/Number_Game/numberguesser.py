import random
import tkinter
from tkinter import *
from tkinter import messagebox

class NumberGuesser:
    def __init__(self):
        self.randomNum = 0
        self.guessed_list = []
        self.start_button = tkinter.Button(text='Start', width=25, command=self.StartGame)
        self.reset_button = tkinter.Button(text='Reset', width=25, command=self.ResetGame, state=DISABLED)
        self.guess_1_button = tkinter.Button(text='Guess 1', width=12, command=self.Guess_1, state=DISABLED)
        self.guess_2_button = tkinter.Button(text='Guess 2', width=12, command=self.Guess_2, state=DISABLED)
        self.guess_3_button = tkinter.Button(text='Guess 3', width=12, command=self.Guess_3, state=DISABLED)
        self.guess_4_button = tkinter.Button(text='Guess 4', width=12, command=self.Guess_4, state=DISABLED)
        self.guess_5_button = tkinter.Button(text='Guess 5', width=12, command=self.Guess_5, state=DISABLED)
        self.guess_6_button = tkinter.Button(text='Guess 6', width=12, command=self.Guess_6, state=DISABLED)
        self.guess_7_button = tkinter.Button(text='Guess 7', width=12, command=self.Guess_7, state=DISABLED)
        self.guess_8_button = tkinter.Button(text='Guess 8', width=12, command=self.Guess_8, state=DISABLED)
        self.guess_9_button = tkinter.Button(text='Guess 9', width=12, command=self.Guess_9, state=DISABLED)
        self.guess_10_button = tkinter.Button(text='Guess 10', width=12, command=self.Guess_10, state=DISABLED)

    def StartGame(self):
        self.randomNum = random.randint(1, 10)
        messagebox.showinfo(message="Random Number Generated; Start Guessing!!")
        self.start_button['state'] = DISABLED
        self.reset_button['state'] = NORMAL
        self.guess_1_button['state'] = NORMAL
        self.guess_2_button['state'] = NORMAL
        self.guess_3_button['state'] = NORMAL
        self.guess_4_button['state'] = NORMAL
        self.guess_5_button['state'] = NORMAL
        self.guess_6_button['state'] = NORMAL
        self.guess_7_button['state'] = NORMAL
        self.guess_8_button['state'] = NORMAL
        self.guess_9_button['state'] = NORMAL
        self.guess_10_button['state'] = NORMAL

    def ResetGame(self):
        self.guessed_list.clear() #clear out the guessed list for new game
        messagebox.showinfo(message="Game Reset")
        self.start_button['state'] = NORMAL
        self.reset_button['state'] = DISABLED
        self.guess_1_button['state'] = DISABLED
        self.guess_2_button['state'] = DISABLED
        self.guess_3_button['state'] = DISABLED
        self.guess_4_button['state'] = DISABLED
        self.guess_5_button['state'] = DISABLED
        self.guess_6_button['state'] = DISABLED
        self.guess_7_button['state'] = DISABLED
        self.guess_8_button['state'] = DISABLED
        self.guess_9_button['state'] = DISABLED
        self.guess_10_button['state'] = DISABLED

    def Guess_1(self):
        if self.randomNum == 1:
            self.messagebox.showinfo(message="Correct! The number was 1!")
            self.guess_1_button['state'] = DISABLED
            self.guess_2_button['state'] = DISABLED
            self.guess_3_button['state'] = DISABLED
            self.guess_4_button['state'] = DISABLED
            self.guess_5_button['state'] = DISABLED
            self.guess_6_button['state'] = DISABLED
            self.guess_7_button['state'] = DISABLED
            self.guess_8_button['state'] = DISABLED
            self.guess_9_button['state'] = DISABLED
            self.guess_10_button['state'] = DISABLED
        else:
            messagebox.showinfo(message="Guess Higher!")
            self.guessed_list.append(1)
            self.guess_1_button['state'] = DISABLED

    def Guess_2(self):
        if self.randomNum == 2:
            messagebox.showinfo(message="Correct! The number was 2!")
            self.guess_1_button['state'] = DISABLED
            self.guess_2_button['state'] = DISABLED
            self.guess_3_button['state'] = DISABLED
            self.guess_4_button['state'] = DISABLED
            self.guess_5_button['state'] = DISABLED
            self.guess_6_button['state'] = DISABLED
            self.guess_7_button['state'] = DISABLED
            self.guess_8_button['state'] = DISABLED
            self.guess_9_button['state'] = DISABLED
            self.guess_10_button['state'] = DISABLED
        else:
            if self.randomNum < 2:
                messagebox.showinfo(message="Guess Lower!")
            else:
                messagebox.showinfo(message="Guess Higher!")
            self.guessed_list.append(2)
            self.guess_2_button['state'] = DISABLED

    def Guess_3(self):
        if self.randomNum == 3:
            messagebox.showinfo(message="Correct! The number was 3!")
            self.guess_1_button['state'] = DISABLED
            self.guess_2_button['state'] = DISABLED
            self.guess_3_button['state'] = DISABLED
            self.guess_4_button['state'] = DISABLED
            self.guess_5_button['state'] = DISABLED
            self.guess_6_button['state'] = DISABLED
            self.guess_7_button['state'] = DISABLED
            self.guess_8_button['state'] = DISABLED
            self.guess_9_button['state'] = DISABLED
            self.guess_10_button['state'] = DISABLED
        else:
            if self.randomNum < 3:
                messagebox.showinfo(message="Guess Lower!")
            else:
                messagebox.showinfo(message="Guess Higher!")
            self.guessed_list.append(3)
            self.guess_3_button['state'] = DISABLED

    def Guess_4(self):
        if self.randomNum == 4:
            messagebox.showinfo(message="Correct! The number was 4!")
            self.guess_1_button['state'] = DISABLED
            self.guess_2_button['state'] = DISABLED
            self.guess_3_button['state'] = DISABLED
            self.guess_4_button['state'] = DISABLED
            self.guess_5_button['state'] = DISABLED
            self.guess_6_button['state'] = DISABLED
            self.guess_7_button['state'] = DISABLED
            self.guess_8_button['state'] = DISABLED
            self.guess_9_button['state'] = DISABLED
            self.guess_10_button['state'] = DISABLED
        else:
            if self.randomNum < 4:
                messagebox.showinfo(message="Guess Lower!")
            else:
                messagebox.showinfo(message="Guess Higher!")
            self.guessed_list.append(4)
            self.guess_4_button['state'] = DISABLED

    def Guess_5(self):
        if self.randomNum == 5:
            messagebox.showinfo(message="Correct! The number was 5!")
            self.guess_1_button['state'] = DISABLED
            self.guess_2_button['state'] = DISABLED
            self.guess_3_button['state'] = DISABLED
            self.guess_4_button['state'] = DISABLED
            self.guess_5_button['state'] = DISABLED
            self.guess_6_button['state'] = DISABLED
            self.guess_7_button['state'] = DISABLED
            self.guess_8_button['state'] = DISABLED
            self.guess_9_button['state'] = DISABLED
            self.guess_10_button['state'] = DISABLED
        else:
            if self.randomNum < 5:
                messagebox.showinfo(message="Guess Lower!")
            else:
                messagebox.showinfo(message="Guess Higher!")
            self.guessed_list.append(5)
            self.guess_5_button['state'] = DISABLED

    def Guess_6(self):
        if self.randomNum == 6:
            messagebox.showinfo(message="Correct! The number was 6!")
            self.guess_1_button['state'] = DISABLED
            self.guess_2_button['state'] = DISABLED
            self.guess_3_button['state'] = DISABLED
            self.guess_4_button['state'] = DISABLED
            self.guess_5_button['state'] = DISABLED
            self.guess_6_button['state'] = DISABLED
            self.guess_7_button['state'] = DISABLED
            self.guess_8_button['state'] = DISABLED
            self.guess_9_button['state'] = DISABLED
            self.guess_10_button['state'] = DISABLED
        else:
            if self.randomNum < 6:
                messagebox.showinfo(message="Guess Lower!")
            else:
                messagebox.showinfo(message="Guess Higher!")
            self.guessed_list.append(6)
            self.guess_6_button['state'] = DISABLED

    def Guess_7(self):
        if self.randomNum == 7:
            messagebox.showinfo(message="Correct! The number was 7!")
            self.guess_1_button['state'] = DISABLED
            self.guess_2_button['state'] = DISABLED
            self.guess_3_button['state'] = DISABLED
            self.guess_4_button['state'] = DISABLED
            self.guess_5_button['state'] = DISABLED
            self.guess_6_button['state'] = DISABLED
            self.guess_7_button['state'] = DISABLED
            self.guess_8_button['state'] = DISABLED
            self.guess_9_button['state'] = DISABLED
            self.guess_10_button['state'] = DISABLED
        else:
            if self.randomNum < 7:
                messagebox.showinfo(message="Guess Lower!")
            else:
                messagebox.showinfo(message="Guess Higher!")
            self.guessed_list.append(7)
            self.guess_7_button['state'] = DISABLED

    def Guess_8(self):
        if self.randomNum == 8:
            messagebox.showinfo(message="Correct! The number was 8!")
            self.guess_1_button['state'] = DISABLED
            self.guess_2_button['state'] = DISABLED
            self.guess_3_button['state'] = DISABLED
            self.guess_4_button['state'] = DISABLED
            self.guess_5_button['state'] = DISABLED
            self.guess_6_button['state'] = DISABLED
            self.guess_7_button['state'] = DISABLED
            self.guess_8_button['state'] = DISABLED
            self.guess_9_button['state'] = DISABLED
            self.guess_10_button['state'] = DISABLED
        else:
            if self.randomNum < 8:
                messagebox.showinfo(message="Guess Lower!")
            else:
                messagebox.showinfo(message="Guess Higher!")
            self.guessed_list.append(8)
            self.guess_8_button['state'] = DISABLED

    def Guess_9(self):
        if self.randomNum == 9:
            messagebox.showinfo(message="Correct! The number was 9!")
            self.guess_1_button['state'] = DISABLED
            self.guess_2_button['state'] = DISABLED
            self.guess_3_button['state'] = DISABLED
            self.guess_4_button['state'] = DISABLED
            self.guess_5_button['state'] = DISABLED
            self.guess_6_button['state'] = DISABLED
            self.guess_7_button['state'] = DISABLED
            self.guess_8_button['state'] = DISABLED
            self.guess_9_button['state'] = DISABLED
            self.guess_10_button['state'] = DISABLED
        else:
            if self.randomNum < 9:
                messagebox.showinfo(message="Guess Lower!")
            else:
                messagebox.showinfo(message="Guess Higher!")
            self.guessed_list.append(9)
            self.guess_9_button['state'] = DISABLED

    def Guess_10(self):
        if self.randomNum == 10:
            messagebox.showinfo(message="Correct! The number was 10!")
            self.guess_1_button['state'] = DISABLED
            self.guess_2_button['state'] = DISABLED
            self.guess_3_button['state'] = DISABLED
            self.guess_4_button['state'] = DISABLED
            self.guess_5_button['state'] = DISABLED
            self.guess_6_button['state'] = DISABLED
            self.guess_7_button['state'] = DISABLED
            self.guess_8_button['state'] = DISABLED
            self.guess_9_button['state'] = DISABLED
            self.guess_10_button['state'] = DISABLED
        else:
            messagebox.showinfo(message="Guess Lower!")
            self.guessed_list.append(10)
            self.guess_10_button['state'] = DISABLED

#create main window
m = tkinter.Tk()

#Main Window Title
m.title('Number Guessing Game')

label = tkinter.Label(m, text="Number Guessing Game")
label.grid(row=1)

#create a NumberGuesser object
game = NumberGuesser()

#Start button
game.start_button.grid(row=2)

#Guess Buttons
game.guess_1_button.grid(row=3)
game.guess_2_button.grid(row=4)
game.guess_3_button.grid(row=5)
game.guess_4_button.grid(row=6)
game.guess_5_button.grid(row=7)
game.guess_6_button.grid(row=8)
game.guess_7_button.grid(row=9)
game.guess_8_button.grid(row=10)
game.guess_9_button.grid(row=11)
game.guess_10_button.grid(row=12)

#Reset the Game
game.reset_button.grid(row=13)

#exit
exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=18)
m.mainloop()
