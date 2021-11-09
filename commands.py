# Author: Danny Chung
# Date: 10/26/21
# Description: Commands for tkinter buttons

import tkinter as tk
import requests

def accessWiki(parent, input):
    """Utilizes Colin's Wikipedia scraper"""
    response = requests.get('http://localhost:6989/get_scraped/'+str(input))        # Makes http request to microservice
    newText = tk.Text(parent, height=10, width=50, wrap="word")     # Creates Tkinter textbox
    newText.insert(tk.END, response.content)            # Writes response's content to text box
    newText.configure(state='disabled')
    newText.grid(row=1, column=0, sticky=tk.E+tk.W, columnspan=4)              # Handles geometry


def accessYoutube(parent, input):
    """Utilizes Danny's Scraper"""
    response = requests.get('http://localhost:8888/get_video/'+str(input))
    newText = tk.Text(parent, height=10, width=50, wrap="word")
    newText.insert(tk.END, response.content)
    newText.configure(state='disabled')
    newText.grid(row=2, column=0, sticky=tk.E+tk.W, columnspan=4)
