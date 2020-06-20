import tkinter as tk

window = tk.Tk()
frameTitle = tk.Frame(master=window)
frameTotalTime = tk.Frame(master=window)
frameCardStatus = tk.Frame(master=window)
frameCardTimer = tk.Frame(master=window)
frameCard = tk.Frame(master=window)
frameButtons = tk.Frame(master=window)

title = tk.Label(master=frameTitle,text="SSBM Flash Card Training Tool",font=("Arial", 16))
title.pack(pady=20)

totalTime = tk.Label(master=frameTotalTime,text="Session Time: 0:00",font=("Arial", 12))
totalTime.pack()

deckStatus = tk.Label(master=frameCardStatus,text="Deck m",font=("Arial", 12))
deckStatus.pack(side=tk.LEFT,padx = 10, pady=20)

cardStatus = tk.Label(master=frameCardStatus,text="Card n",font=("Arial", 12))
cardStatus.pack(side=tk.RIGHT,padx = 10)

cardTimer = tk.Label(master=frameCardTimer,text="Card Time: 0:00",font=("Arial", 12))
cardTimer.pack()

card = tk.Label(master=frameCard, text="Test Card",width =25, height = 5,relief=tk.SUNKEN,font=("Arial Bold", 20))
card.pack(pady = 0,padx=10)

start = tk.Button(
	master=frameButtons,
    text="Start",
    width=10,
    height=1,
    fg="green",
	font=("Arial", 12)
)
start.pack(side=tk.LEFT,padx = 10,pady=15)

next = tk.Button(
	master=frameButtons,
    text="Next",
    width=10,
    height=1,
	font=("Arial", 12)
)
next.pack(side=tk.RIGHT,padx = 10)

frameTitle.pack()
frameTotalTime.pack()
frameCardStatus.pack()
frameCard.pack()
frameCardTimer.pack()
frameButtons.pack()

window.mainloop()