from pathlib import Path
import tkinter as tk
from utils import utils


# Create a function to format the dictionary properly
def form(name, description, hp, xp, location, power, attack1, attack2, attack3):
    data = dict(
            name=name,
            description=description,
            hp=hp,
            xp=xp,
            location=location,
            power=power,
            attack1=attack1,
            attack2=attack2,
            attack3=attack3,
    )
    return data


def save():

    location = location_entry.get()
    name = name_entry.get()

    # dict prep and file location
    dictionary = form(
            name_entry.get(),
            description_entry.get(),
            hp_entry.get(),
            xp_entry.get(),
            location_entry.get(),
            power_entry.get(),
            attack1_entry.get(),
            attack2_entry.get(),
            attack3_entry.get()
            )
    path = f'data/monsters/{location}'
    file = f'data/monsters/{location}/{name}.yml'

    # check for path directories and create if needed
    Path(path).mkdir(parents=True, exist_ok=True)

    # write out and update status label
    utils.write(dictionary, file)
    status_label["text"] = "Saved"


def clear():
    # Clear form fields
    name_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    xp_entry.delete(0, tk.END)
    location_entry.delete(0, tk.END)
    power_entry.delete(0, tk.END)
    attack1_entry.delete(0, tk.END)
    attack2_entry.delete(0, tk.END)
    attack3_entry.delete(0, tk.END)

    # update status label
    status_label["text"] = "Cleared"

if __name__ == "__main__":

    # Create a Tkinter window
    window = tk.Tk()

    # Set the window title
    window.title("Options")

    # Create creature label and entry
    name_label = tk.Label(text="Name")
    name_entry = tk.Entry()

    # Create description label and entry
    description_label = tk.Label(text="description")
    description_entry = tk.Entry()

    # Create hp label and entry
    hp_label = tk.Label(text="hitpoints")
    hp_entry = tk.Entry()

    # Create experience label and entry
    xp_label = tk.Label(text="xp")
    xp_entry = tk.Entry()

    # Create location label and entry
    location_label = tk.Label(text="location")
    location_entry = tk.Entry()

    # Create power label and entry
    power_label = tk.Label(text="power level")
    power_entry = tk.Entry()

    # Create attack flavor1 label and entry
    attack1_label = tk.Label(text="attack flavor text 1")
    attack1_entry = tk.Entry()

    # Create attack flavor2 label and entry
    attack2_label = tk.Label(text="attack flavor text 2")
    attack2_entry = tk.Entry()

    # Create attack flavor3 label and entry
    attack3_label = tk.Label(text="attack flavor text 3")
    attack3_entry = tk.Entry()

    # Create the buttons
    save_button = tk.Button(window, text="Save", command=save)
    clear_button = tk.Button(window, text="Clear", command=clear)

    # Create a status label that is empty
    status_label = tk.Label(text="")

    # Add creature name label and entry to window
    name_label.pack()
    name_entry.pack()

    # Add creature description label and entry to window
    description_label.pack()
    description_entry.pack()

    # Add creature hp label and entry to window
    hp_label.pack()
    hp_entry.pack()

    # Add creature xp label and entry to window
    xp_label.pack()
    xp_entry.pack()

    # Add creature location label and entry to window
    location_label.pack()
    location_entry.pack()

    # Add creature power label and entry to window
    power_label.pack()
    power_entry.pack()

    # Add creature attack1 label and entry to window
    attack1_label.pack()
    attack1_entry.pack()

    # Add creature attack2 label and entry to window
    attack2_label.pack()
    attack2_entry.pack()

    # Add creature attack3 label and entry to window
    attack3_label.pack()
    attack3_entry.pack()

    # Add the buttons to the window
    save_button.pack()
    clear_button.pack()

    # Add the status label to window
    status_label.pack()

    # Run the Tkinter event loop
    window.mainloop()
