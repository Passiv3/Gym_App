# Author: Danny Chung
# Date: 10/26/21
# Description: Commands for tkinter buttons

import tkinter as tk
import requests
from tkinter import ttk

def accessWiki(input):
    """Utilizes Colin's Wikipedia scraper"""
    response = requests.get('http://localhost:6989/get_scraped/'+str(input))        # Makes http request to microservice
    newText = tk.Text(height=10, width=50, wrap="word")     # Creates Tkinter textbox
    newText.insert(tk.END, response.content)            # Writes response's content to text box
    newText.pack(side='top')              # Handles geometry


def accessYoutube(input):
    """Utilizes Danny's Scraper"""
    response = requests.get('http://localhost:8888/get_video/'+str(input))
    newText= tk.Text(height=20, width=20, wrap="word")
    newText.insert(tk.END, response.content)
    newText.pack()
