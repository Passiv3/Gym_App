# Author: Danny Chung
# Date: 10/26/21
# Description: Frames for use with notebook

import tkinter as tk
from tkinter import ttk
import commands


class homeFrame(tk.Frame):
    """
    Home Page
    """

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        textBox = tk.Text(self, height=10, width=60, wrap="word")
        textBox.place(relx=.5, rely=.5, anchor="center")

        About = "Application written by Danny Chung for CS361\n" \
            "------------------------\n" \
            "HOW TO USE\n" \
            "------------------------\n"\
            "The tabs at the top are the major body part, once selected, you will be able to select an exercise. " \
            "Then, you can get both the description from Wikipedia, and a YouTube video on how to perform the exercise"
        textBox.insert(tk.END, About)
        textBox.configure(state='disabled')

class dictFrame(tk.Frame):
    """
    Frame class for each workout region
    """
    def __init__(self, parent, word):
        """
        Init method, produces the layout of the frame to be used in the notebook
        """
        tk.Frame.__init__(self, parent)
        dictOfWorkouts = {"Arms": ["Biceps Curl", "Triceps Extension"],
                          "Chest": ["Bench Press", "Push-up"],
                          "Back": ["Bent-over Row", "Deadlift"],
                          "Legs": ["Calf raises", "Squats", "Leg Curl"],
                          "Core": ["Russian Twist"]}
        listOfWorkouts = sorted(dictOfWorkouts[word])  # Assign list
        dictFrame.columnconfigure(self, 3, weight=1)
        dictFrame.columnconfigure(self, 2, weight=1)

        # Widget management
        workoutsLabel = tk.Label(self, text="Workouts: ")  # Create label
        workouts_CB = ttk.Combobox(self)        # Create combobox

        # Maps buttons to commands
        wikiButton = tk.Button(self, text="Information from Wikipedia", command=lambda: commands.accessWiki(self, workouts_CB.get()))
        ytButton = tk.Button(self, text="Find Exercise guide on Youtube", command=lambda: commands.accessYoutube(self, workouts_CB.get()))

        # Geometry management
        workoutsLabel.grid(row=0, column=0, sticky=tk.E + tk.W)
        workouts_CB.grid(row=0, column=1)
        wikiButton.grid(row=0, column=2, sticky=tk.E + tk.W)
        ytButton.grid(row=0, column=3, sticky=tk.E + tk.W)

#        exercises = tk.StringVar()
        workouts_CB['values'] = listOfWorkouts
