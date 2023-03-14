import tkinter as tk
from utils import utils


# Create a function to format the dictionary properly
def form(name, description, hp):
    data = dict(
            name=name,
            description=description,
            hp=hp,
    )
    return data


def save():
    # get the values from form
    name = name_entry.get()
    description = description_entry.get()
    hp = hp_entry.get()

    # dict prep and file location
    dictionary = form(name, description, hp)
    path = f'data/{name}.yml'

    # write out and update status label
    utils.write(dictionary, path)
    status_label["text"] = "Saved"


def clear():
    # Clear form fields
    name_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    hp_entry.delete(0, tk.END)

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

    # Create creature label and entry
    hp_label = tk.Label(text="hitpoint")
    hp_entry = tk.Entry()

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

    # Add creature name label and entry to window
    hp_label.pack()
    hp_entry.pack()

    # Add the buttons to the window
    save_button.pack()
    clear_button.pack()

    # Add the status label to window
    status_label.pack()

    # Run the Tkinter event loop
    window.mainloop()
