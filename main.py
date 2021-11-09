# Author: Danny Chung
# Date: 10/21/21
# Description: This is a gym application

from tkinter import *
from frames import *

# Main initialization and style configuration
root = Tk()
root.title("Gymcyclopedia")
root.geometry("800x400")
root.columnconfigure(1, weight=1)

style = ttk.Style()
style.theme_create("CustomStyle", parent="alt", settings={
    "TNotebook": {"configure": {"tabmargins": [1, 1, 1, 0]}},
    "TNotebook.Tab": {"configure": {"padding": [10, 10], "sticky": tk.E+tk.W}}
})
style.theme_use("CustomStyle")

# Tab Widget management
notebook = ttk.Notebook(root)
notebook.pack(fill=BOTH, expand=TRUE)

# Tab creation and addition
homeTab = homeFrame(notebook)
armTab = dictFrame(notebook, "Arms")
chestTab = dictFrame(notebook, "Chest")
backTab = dictFrame(notebook, "Back")
legsTab = dictFrame(notebook, "Legs")
coreTab = dictFrame(notebook, "Core")
notebook.add(homeTab, text="Home")
notebook.add(armTab, text="Arms")
notebook.add(chestTab, text="Chest")
notebook.add(backTab, text="Back")
notebook.add(legsTab, text="Legs")
notebook.add(coreTab, text="Core")



root.mainloop()
