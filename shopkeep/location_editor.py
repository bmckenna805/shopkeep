from pathlib import Path
import tkinter as tk
from utils import utils


# Create a function to format the dictionary properly
def form(name, description, flavor1, flavor2, flavor3):
    data = dict(
            name=name,
            description=description,
            flavor1=flavor1,
            flavor2=flavor2,
            flavor3=flavor3,
    )
    return data


def save():

    name = name_entry.get()

    # dict prep and file location
    dictionary = form(
            name_entry.get(),
            description_entry.get(),
            flavor1_entry.get(),
            flavor2_entry.get(),
            flavor3_entry.get()
            )
    path = 'data/locations/'
    file = f'data/locations/{name}.yml'

    # check for path directories and create if needed
    Path(path).mkdir(parents=True, exist_ok=True)

    # write out and update status label
    utils.write(dictionary, file)
    status_label["text"] = "Saved"


def clear():
    # Clear form fields
    name_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    flavor1_entry.delete(0, tk.END)
    flavor2_entry.delete(0, tk.END)
    flavor3_entry.delete(0, tk.END)

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

    # Create flavor1 label and entry
    flavor1_label = tk.Label(text="location flavor text 1")
    flavor1_entry = tk.Entry()

    # Create flavor2 label and entry
    flavor2_label = tk.Label(text="location flavor text 2")
    flavor2_entry = tk.Entry()

    # Create flavor3 label and entry
    flavor3_label = tk.Label(text="location flavor text 3")
    flavor3_entry = tk.Entry()

    # Create the buttons
    save_button = tk.Button(window, text="Save", command=save)
    clear_button = tk.Button(window, text="Clear", command=clear)

    # Create a status label that is empty
    status_label = tk.Label(text="")

    # Add location name label and entry to window
    name_label.pack()
    name_entry.pack()

    # Add location description label and entry to window
    description_label.pack()
    description_entry.pack()

    # Add location flavor1 label and entry to window
    flavor1_label.pack()
    flavor1_entry.pack()

    # Add location flavor2 label and entry to window
    flavor2_label.pack()
    flavor2_entry.pack()

    # Add location flavor3 label and entry to window
    flavor3_label.pack()
    flavor3_entry.pack()

    # Add the buttons to the window
    save_button.pack()
    clear_button.pack()

    # Add the status label to window
    status_label.pack()

    # Run the Tkinter event loop
    window.mainloop()
