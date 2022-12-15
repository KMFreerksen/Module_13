import random
import tkinter
from tkinter import *
from tkinter import messagebox

class NumberGuesser():
    def __init__(self):
        self.randomNum = 0
        self.guessed_list = []


    def StartGame(self):
        self.randomNum = random.randint(1,10)
        messagebox.showinfo(message="Random Number Generated; Start Guessing!!")
        start_button['state'] = DISABLED
        reset_button['state'] = NORMAL
        guess_1_button['state'] = NORMAL
        guess_2_button['state'] = NORMAL
        guess_3_button['state'] = NORMAL
        guess_4_button['state'] = NORMAL
        guess_5_button['state'] = NORMAL
        guess_6_button['state'] = NORMAL
        guess_7_button['state'] = NORMAL
        guess_8_button['state'] = NORMAL
        guess_9_button['state'] = NORMAL
        guess_10_button['state'] = NORMAL

    def ResetGame(self):
        self.guessed_list.clear() #clear out the guessed list for new game
        messagebox.showinfo(message="Game Reset")
        start_button['state'] = NORMAL
        reset_button['state'] = DISABLED
        guess_1_button['state'] = DISABLED
        guess_2_button['state'] = DISABLED
        guess_3_button['state'] = DISABLED
        guess_4_button['state'] = DISABLED
        guess_5_button['state'] = DISABLED
        guess_6_button['state'] = DISABLED
        guess_7_button['state'] = DISABLED
        guess_8_button['state'] = DISABLED
        guess_9_button['state'] = DISABLED
        guess_10_button['state'] = DISABLED

    def Guess_1(self):
        if self.randomNum == 1:
            messagebox.showinfo(message="Correct! The number was 1!")
            guess_1_button['state'] = DISABLED
            guess_2_button['state'] = DISABLED
            guess_3_button['state'] = DISABLED
            guess_4_button['state'] = DISABLED
            guess_5_button['state'] = DISABLED
            guess_6_button['state'] = DISABLED
            guess_7_button['state'] = DISABLED
            guess_8_button['state'] = DISABLED
            guess_9_button['state'] = DISABLED
            guess_10_button['state'] = DISABLED
        else:
            messagebox.showinfo(message="Guess Higher!")
            self.guessed_list.append(1)
            guess_1_button['state'] = DISABLED

    def Guess_2(self):
        if self.randomNum == 2:
            messagebox.showinfo(message="Correct! The number was 2!")
            guess_1_button['state'] = DISABLED
            guess_2_button['state'] = DISABLED
            guess_3_button['state'] = DISABLED
            guess_4_button['state'] = DISABLED
            guess_5_button['state'] = DISABLED
            guess_6_button['state'] = DISABLED
            guess_7_button['state'] = DISABLED
            guess_8_button['state'] = DISABLED
            guess_9_button['state'] = DISABLED
            guess_10_button['state'] = DISABLED
        else:
            if self.randomNum < 2:
                messagebox.showinfo(message="Guess Lower!")
            else:
                messagebox.showinfo(message="Guess Higher!")
            self.guessed_list.append(2)
            guess_2_button['state'] = DISABLED

    def Guess_3(self):
        if self.randomNum == 3:
            messagebox.showinfo(message="Correct! The number was 3!")
            guess_1_button['state'] = DISABLED
            guess_2_button['state'] = DISABLED
            guess_3_button['state'] = DISABLED
            guess_4_button['state'] = DISABLED
            guess_5_button['state'] = DISABLED
            guess_6_button['state'] = DISABLED
            guess_7_button['state'] = DISABLED
            guess_8_button['state'] = DISABLED
            guess_9_button['state'] = DISABLED
            guess_10_button['state'] = DISABLED
        else:
            if self.randomNum < 3:
                messagebox.showinfo(message="Guess Lower!")
            else:
                messagebox.showinfo(message="Guess Higher!")
            self.guessed_list.append(3)
            guess_3_button['state'] = DISABLED

    def Guess_4(self):
        if self.randomNum == 4:
            messagebox.showinfo(message="Correct! The number was 4!")
            guess_1_button['state'] = DISABLED
            guess_2_button['state'] = DISABLED
            guess_3_button['state'] = DISABLED
            guess_4_button['state'] = DISABLED
            guess_5_button['state'] = DISABLED
            guess_6_button['state'] = DISABLED
            guess_7_button['state'] = DISABLED
            guess_8_button['state'] = DISABLED
            guess_9_button['state'] = DISABLED
            guess_10_button['state'] = DISABLED
        else:
            if self.randomNum < 4:
                messagebox.showinfo(message="Guess Lower!")
            else:
                messagebox.showinfo(message="Guess Higher!")
            self.guessed_list.append(4)
            guess_4_button['state'] = DISABLED

    def Guess_5(self):
        if self.randomNum == 5:
            messagebox.showinfo(message="Correct! The number was 5!")
            guess_1_button['state'] = DISABLED
            guess_2_button['state'] = DISABLED
            guess_3_button['state'] = DISABLED
            guess_4_button['state'] = DISABLED
            guess_5_button['state'] = DISABLED
            guess_6_button['state'] = DISABLED
            guess_7_button['state'] = DISABLED
            guess_8_button['state'] = DISABLED
            guess_9_button['state'] = DISABLED
            guess_10_button['state'] = DISABLED
        else:
            if self.randomNum < 5:
                messagebox.showinfo(message="Guess Lower!")
            else:
                messagebox.showinfo(message="Guess Higher!")
            self.guessed_list.append(5)
            guess_5_button['state'] = DISABLED

    def Guess_6(self):
        if self.randomNum == 6:
            messagebox.showinfo(message="Correct! The number was 6!")
            guess_1_button['state'] = DISABLED
            guess_2_button['state'] = DISABLED
            guess_3_button['state'] = DISABLED
            guess_4_button['state'] = DISABLED
            guess_5_button['state'] = DISABLED
            guess_6_button['state'] = DISABLED
            guess_7_button['state'] = DISABLED
            guess_8_button['state'] = DISABLED
            guess_9_button['state'] = DISABLED
            guess_10_button['state'] = DISABLED
        else:
            if self.randomNum < 6:
                messagebox.showinfo(message="Guess Lower!")
            else:
                messagebox.showinfo(message="Guess Higher!")
            self.guessed_list.append(6)
            guess_6_button['state'] = DISABLED

    def Guess_7(self):
        if self.randomNum == 7:
            messagebox.showinfo(message="Correct! The number was 7!")
            guess_1_button['state'] = DISABLED
            guess_2_button['state'] = DISABLED
            guess_3_button['state'] = DISABLED
            guess_4_button['state'] = DISABLED
            guess_5_button['state'] = DISABLED
            guess_6_button['state'] = DISABLED
            guess_7_button['state'] = DISABLED
            guess_8_button['state'] = DISABLED
            guess_9_button['state'] = DISABLED
            guess_10_button['state'] = DISABLED
        else:
            if self.randomNum < 7:
                messagebox.showinfo(message="Guess Lower!")
            else:
                messagebox.showinfo(message="Guess Higher!")
            self.guessed_list.append(7)
            guess_7_button['state'] = DISABLED

    def Guess_8(self):
        if self.randomNum == 8:
            messagebox.showinfo(message="Correct! The number was 8!")
            guess_1_button['state'] = DISABLED
            guess_2_button['state'] = DISABLED
            guess_3_button['state'] = DISABLED
            guess_4_button['state'] = DISABLED
            guess_5_button['state'] = DISABLED
            guess_6_button['state'] = DISABLED
            guess_7_button['state'] = DISABLED
            guess_8_button['state'] = DISABLED
            guess_9_button['state'] = DISABLED
            guess_10_button['state'] = DISABLED
        else:
            if self.randomNum < 8:
                messagebox.showinfo(message="Guess Lower!")
            else:
                messagebox.showinfo(message="Guess Higher!")
            self.guessed_list.append(8)
            guess_8_button['state'] = DISABLED

    def Guess_9(self):
        if self.randomNum == 9:
            messagebox.showinfo(message="Correct! The number was 9!")
            guess_1_button['state'] = DISABLED
            guess_2_button['state'] = DISABLED
            guess_3_button['state'] = DISABLED
            guess_4_button['state'] = DISABLED
            guess_5_button['state'] = DISABLED
            guess_6_button['state'] = DISABLED
            guess_7_button['state'] = DISABLED
            guess_8_button['state'] = DISABLED
            guess_9_button['state'] = DISABLED
            guess_10_button['state'] = DISABLED
        else:
            if self.randomNum < 9:
                messagebox.showinfo(message="Guess Lower!")
            else:
                messagebox.showinfo(message="Guess Higher!")
            self.guessed_list.append(9)
            guess_9_button['state'] = DISABLED

    def Guess_10(self):
        if self.randomNum == 10:
            messagebox.showinfo(message="Correct! The number was 10!")
            guess_1_button['state'] = DISABLED
            guess_2_button['state'] = DISABLED
            guess_3_button['state'] = DISABLED
            guess_4_button['state'] = DISABLED
            guess_5_button['state'] = DISABLED
            guess_6_button['state'] = DISABLED
            guess_7_button['state'] = DISABLED
            guess_8_button['state'] = DISABLED
            guess_9_button['state'] = DISABLED
            guess_10_button['state'] = DISABLED
        else:
            messagebox.showinfo(message="Guess Lower!")
            self.guessed_list.append(10)
            guess_10_button['state'] = DISABLED


#create main window
m = tkinter.Tk()

#Main Window Title
m.title('Number Guessing Game')

label = tkinter.Label(m, text="Number Guessing Game")
label.grid(row=1)

#create a NumberGuesser object
game = NumberGuesser()

#Start button
start_button = tkinter.Button(m, text='Start', width=25, command=game.StartGame)
start_button.grid(row = 3)

#Guess Buttons
guess_1_button = tkinter.Button(m, text='Guess 1', width=12, command=game.Guess_1)
guess_1_button.grid(row = 5)

guess_2_button = tkinter.Button(m, text='Guess 2', width=12, command=game.Guess_2)
guess_2_button.grid(row = 6)

guess_3_button = tkinter.Button(m, text='Guess 3', width=12, command=game.Guess_3)
guess_3_button.grid(row = 7)

guess_4_button = tkinter.Button(m, text='Guess 4', width=12, command=game.Guess_4)
guess_4_button.grid(row = 8)

guess_5_button = tkinter.Button(m, text='Guess 5', width=12, command=game.Guess_5)
guess_5_button.grid(row = 9)

guess_6_button = tkinter.Button(m, text='Guess 6', width=12, command=game.Guess_6)
guess_6_button.grid(row = 10)

guess_7_button = tkinter.Button(m, text='Guess 7', width=12, command=game.Guess_7)
guess_7_button.grid(row = 11)

guess_8_button = tkinter.Button(m, text='Guess 8', width=12, command=game.Guess_8)
guess_8_button.grid(row = 12)

guess_9_button = tkinter.Button(m, text='Guess 9', width=12, command=game.Guess_9)
guess_9_button.grid(row = 13)

guess_10_button = tkinter.Button(m, text='Guess 10', width=12, command=game.Guess_10)
guess_10_button.grid(row = 14)

#Reset the Game
reset_button = tkinter.Button(m, text='Reset', width=25, command=game.ResetGame)
reset_button.grid(row = 16)

#exit
exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row = 18)
m.mainloop()
