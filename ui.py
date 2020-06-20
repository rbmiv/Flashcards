import tkinter as tk


window = tk.Tk()
frameTitle = tk.Frame(master=window)
frameTotalTime = tk.Frame(master=window)
frameCardStatus = tk.Frame(master=window)
frameCardTimer = tk.Frame(master=window)
frameCard = tk.Frame(master=window)
frameButtons = tk.Frame(master=window)

title = tk.Label(master=frameTitle,text="Super Smash Bros. Melee Flash Card Training Tool")
title.pack()

totalTime = tk.Label(master=frameTotalTime,text="Test Total Time")
totalTime.pack()

deckStatus = tk.Label(master=frameCardStatus,text="Deck N")
deckStatus.pack()

cardStatus = tk.Label(master=frameCardStatus,text="Card N")
cardStatus.pack()

cardTimer = tk.Label(master=frameCardTimer,text="Test Card Timer")
cardTimer.pack()

card = tk.Label(master=frameCard, text="Test Card")
card.pack()

start = tk.Button(
	master=frameButtons,
    text="Start",
    width=15,
    height=3,
    fg="green",
)

next = tk.Button(
	master=frameButtons,
    text="Next",
    width=15,
    height=3
)

start.pack()
next.pack()
frameTitle.pack()
frameTotalTime.pack()
frameCardStatus.pack()
frameCardTimer.pack()
frameCard.pack()
frameButtons.pack()

window.mainloop()